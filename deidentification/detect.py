# -*- coding: utf-8 -*-

import argparse
import time
from pathlib import Path
import numpy as np
import cv2
import warnings
warnings.filterwarnings('ignore')
import os
import sys
import gc
gc.collect()
from tqdm import tqdm
from PySide6.QtCore import QThread, Signal
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import onnx
import io
import onnxruntime as ort

VIDEO_EXTENSIONS = ['.mp4']
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg']

sys.path.insert(0, './deidentification')

class DetectThread(QThread):
    mosaic_processing_signal = Signal(int)
    mosaic_path_signal = Signal(str)
    
    def __init__(self, image_path=''):
        super().__init__()
        self.image_path = image_path
        self.working = True
        self.weights = './deidentification/models/encrypted_3t.onnx'
        self.view_img = True
        self.save_txt = True
        self.imgsz = 416
        self.trace = False
        self.dtype = 'mosaic'
        self.classes = 0
        self.select_classes = []
        self.dataset = None
        self.person_classes_list = ["Person", "Head", "Car"]
        self.car_classes_list = ["Car"]
        self.model = None
        self.model_upload_flag = False
        self.save_with_object_id = True
        self.save_bbox_dim = True
        self.strength = 25
        self.ready_flag = False
        self.resize_width = 640
        self.resize_height = 640

    def loading(self):
        from deidentification.utils import Sort, Detect_Model
        import logging
        import traceback

        # Configure logging
        logging.basicConfig(level=logging.INFO)
        
        try:
            self.sort_tracker = Sort.Sort(max_age=5, min_hits=2, iou_threshold=0.2)
            self.detected_objects = []
            self.total_detection_time = 0.0
            self.frame_count = 0

            start_time = time.time()
            logging.info("Loading model...")
            ######################## 모델 암호화 ###########################
            encrypted_model_path = self.weights
            key = bytes.fromhex('e287dcf90a4f3e5376d5bc9313202633605f2489c087c2589dfa24990a3565c1')
            with open(encrypted_model_path, 'rb') as f:
                iv = f.read(16)
                encrypted_data = f.read()

            backend = default_backend()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            decryptor = cipher.decryptor()

            decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

            model = onnx.load_model(io.BytesIO(data))
            self.model = model.SerializeToString()

            # Pass model_bytes to Detect_Model
            self.detect_model = Detect_Model.Detect_Model(self.model, conf_thres=0.3, iou_thres=0.3)
            ###################################################
            dummy_frame = np.zeros((1, 1, 3), dtype=np.uint8)
            self.detect_model(dummy_frame)

            end_time = time.time()
            logging.info(f"Model loading time: {end_time - start_time:.2f} seconds")
        except Exception as e:
            logging.error("An error occurred during model loading.")
            logging.error(traceback.format_exc())

    def run(self):
        if self.model is None:
            self.loading()
            self.model_upload_flag = True
            
        if self.ready_flag == True:
            
            save_path = ""
            select_classes_num = []
            for i in self.select_classes:        
                if i == "Person":
                    select_classes_num.append(0)
                if i == "Head":
                    select_classes_num.append(1)
                if i == "Car":
                    select_classes_num.append(2)
                    
            if len(select_classes_num) > 0:
                filename, file_extension = os.path.splitext(self.image_path)
                if file_extension.lower() in IMAGE_EXTENSIONS:
                    file_type = 'image'
                    extension = file_extension.lower()
                    output_path = self.process_image(extension)
                elif file_extension.lower() in VIDEO_EXTENSIONS:
                    file_type = 'video'
                    output_path = self.process_video()
                    
                print("사람모델 완료")
                self.image_path = output_path
            
            # if len(save_path) > 0:
            self.mosaic_path_signal.emit(self.image_path)
            
            self.ready_flag = False
            
    def process_video(self):
        
        from deidentification.utils import plots
        
        self.mosaic_processing_signal.emit(0)
        cap = cv2.VideoCapture(self.image_path)

        if not cap.isOpened():
            print(f"{self.image_path}에서 비디오 스트림 또는 파일을 열 수 없습니다")
            return

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))  # 원본 프레임 FPS 가져오기
        frame_all_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        out = cv2.VideoWriter(self.image_path + '_mosaic.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))
        
        result_path = self.image_path + '_mosaic.mp4'
        
        total_detection_time = 0.0
        frame_count = 0
        frame_objects_dict = {}
        
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame_count += 1
            start_time = time.time()

            # 원본 이미지의 종횡비 유지하면서 모델 입력 크기에 맞게 패딩 추가
            h, w, _ = frame.shape
            scale = min(self.resize_width / w, self.resize_height / h)
            new_w = int(w * scale)
            new_h = int(h * scale)
            resized_frame = cv2.resize(frame, (new_w, new_h))

            top = (self.resize_height - new_h) // 2
            bottom = self.resize_height - new_h - top
            left = (self.resize_width - new_w) // 2
            right = self.resize_width - new_w - left

            padded_frame = cv2.copyMakeBorder(resized_frame, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

            # YOLOv7 모델로 객체 감지
            boxes, scores, class_ids = self.detect_model(padded_frame)

            dets_to_sort = np.empty((0, 6), dtype=np.float32)
            data = []

            for box, score, class_id in zip(boxes, scores, class_ids):
                # 패딩된 좌표를 원본 프레임 크기로 변환
                x1_padded, y1_padded, x2_padded, y2_padded = box.astype(int)
                
                x1 = max(0, int((x1_padded - left) / scale))
                y1 = max(0, int((y1_padded - top) / scale))
                x2 = min(w, int((x2_padded - left) / scale))
                y2 = min(h, int((y2_padded - top) / scale))

                x_center = ((x1 + x2) / 2) / frame.shape[1]
                y_center = ((y1 + y2) / 2) / frame.shape[0]
                w_norm = (x2 - x1) / frame.shape[1]
                h_norm = (y2 - y1) / frame.shape[0]
                det_info = np.array([[x1, y1, x2, y2, score, class_id]], dtype=np.float32)
                dets_to_sort = np.vstack([dets_to_sort, det_info])
                data.append([0, class_id, x_center, y_center, w_norm, h_norm])

                # 바운딩 박스 그리기
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # 파란색, 두께 2 


            # 적용 범위를 빼고 삭제
            if 'Person' not in self.select_classes:
                data = [d for d in data if d[1] != 0]# Remove data with class_id == 0 (person)

            if 'Head' not in self.select_classes:
                data = [d for d in data if d[1] != 1]  # Remove data with class_id == 1 (head)

            if 'Car' not in self.select_classes:
                data = [d for d in data if d[1] != 2]  # Remove data with class_id == 2 (car)

            # 블러 또는 모자이크 적용
            if self.dtype == 'mosaic':
                frame = plots.Bounding_box_coordinates_mosaic(data, frame, self.strength, self.imgsz)
            else:
                frame = plots.Bounding_box_coordinates_blur(data, frame, self.strength, 1.5)

            trackers = self.sort_tracker.update(dets_to_sort)
            tracks = self.sort_tracker.getTrackers()

            frame_objects = []
            for track in tracks:
                if track.detclass == '':
                    continue

                x_normalized = track.centroidarr[-1][0] / frame_width
                y_normalized = track.centroidarr[-1][1] / frame_height
                width_normalized = (track.bbox_history[-1][2] - track.bbox_history[-1][0]) / frame_width
                height_normalized = (track.bbox_history[-1][3] - track.bbox_history[-1][1]) / frame_height

                object_coords = (track.detclass, track.id + 1, (x_normalized, y_normalized, width_normalized, height_normalized))
                frame_objects.append(object_coords)

                if frame_count not in frame_objects_dict:
                    frame_objects_dict[frame_count] = []
                frame_objects_dict[frame_count].append(object_coords)

            self.detected_objects.append(frame_objects)
            out.write(frame)

            end_time = time.time()

            detection_time_ms = (end_time - start_time) * 1000
            total_detection_time += detection_time_ms
            detection_time_sec = detection_time_ms / 1000

            print(f"프레임 {frame_count}의 탐지 시간: {detection_time_sec:.2f} 초")
            
            pro_value = int(frame_count/frame_all_count*100)
            self.mosaic_processing_signal.emit(pro_value)

            if not frame_objects:
                continue
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        print(f"{frame_count} 프레임의 총 탐지 시간: {total_detection_time / 1000:.2f} 초")

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        print("\n프레임별 감지된 객체 정보:")
        # for frame_num, objects_list in frame_objects_dict.items():
        #     print(f"프레임 {frame_num}의 감지된 객체 정보:")
        #     # ID가 0인 객체 수를 세어 사람수라고 표현
        #     person_count = sum(1 for obj in objects_list if obj[0] == 0) 
        #     print(f"사람 수: {person_count}")
        #     # 모든 좌표 출력
        #     for obj in objects_list:
        #         print(f"{obj[0]}, ID: {obj[1]}, 좌표: {obj[2]}")
        return result_path

    def process_image(self, extension):
                
        from deidentification.utils import plots
        
        frame = read_image(self.image_path)

        if frame is None:
            print(f"{self.image_path}에서 이미지를 열 수 없습니다")
            return
        self.mosaic_processing_signal.emit(0)
        start_time = time.time()
        
        h, w, _ = frame.shape
        scale = min(self.resize_width / w, self.resize_height / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized_frame = cv2.resize(frame, (new_w, new_h))

        top = (self.resize_height - new_h) // 2
        bottom = self.resize_height - new_h - top
        left = (self.resize_width - new_w) // 2
        right = self.resize_width - new_w - left

        padded_frame = cv2.copyMakeBorder(resized_frame, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        
        boxes, scores, class_ids = self.detect_model(padded_frame)
        end_time = time.time()
        self.mosaic_processing_signal.emit(30)
        detection_time_ms = (end_time - start_time) * 1000
        detection_time_sec = detection_time_ms / 1000
        print(f"이미지의 탐지 시간: {detection_time_sec:.2f} 초")

        data = []
        dets_to_sort = np.empty((0, 6), dtype=np.float32)
        for box, score, class_id in zip(boxes, scores, class_ids):
            # 패딩된 좌표를 원본 프레임 크기로 변환
            x1_padded, y1_padded, x2_padded, y2_padded = box.astype(int)
            
            x1 = max(0, int((x1_padded - left) / scale))
            y1 = max(0, int((y1_padded - top) / scale))
            x2 = min(w, int((x2_padded - left) / scale))
            y2 = min(h, int((y2_padded - top) / scale))

            x_center = ((x1 + x2) / 2) / frame.shape[1]
            y_center = ((y1 + y2) / 2) / frame.shape[0]
            w_norm = (x2 - x1) / frame.shape[1]
            h_norm = (y2 - y1) / frame.shape[0]
            det_info = np.array([[x1, y1, x2, y2, score, class_id]], dtype=np.float32)
            dets_to_sort = np.vstack([dets_to_sort, det_info])
            data.append([0, class_id, x_center, y_center, w_norm, h_norm])
            
            
        self.mosaic_processing_signal.emit(60)
            # 바운딩 박스 그리기
            #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # 파란색, 두께 2

        # 적용 범위를 빼고 삭제
        if 'Person' not in self.select_classes:
            data = [d for d in data if d[1] != 0]# Remove data with class_id == 0 (person)

        if 'Head' not in self.select_classes:
            data = [d for d in data if d[1] != 1]  # Remove data with class_id == 1 (head)

        if 'Car' not in self.select_classes:
            data = [d for d in data if d[1] != 2]  # Remove data with class_id == 2 (car)
            
        self.mosaic_processing_signal.emit(80)
        
        # 블러 or 모자이크 적용
        if self.dtype == 'mosaic':
            frame = plots.Bounding_box_coordinates_mosaic(data, frame, self.strength, self.imgsz)
        else:
            frame = plots.Bounding_box_coordinates_blur(data, frame, self.strength, 1.2)
        
        filename, file_extension = os.path.splitext(self.image_path)
        
        output_path = filename + f'_mosaic{extension}'
        cv2.imwrite(output_path, frame)
        print(f"탐지 결과 이미지가 {output_path}에 저장되었습니다.")
        self.mosaic_processing_signal.emit(100)
        return output_path
        
    
    
    # def merge_video_audio_clip(self, image_path, save_path):
    #     # 원본 오디오 클립 추출
    #     self.audio_clip = AudioFileClip(image_path)
    #     # 작업한 비디오 클립 추출
    #     video_clip = VideoFileClip(save_path)
        
    #     save_file_path, file_name = os.path.split(save_path)
    #     only_file_name, extension = os.path.splitext(file_name)
    #     new_save_path = os.path.join(save_file_path, only_file_name + "_aa"+extension)
    #     # 오디오를 비디오에 추가
    #     video_clip.audio = self.audio_clip
    #     # 비디오와 오디오를 결합한 새로운 비디오를 저장
    #     video_clip.write_videofile(new_save_path, codec='libx264')
    #     # 작업이 완료되면 파일을 닫아줍니다.
    #     video_clip.close()
    #     self.audio_clip.close()
        
        
    #     return new_save_path
    
    def draw_boxes(self, img, bbox, identities=None, categories=None, names=None, save_with_object_id=False, path=None):
    
        save_path, file_name = os.path.split(path)
        print("file_name : ", file_name)
        re_file_name, extension = os.path.splitext(file_name)
        print("re_file_name, extension : ", re_file_name, extension)
        target_path = os.path.join(save_path, re_file_name)
        os.makedirs(target_path, exist_ok=True)
        im0 = img.copy()
        
        for i, box in enumerate(bbox):
            x1, y1, x2, y2 = [int(i) for i in box]
            tl = 2 or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness

            cat = int(categories[i]) if categories is not None else 0
            id = int(identities[i]) if identities is not None else 0
            # conf = confidences[i] if confidences is not None else 0

            color = (255,0,20)
            target_file_name = re_file_name + "_" + str(id) + extension
            target_file_path = os.path.join(target_path, target_file_name)
            # print(target_file_path)
            
            target_img = im0[y1:y2, x1:x2]
            # print(target_img.shape)
            # cv2.imwrite(target_file_path, target_img)
            # if not opt.nobbox:
            if y1 < 0 or y2 < 0 or x1 < 0 or x2 < 0:
                print("x1, y1, x2, y2 : ", x1, y1, x2, y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, tl)

            # if not opt.nolabel:
            if id is not None:
                label = f"{id}:{names[cat]}"
            else:
                label = names[cat]
                
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(img, label, (x1, y1 - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        return img
    
        
    def stop(self):
        self.working = False
        self.quit()
        self.wait()
    
    def __del__(self):
        self.wait()
        
def read_image(image_path):
    # np.fromfile을 사용하여 파일을 바이트 배열로 읽기
    file_bytes = np.fromfile(image_path, np.uint8)
    
    # cv2.imdecode를 사용하여 이미지를 디코딩
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    return image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    #     # parser.add_argument('--self.rtsp_url', type=str, default='rtsp://admin:sijung5520@192.168.100.133/profile4/media.smp',
    #                     help='self.rtsp_url')  # file/folder, 0 for webcam
    parser.add_argument('--self.rtsp_url', type=str, default='rtsp://admin:sijung5520@192.168.100.30/profile4/media.smp',
                        help='self.rtsp_url')  # file/folder, 0 for webcam
    # parser.add_argument('--self.rtsp_url', type=str, default='rtsp://assist:sijung1234@sihwa.iptime.org:554/cam0_0',
    #                     help='self.rtsp_url')  # file/folder, 0 for webcam
    parser.add_argument('--type', type=str, default='box', help='detect type')
    parser.add_argument('--img-size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    parser.add_argument('--area', type=int, default=21, help='input area')
    opt = parser.parse_args()

    # check_requirements(exclude=('pycocotools', 'thop'))

    # with torch.no_grad():
    #     if opt.update:  # update all models (to fix self.rtsp_urlChangeWarning)
    #         for opt.weights in ['yolov7.pt']:
    #             detect()
    #             # strip_optimizer(opt.weights)
    #     else:
    #         detect()

    # detect()
