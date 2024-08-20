# -*- coding: utf-8 -*-

import shutil
import time
import zipfile
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox, QFileDialog, QStyle, QPushButton, QSlider
from PySide6.QtCore import Qt, QThread, Signal, QTimer, QDateTime, QUrl
from PySide6.QtGui import QPixmap, QImage, QPainter, QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
import requests

from resources.mz01_main_v4 import Ui_mz01_main_v2  # YourMainWindow은 실제로 변환된 UI 클래스명일 수 있습니다.
import sys
import cv2
import os
import subprocess

# 로딩창을 먼저 띄우기 위해 아래로 선언
from deidentification.detect import DetectThread

    
class MainWidget(QMainWindow, Ui_mz01_main_v2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appIcon = QIcon('new_logo.png')
        self.setWindowIcon(appIcon)
        self.pushButton_5.show()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_6.hide()
        # 창 테두리와 닫기 버튼 제거
        # 최대화 및 창 테두리, 메뉴, 상태 창 숨기기
        # self.setWindowFlags(self.windowFlags() | 
        #                     Qt.FramelessWindowHint | 
        #                     Qt.WindowMaximizeButtonHint)
        # self.setWindowState(Qt.WindowMaximized)
        
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.is_main = False
        self.save_path = None
        self.ori_img_label = QLabel(self)
        self.mozaic_img_label = QLabel(self)
        self.videoWidget = QVideoWidget(self)  # QVideoWidget 생성
        self.videoWidget.setGeometry(540, 50, 890, 580)  # 위치 및 크기 설정
        self.videoWidget.hide()
        self.label_2.hide()
        self.v_duration = None
        self.mosaic_flag = False
        self.image_path = None
        self.finish_flag = False
        self.mediaPlayer = None
        self.is_fullscreen = False  # 풀스크린 상태를 추적하는 변수
        
        self.mosaic_videoWidget = QVideoWidget(self)  # QVideoWidget 생성
        self.mosaic_videoWidget.setGeometry(960, 50, 890, 580)  # 위치 및 크기 설정
        self.mosaic_videoWidget.hide()
        
        self.playButton = QPushButton(self)
        self.playButton.setEnabled(True)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        self.playButton.setGeometry(680, 660, 20, 20)  # 위치 및 크기 설정
        self.playButton.hide()
        
        self.positionSlider = QSlider(Qt.Horizontal, self)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.positionSlider.setGeometry(710, 660, 560, 20)
        self.positionSlider.hide()
        
        self.pushButton_2.clicked.connect(self.openFile)
        self.pushButton_3.clicked.connect(self.init_image)
        self.pushButton_6.clicked.connect(self.openSaveFolder)
        self.pushButton_5.clicked.connect(self.quit_app)
        self.pushButton.clicked.connect(self.start_mozaic)
        self.pixmap = None
        self.classes = None
        self.dtype = None
        self.strength = None
        self.img_formats = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']  # acceptable image suffixes
        self.vid_formats = ['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv']  # acceptable video suffixes
        
        self.comboBox.currentIndexChanged.connect(self.updateSliderValue)
        self.horizontalSlider.valueChanged.connect(self.update_combo_value)
        
        
        self.detect_thread = DetectThread()
        
        self.detect_thread.mosaic_path_signal.connect(self.mosaic_image_upload)
        
        self.detect_thread.mosaic_processing_signal.connect(self.mosaic_processing)
        
        self.detect_thread.start() # 하위 스레드로 하려면 필수임
        # self.test_thread = Worker()
        # self.test_thread.start()
        # self.test_thread.timeout.connect(self.test_tt)
    
    def openSaveFolder(self):

        if self.mosaic_flag == True:
            return

        if self.save_path is not None:

            folder_path = os.path.split(self.save_path)[0]
            os.startfile(folder_path)
        
    def update_combo_value(self, value):
        idx = value // 10
        self.comboBox.setCurrentIndex(idx)
        
    def updateSliderValue(self, index):
        # 콤보 박스에서 선택한 값에 따라 슬라이더와 레이블의 값을 변경
        value = (index) * 10
        print("value : ", value)
        self.horizontalSlider.setValue(value)
    
    def openFile(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, a = QFileDialog.getOpenFileName(self, "파일 열기", "", "비디오 파일 (*.mp4 *.avi *.mov);;이미지 파일 (*.jpg *.png *.bmp *.gif);;모든 파일 (*)")
        if fileName:
            self.checkable_file_format(fileName)
            
    def mosaic_processing(self, i):
        self.progressBar.setValue(i)
        
    def quit_app(self):
        # 애플리케이션을 종료합니다.
        QApplication.quit()
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.checkable_file_format(file_path)
            break
    
    def checkable_file_format(self, file_path):       
        
        if self.mosaic_flag == True or self.finish_flag == True:
            return
        
        file_name = os.path.split(file_path)[1]
        name, ext = os.path.splitext(file_name)
        ext_split = ext.split('.')[1]
        
        # self.image_path = urllib.parse.quote(file_path)
        self.image_path = file_path
        print("self.image_path1111 : ", self.image_path)
        
        if ext_split in self.img_formats:
            
            self.pixmap = QPixmap(file_path)
            self.ori_img_label.setGeometry(540, 50, 890, 620)
            self.ori_img_label.setPixmap(self.pixmap.scaled(self.ori_img_label.size(), Qt.KeepAspectRatio))
            self.upload_image()
        
        elif ext_split in self.vid_formats:
            
            self.upload_video(QUrl.fromLocalFile(self.image_path))
        
        else:
            QMessageBox.information(self, "에러 메세지", "파일 형식이 잘못됐습니다.")
        
        self.progressBar.setValue(0)
        self.label_2.hide()
    
    def init_image(self):
        """이미지 초기화 버튼을 눌렀을 때"""
        # 이전 동영상 재생 중지 및 QMediaPlayer 객체 삭제
        
        if self.mosaic_flag == True:
            return
            
        
        if hasattr(self, 'mediaPlayer') and self.mediaPlayer is not None:
            self.mediaPlayer.setPosition(self.v_duration)
            self.mediaPlayer.stop()
            self.mediaPlayer=None
        self.label.show()
        self.pushButton_2.show()
        self.ori_img_label.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_6.hide()
        self.pushButton.show()
        self.mozaic_img_label.hide()
        self.pushButton.move(1040,920)
        
        self.videoWidget.hide()
        self.playButton.hide()
        self.positionSlider.hide()
        self.mosaic_videoWidget.hide()
        self.positionSlider.setValue(0)
        self.progressBar.setValue(0)
        self.image_path = None
        self.finish_flag = False
        
        
        self.label_2.hide()
    
    def upload_video(self, url):
        """비디오를 업로드 했을 때"""
        self.label.hide()
        self.pushButton_3.show()
        self.pushButton_2.hide()
        self.pushButton.move(1220,920)
        self.videoWidget.move(540, 50)  # 위치 설정


                # 이전 동영상 재생 중지 및 QMediaPlayer 객체 삭제
        if hasattr(self, 'mediaPlayer') and self.mediaPlayer is not None:
            self.mediaPlayer.setPosition(self.v_duration)
            self.mediaPlayer.stop()            
            self.mediaPlayer.setSource(url)
            self.mediaPlayer.setPosition(0)
            self.mediaPlayer.pause()
        else:
            
            self.mediaPlayer = QMediaPlayer()
            self.mediaPlayer.setVideoOutput(self.videoWidget)
            self.mediaPlayer.playingChanged.connect(self.mediaStateChanged)
            self.mediaPlayer.positionChanged.connect(self.positionChanged)
            self.mediaPlayer.durationChanged.connect(self.durationChanged)
            # 오류 시그널 연결
            self.mediaPlayer.errorOccurred.connect(self.handle_media_player_error)
            self.mediaPlayer.setSource(url)
            self.mediaPlayer.pause()
        
        self.videoWidget.show()  # QVideoWidget 표시
        self.playButton.show()
        self.positionSlider.show()
        
        
        
        self.mosaic_mediaPlayer = None
        
        # self.mediaPlayer.play()
    
    def handle_media_player_error(self, error):
        # 여기서 error는 QMediaPlayerError 타입입니다.
        error_message = f"Media Player Error: {error.errorString()}"
        print(error_message)
        # 필요하다면 사용자에게 오류를 표시하는 등의 추가 작업을 수행할 수 있습니다.
        
    def play(self):

        if self.mosaic_flag == True:
            return

        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            
            
            if self.mosaic_mediaPlayer is not None:
                self.mosaic_mediaPlayer.pause()
                self.mediaPlayer.pause()
            else:
                self.mediaPlayer.pause()
                
        else:
            if self.mosaic_mediaPlayer is not None:
                self.mosaic_mediaPlayer.play()
                self.mediaPlayer.play()
            else:
                self.mediaPlayer.play()
            
    def mediaStateChanged(self, state):
        if state == True:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.v_duration = duration
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
        
        if self.mosaic_mediaPlayer is not None:
                self.mosaic_mediaPlayer.setPosition(position)
                
        
    def upload_image(self):
        """이미지를 업로드 했을 때"""
        
        self.label.hide()
        self.pushButton_3.show()
        self.pushButton_2.hide()
        self.ori_img_label.show()
        self.pushButton.move(1220,920)
    
    def start_mozaic(self):
        """모자이크 버튼을 눌렀을 때"""
        
        if self.detect_thread.model_upload_flag == False:
            QMessageBox.information(self, "error", "AI 모델 업로드 중입니다. 잠시만 기다려주세요")
            return
        
        if self.image_path is None:
            QMessageBox.information(self, "error", "이미지 또는 동영상 파일을 넣어주세요")
            return
        self.classes_list = []
        self.mosaic_flag = True
        
        if self.mediaPlayer is not None:
            self.mediaPlayer.stop()        
        
        if self.checkBox.isChecked():
            self.classes = 0 # person
            self.classes_list.append("Person")
            
        if self.checkBox_2.isChecked():
            self.classes = 1 # head
            self.classes_list.append("Head")
            
        if self.checkBox_4.isChecked():
            self.classes = 2 # car
            self.classes_list.append("Car")
            print("self.image_path3333 : ", self.image_path)
        
        if len(self.classes_list) == 0:
            self.classes = 0
            self.classes_list.append("Person")

        if self.radioButton_3.isChecked():
            self.dtype = 'mosaic' # mosaic
            
        elif self.radioButton_4.isChecked():
            self.dtype = 'blur' # blur
        
        else:
            self.dtype = 'mosaic' # mosaic
            
        
        if self.comboBox.currentText() == "0%":
            self.strength = 20
        else:
            self.strength = int(self.comboBox.currentText().split("%")[0])
        
        self.detect_thread.image_path = self.image_path
        self.detect_thread.classes = self.classes
        self.detect_thread.select_classes = self.classes_list
        self.detect_thread.dtype = self.dtype
        self.detect_thread.strength = self.strength
        self.detect_thread.ready_flag = True
        self.detect_thread.start()
        
        
        self.pushButton_3.show()
        self.pushButton_6.show()        
        self.pushButton.hide()
        
        
        # self.detect_thread.stop()
        self.positionSlider.setValue(0)

    
    def mosaic_image_upload(self, image_path):
        
        current_directory = os.getcwd()  # 현재 작업 디렉토리를 얻음
        file_path = os.path.join(current_directory, image_path)
        file_name = os.path.split(image_path)[1]
        
        
        self.save_path = file_path
        name, ext = os.path.splitext(file_name)
        ext_split = ext.split('.')[1]
        
        if ext_split in self.img_formats:
            self.ori_img_label.setGeometry(50, 50, 890, 620)
            
            image = cv2.imread(file_path)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = rgb_image.shape
            bytesPerLine = 3 * width
            qImg = QImage(rgb_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            
            self.mosic_pixmap = QPixmap(qImg)
            self.mozaic_img_label.setGeometry(960, 50, 890, 620)
            self.mozaic_img_label.setPixmap(self.mosic_pixmap.scaled(self.mozaic_img_label.size(), Qt.KeepAspectRatio))
            self.mozaic_img_label.show()
        
        elif ext_split in self.vid_formats:
            
            
            
            url = QUrl.fromLocalFile(file_path)
            self.videoWidget.move(50, 50)
            self.mosaic_mediaPlayer = QMediaPlayer()
            self.mosaic_mediaPlayer.setVideoOutput(self.mosaic_videoWidget)
            self.mosaic_mediaPlayer.playingChanged.connect(self.mediaStateChanged)
            self.mosaic_mediaPlayer.durationChanged.connect(self.durationChanged)
            self.mosaic_mediaPlayer.setSource(url)
            self.mediaPlayer.setPosition(0)
            self.mosaic_mediaPlayer.pause()
            self.mediaPlayer.pause()
            self.mosaic_mediaPlayer.setPosition(0)
            self.mosaic_videoWidget.show()  # QVideoWidget 표시
        
        self.label_2.setText(f"저장위치 : {file_path}")
        self.label_2.show()
        self.mosaic_flag = False
        self.finish_flag = True
    
    # def mousePressEvent(self, event):
    #     # Store the positions of mouse and window and
    #     # change the window position relative to them.
    #     self.windowPos = self.pos()
    #     self.mousePos = event.globalPos()
    #     self.is_main = True
    #     super(MainWidget, self).mousePressEvent(event)

    # def mouseMoveEvent(self, event):
    #     if self.is_main:
    #         self.move(self.windowPos + event.globalPos() - self.mousePos)
    #     super(MainWidget, self).mouseMoveEvent(event)
        
    # def mouseReleaseEvent(self, event):
    #     self.is_main = False
    #     super(MainWidget, self).mouseReleaseEvent(event)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.toggle_fullscreen()

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.showNormal()
        else:
            self.showFullScreen()
        self.is_fullscreen = not self.is_fullscreen
        


if __name__ == '__main__':

    print("업데이트가 성공적으로 완료되었습니다.")
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec())

