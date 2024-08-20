
# 텍스트 좌표기반 이미지 모자이크
import math
import cv2
import numpy as np

def Bounding_box_coordinates_mosaic(data, img, strength,size):
    img_h, img_w = img.shape[:2]
    strength = strength
    size = size
    for line in data:
        # 좌표 정보를 추출하고 이미지 크기에 맞게 변환합니다.
        track_id ,class_id,x_center, y_center, w, h = map(float, line)
        x_center, y_center, w, h = int(math.ceil(x_center * img_w)), int(math.ceil(y_center * img_h)), int(math.ceil(w * img_w)), int(math.ceil(h * img_h))
        
        # 모자이크 적용할 영역의 좌표를 계산합니다.
        x1, y1 = max(0, x_center - w // 2), max(0, y_center - h // 2)
        x2, y2 = min(img_w, x_center + w // 2), min(img_h, y_center + h // 2)
        
        # 모자이크 적용할 영역을 추출합니다.
        mosaic_roi = img[y1:y2, x1:x2]

        # 객체 크기를 이미지 크기와 비교하여 비율을 계산합니다.
        object_area = w * h
        image_area = img_w * img_h
        object_ratio = object_area / image_area

        # 객체 크기 비율에 따른 모자이크 강도 조정 (작을수록 약하게)
        if object_ratio <= 0.1:
            strength_to_apply = int(strength * 0.1)
        elif object_ratio <= 0.2:
            strength_to_apply = int(strength * 0.2)
        elif object_ratio <= 0.3:
            strength_to_apply = int(strength * 0.3)
        elif object_ratio <= 0.4:
            strength_to_apply = int(strength * 0.4)
        elif object_ratio <= 0.5:
            strength_to_apply = int(strength * 0.5)
        elif object_ratio <= 0.6:
            strength_to_apply = int(strength * 0.6)
        elif object_ratio <= 0.7:
            strength_to_apply = int(strength * 0.7)
        elif object_ratio <= 0.8:
            strength_to_apply = int(strength * 0.8)
        elif object_ratio <= 0.9:
            strength_to_apply = int(strength * 0.9)
        else:
            strength_to_apply = int(strength * 1.0)

        # 모자이크 강도 설정 및 모자이크 적용
        while True:
            try:
                #mosaic_roi = cv2.resize(mosaic_roi, None, fx=1/strength_to_apply, fy=1/strength_to_apply, interpolation=cv2.INTER_NEAREST)
                mosaic_w = x2 - x1
                mosaic_h = y2 - y1
                if strength_to_apply <= 0:
                    strength_to_apply = 0.1
                mosaic_roi = cv2.resize(mosaic_roi, (mosaic_w // (strength_to_apply*10), mosaic_h // (strength_to_apply*10)), interpolation=cv2.INTER_NEAREST)
            except cv2.error:
                # 모자이크 강도가 너무 큰 경우 예외 처리 및 강도 조절
                strength_to_apply -= 1
                if strength_to_apply <= 1:
                    # 최소 강도까지 줄어들었는데도 축소가 안 되면 반복 종료
                    break
            else:
                # 축소가 성공한 경우 반복 종료
                break

        # 모자이크 적용된 영역을 원래 크기로 변환하여 모자이크를 적용합니다.
        mosaic_roi = cv2.resize(mosaic_roi, (x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)
        img[y1:y2, x1:x2] = mosaic_roi

    return img


# 텍스트 좌표기반 이미지 리사이즈 블러
def Bounding_box_coordinates_blur(data, img, strength,size):
    img_h, img_w = img.shape[:2]
    
    # 결과 이미지 생성 (원본 이미지와 동일한 크기와 타입)
    result_img = np.copy(img)
    strength = strength
    size = size
    
    for line in data:
        track_id, class_id, x_center, y_center, w, h = map(float, line)
        
        # 좌표 정보를 이미지 크기에 맞게 변환
        x_center, y_center = int(x_center * img_w), int(y_center * img_h)
        w, h = int(w * img_w), int(h * img_h)
        
        # 객체의 새로운 크기 계산 (1.5배 확대)
        new_w = min(w * size, img_w)
        new_h = min(h * size, img_h)
        
        # 새로운 좌상단, 우하단 좌표 계산
        x1 = max(int(x_center - new_w // 2), 0)
        y1 = max(int(y_center - new_h // 2), 0)
        x2 = min(int(x_center + new_w // 2), img_w)
        y2 = min(int(y_center + new_h // 2), img_h)
        
        # 좌표 부분 이미지 추출
        coord_img = result_img[y1:y2, x1:x2]
        
        sigma_adjusted = strength / 100 * 5

        # 비율 ~이하인 값은 리사이즈 하지 않기
        donotresizebelow = 0.3

        if w <= donotresizebelow or h <= donotresizebelow:
            resized_coord_img = coord_img
        else:
            # 크기가 클수록 더 작게 리사이즈하는 비율 계산
            if new_w > 0.9 or new_h > 0.9:
                resize_factor = 0.1  # 매우 큰 객체는 더 작게 리사이즈하여 뭉개기 효과
            elif new_w > 0.8 or new_h > 0.8:
                resize_factor = 0.2
            elif new_w > 0.7 or new_h > 0.7:
                resize_factor = 0.3
            elif new_w > 0.6 or new_h > 0.6:
                resize_factor = 0.4
            elif new_w > 0.5 or new_h > 0.5:
                resize_factor = 0.5
            elif new_w > 0.4 or new_h > 0.4:
                resize_factor = 0.6
            elif new_w > 0.3 or new_h > 0.3:
                resize_factor = 0.7
            elif new_w > 0.2 or new_h > 0.2:
                resize_factor = 0.8
            elif new_w > 0.1 or new_h > 0.1:
                resize_factor = 0.9
            # 좌표 부분 이미지를 작게 리사이즈합니다.
            resized_coord_img = cv2.resize(coord_img, None, fx=resize_factor, fy=resize_factor)

        # 가우시안 블러 적용
        blurred_resized_img = cv2.GaussianBlur(resized_coord_img, (15, 15), sigma_adjusted)


        if w <= donotresizebelow or h <= donotresizebelow:
            restored_img = blurred_resized_img
        else:
            # 리사이즈된 이미지를 다시 원래 크기로 되돌립니다.
            restored_img = cv2.resize(blurred_resized_img, (coord_img.shape[1], coord_img.shape[0]))

        # head 
        if int(class_id) == 1:
            # 원 모양의 마스크 생성
            mask = np.zeros_like(coord_img)
            cv2.circle(mask, (int(x_center - x1), int(y_center - y1)), min(int(new_w), int(new_h)) // 2, (255, 255, 255), -1)

                # 마스크 반전
            mask_inv = cv2.bitwise_not(mask)

            # 마스크를 이용하여 이미지를 조합
            result_img[y1:y2, x1:x2] = cv2.bitwise_and(coord_img, mask_inv) + cv2.bitwise_and(restored_img, mask)
        
        else:
            restored_img = cv2.resize(blurred_resized_img, (coord_img.shape[1], coord_img.shape[0]))
            result_img[y1:y2, x1:x2] = restored_img

    return result_img


