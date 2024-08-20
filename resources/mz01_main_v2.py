# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mz01_main_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_mz01_main_v2(object):
    def setupUi(self, mz01_main_v2):
        if not mz01_main_v2.objectName():
            mz01_main_v2.setObjectName(u"mz01_main_v2")
        mz01_main_v2.resize(1024, 680)
        mz01_main_v2.setMinimumSize(QSize(1024, 680))
        mz01_main_v2.setMaximumSize(QSize(1024, 680))
        mz01_main_v2.setStyleSheet(u"#mz01_main_v2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	border:3px;\n"
"    border-radius: 20px;\n"
"	border-color:rgb(0,0,0);\n"
"	Border-Style:solid;\n"
"	background-repeat: no-repeat\n"
"}")
        mz01_main_v2.setDocumentMode(False)
        mz01_main_v2.setDockNestingEnabled(True)
        self.centralwidget = QWidget(mz01_main_v2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 412, 80, 30))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515\ucf54\ub529"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"#label_3\n"
"{\n"
"	background-color:rgb(80,80,80);\n"
"	color:rgb(255,255,255);\n"
"    height: 30px;\n"
"	border-radius: 15;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(690, 420, 80, 16))
        self.checkBox.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\ub098\ub214\uace0\ub515\ucf54\ub529"])
        font1.setPointSize(12)
        self.checkBox.setFont(font1)
        self.checkBox.setStyleSheet(u"#checkBox\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(770, 420, 80, 16))
        self.checkBox_2.setMaximumSize(QSize(80, 16777215))
        self.checkBox_2.setFont(font1)
        self.checkBox_2.setStyleSheet(u"#checkBox_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(850, 420, 80, 16))
        self.checkBox_4.setMaximumSize(QSize(80, 16777215))
        self.checkBox_4.setFont(font1)
        self.checkBox_4.setStyleSheet(u"#checkBox_4\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1021, 671))
        self.widget.setStyleSheet(u"#widget{\n"
"	background-color:rgb(0,0,0);\n"
"	border:3px;\n"
"    border-radius: 20px;\n"
"	border-color:rgb(0,0,0);\n"
"	Border-Style:solid;\n"
"	background-repeat: no-repeat\n"
"\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 950, 350))
        self.label.setMinimumSize(QSize(950, 350))
        self.label.setMaximumSize(QSize(950, 350))
        font2 = QFont()
        font2.setFamilies([u"Agency FB"])
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet(u"#label\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"	Border-width:3px; \n"
"	Border-Style:dashed;\n"
"    border-radius: 15px;\n"
"	border-color: rgb(255,255,255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 230, 161, 41))
        font3 = QFont()
        font3.setFamilies([u"\ub098\ub214\uace0\ub515 ExtraBold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"#pushButton_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"	border:3px;\n"
"    border-radius: 20px;\n"
"	border-color:rgb(255,255,255);\n"
"	Border-Style:solid;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_2:pressed\n"
"{\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_2:hover\n"
"{\n"
"\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}")
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(190, 550, 271, 61))
        font4 = QFont()
        font4.setFamilies([u"\ub098\ub214\uace0\ub515\ucf54\ub529"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"#pushButton_3\n"
"{\n"
"	color:rgb(67,41,194);\n"
"	border:3px;\n"
"    border-radius: 30px;\n"
"	border-color:rgb(67,41,194);\n"
"	Border-Style:solid;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_3:pressed\n"
"{\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_3:hover\n"
"{\n"
"\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}")
        self.pushButton_3.setFlat(True)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, 550, 271, 61))
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"#pushButton_4\n"
"{\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:1px;\n"
"    border-radius: 30px;\n"
"	border-color:rgb(255,255,255);\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_4:pressed\n"
"{\n"
"	background-color:rgb(67,41,194);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton_4:hover\n"
"{\n"
"\n"
"	background-color:rgb(67,41,194);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}")
        self.pushButton_4.setFlat(True)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(110, 390, 351, 81))
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(500, 16777215))
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_2.setStyleSheet(u"#groupBox_2\n"
"{\n"
"	border: solid;\n"
"	border-color: rgb(0,0,0);\n"
"}")
        self.groupBox_2.setTitle(u"")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 30, 90, 16))
        self.radioButton_3.setFont(font1)
        self.radioButton_3.setStyleSheet(u"#radioButton_3\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.radioButton_3.setChecked(True)
        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(170, 30, 90, 16))
        self.radioButton_4.setFont(font1)
        self.radioButton_4.setStyleSheet(u"#radioButton_4\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 410, 80, 30))
        self.label_4.setMaximumSize(QSize(80, 16777215))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"#label_4\n"
"{\n"
"	background-color:rgb(80,80,80);\n"
"	color:rgb(255,255,255);\n"
"    height: 30px;\n"
"	border-radius: 15;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(910, 470, 81, 22))
        self.comboBox.setMinimumSize(QSize(81, 21))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"#comboBox\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"	Border-width:2px; \n"
"	Border-Style:solid;\n"
"	border-color: white;\n"
"}")
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.horizontalSlider = QSlider(self.widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(150, 475, 691, 22))
        self.horizontalSlider.setStyleSheet(u"#horizontalSlider::groove:horizontal {\n"
"    border-radius: 10px;\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"    background-color: rgb(117,91,244);\n"
"}\n"
"\n"
"#horizontalSlider::handle:horizontal {\n"
"    background-color: rgb(117,91,244);\n"
"    border: none;\n"
"    width: 15px;\n"
"    margin: -8px 0;\n"
"    border-radius: 7;\n"
"    padding: -8px 0px;\n"
"}\n"
"#horizontalSlider::handle:horizontal:hover {\n"
"    background-color: rgb(67,41,194);\n"
"}\n"
"#horizontalSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(67,41,194);\n"
"}\n"
"\n"
"#horizontalSlider::add-page:horizontal{\n"
"    background-color: rgb(100,100,100);\n"
"}")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setValue(20)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(10)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 472, 80, 30))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"#label_5\n"
"{\n"
"	background-color:rgb(80,80,80);\n"
"	color:rgb(255,255,255);\n"
"    height: 30px;\n"
"	border-radius: 15;\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 550, 271, 61))
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"#pushButton\n"
"{\n"
"	background-color:rgb(117,91,244);\n"
"	color:rgb(255,255,255);\n"
"	border:1px;\n"
"    border-radius: 30px;\n"
"	border-color:rgb(255,255,255);\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton:pressed\n"
"{\n"
"	background-color:rgb(67,41,194);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}\n"
"#pushButton:hover\n"
"{\n"
"\n"
"	background-color:rgb(67,41,194);\n"
"	color:rgb(255,255,255);\n"
"	border:0px;\n"
"	background-repeat: no-repeat\n"
"}")
        self.pushButton.setFlat(True)
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 630, 981, 15))
        self.progressBar.setStyleSheet(u"#progressBar\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.progressBar.setValue(0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(150, 510, 741, 20))
        self.label_2.setStyleSheet(u"#label_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(980, 10, 31, 31))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"#pushButton_5\n"
"{\n"
"    border-image: url(./resources/close_button.png);\n"
"	color:rgb(255,255,255);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#pushButton_5:pressed\n"
"{\n"
"    border-image: url(./resources/close_button.png);\n"
"	color:rgb(255,255,255);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#pushButton_5:hover\n"
"{\n"
"\n"
"    border-image: url(./resources/close_button_hover.png);\n"
"	color:rgb(255,255,255);\n"
"    background-repeat: no-repeat;\n"
"}")
        self.pushButton_5.setFlat(True)
        mz01_main_v2.setCentralWidget(self.centralwidget)
        self.widget.raise_()
        self.label_3.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_4.raise_()
        self.menubar = QMenuBar(mz01_main_v2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        mz01_main_v2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mz01_main_v2)
        self.statusbar.setObjectName(u"statusbar")
        mz01_main_v2.setStatusBar(self.statusbar)

        self.retranslateUi(mz01_main_v2)

        self.comboBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(mz01_main_v2)
    # setupUi

    def retranslateUi(self, mz01_main_v2):
        mz01_main_v2.setWindowTitle(QCoreApplication.translate("mz01_main_v2", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("mz01_main_v2", u"\uc801\uc6a9\ubc94\uc704", None))
        self.checkBox.setText(QCoreApplication.translate("mz01_main_v2", u"\uc0ac\ub78c", None))
        self.checkBox_2.setText(QCoreApplication.translate("mz01_main_v2", u"\uc5bc\uad74", None))
        self.checkBox_4.setText(QCoreApplication.translate("mz01_main_v2", u"\ubc88\ud638\ud310", None))
        self.label.setText(QCoreApplication.translate("mz01_main_v2", u"\ud30c\uc77c\uc744 \ub4dc\ub798\uadf8\ud574\uc11c \ub123\uc5b4\uc8fc\uc138\uc694.", None))
        self.pushButton_2.setText(QCoreApplication.translate("mz01_main_v2", u"+  \ud30c\uc77c \uc120\ud0dd", None))
        self.pushButton_3.setText(QCoreApplication.translate("mz01_main_v2", u"\uc774\ubbf8\uc9c0 \ucd08\uae30\ud654", None))
        self.pushButton_4.setText(QCoreApplication.translate("mz01_main_v2", u"\uc800\uc7a5 \ud3f4\ub354 \uc5f4\uae30", None))
        self.radioButton_3.setText(QCoreApplication.translate("mz01_main_v2", u"\ubaa8\uc790\uc774\ud06c", None))
        self.radioButton_4.setText(QCoreApplication.translate("mz01_main_v2", u"\ube14\ub7ec", None))
        self.label_4.setText(QCoreApplication.translate("mz01_main_v2", u"\ud6a8\uacfc", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mz01_main_v2", u"0%", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mz01_main_v2", u"10%", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mz01_main_v2", u"20%", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mz01_main_v2", u"30%", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mz01_main_v2", u"40%", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mz01_main_v2", u"50%", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("mz01_main_v2", u"60%", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("mz01_main_v2", u"70%", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("mz01_main_v2", u"80%", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("mz01_main_v2", u"90%", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("mz01_main_v2", u"100%", None))

        self.label_5.setText(QCoreApplication.translate("mz01_main_v2", u"\uac15\ub3c4", None))
        self.pushButton.setText(QCoreApplication.translate("mz01_main_v2", u"\uc2dc\uc791\ud558\uae30", None))
        self.label_2.setText(QCoreApplication.translate("mz01_main_v2", u"\uc800\uc7a5\uc704\uce58 : ", None))
        self.pushButton_5.setText(QCoreApplication.translate("mz01_main_v2", u"X", None))
    # retranslateUi

