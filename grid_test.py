
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox, QFileDialog, QStyle, QPushButton, QSlider
from PySide6.QtCore import Qt, QThread, Signal, QTimer, QDateTime, QUrl
from PySide6.QtGui import QPixmap, QImage, QPainter, QIcon


from resources.mz01_main_v3_grid import Ui_MainWindow  # YourMainWindow은 실제로 변환된 UI 클래스명일 수 있습니다.
import sys


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec())