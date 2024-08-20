# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mz01_main_v3_grid.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1226, 839)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color:rgb(0,0,0);\n"
"	border:3px;\n"
"    border-radius: 20px;\n"
"	border-color:rgb(0,0,0);\n"
"	Border-Style:solid;\n"
"	background-repeat: no-repeat\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(30, 30))
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

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 10, 30, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(950, 350))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515 ExtraBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
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

        self.verticalLayout_3.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setFont(font)
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

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 30))
        self.label_2.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"\ub098\ub214\uace0\ub515\ucf54\ub529"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"#label_2\n"
"{\n"
"	background-color:rgb(80,80,80);\n"
"	color:rgb(255,255,255);\n"
"    height: 30px;\n"
"	border-radius: 15;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 0))
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(400, 100))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
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
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(150, 0))
        self.radioButton_3.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"\ub098\ub214\uace0\ub515\ucf54\ub529"])
        font2.setPointSize(12)
        self.radioButton_3.setFont(font2)
        self.radioButton_3.setStyleSheet(u"#radioButton_3\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.radioButton_3.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_3, 0, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(150, 0))
        self.radioButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_4.setFont(font2)
        self.radioButton_4.setStyleSheet(u"#radioButton_4\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 30))
        self.label_3.setMaximumSize(QSize(100, 30))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"#label_3\n"
"{\n"
"	background-color:rgb(80,80,80);\n"
"	color:rgb(255,255,255);\n"
"    height: 30px;\n"
"	border-radius: 15;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))
        self.label_6.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(150, 0))
        self.checkBox.setMaximumSize(QSize(250, 16777215))
        self.checkBox.setFont(font2)
        self.checkBox.setFocusPolicy(Qt.WheelFocus)
        self.checkBox.setStyleSheet(u"#checkBox\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(150, 0))
        self.checkBox_2.setMaximumSize(QSize(250, 16777215))
        self.checkBox_2.setFont(font2)
        self.checkBox_2.setStyleSheet(u"#checkBox_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(150, 0))
        self.checkBox_4.setMaximumSize(QSize(250, 16777215))
        self.checkBox_4.setFont(font2)
        self.checkBox_4.setStyleSheet(u"#checkBox_4\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 30))
        self.label_5.setMaximumSize(QSize(300, 16777215))
        self.label_5.setFont(font1)
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

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
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

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_11)

        self.comboBox = QComboBox(self.centralwidget)
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
        self.comboBox.setMinimumSize(QSize(81, 21))
        self.comboBox.setFont(font1)
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

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(700, 50))
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setStyleSheet(u"#label_4\n"
"\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(270, 60))
        self.pushButton_3.setMaximumSize(QSize(270, 16777215))
        font3 = QFont()
        font3.setFamilies([u"\ub098\ub214\uace0\ub515 ExtraBold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.pushButton_3.setFont(font3)
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

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(270, 60))
        self.pushButton.setMaximumSize(QSize(270, 16777215))
        self.pushButton.setFont(font3)
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

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(270, 60))
        self.pushButton_4.setMaximumSize(QSize(270, 16777215))
        self.pushButton_4.setFont(font3)
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

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_10)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(950, 20))
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1226, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText("")
        self.pushButton_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uc744 \ub4dc\ub798\uadf8\ud574\uc11c \ub123\uc5b4\uc8fc\uc138\uc694.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+  \ud30c\uc77c \uc120\ud0dd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud6a8\uacfc", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\uc790\uc774\ud06c", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\ube14\ub7ec", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc801\uc6a9\ubc94\uc704", None))
        self.label_6.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\ub78c", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\uc5bc\uad74", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\ubc88\ud638\ud310", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uac15\ub3c4", None))
        self.label_8.setText("")
        self.label_11.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0%", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"10%", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"20%", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"30%", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"40%", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"50%", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"60%", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"70%", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"80%", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"90%", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"100%", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"    \uc800\uc7a5\uc704\uce58 : ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ucd08\uae30\ud654", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\ud558\uae30", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354 \uc5f4\uae30", None))
        self.label_10.setText("")
    # retranslateUi

