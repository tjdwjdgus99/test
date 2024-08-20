# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mz01_main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_mz01_main(object):
    def setupUi(self, mz01_main):
        if not mz01_main.objectName():
            mz01_main.setObjectName(u"mz01_main")
        mz01_main.resize(1024, 768)
        mz01_main.setAcceptDrops(False)
        mz01_main.setStyleSheet(u"#mz01_main\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"}")
        self.centralwidget = QWidget(mz01_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1031, 731))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1028, 300))
        self.label.setMaximumSize(QSize(1028, 500))
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet(u"#label\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"#label_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 150))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 170, 90, 16))
        self.radioButton.setStyleSheet(u"#radioButton\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(110, 170, 90, 16))
        self.radioButton_2.setStyleSheet(u"#radioButton_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.groupBox)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"#label_3\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.label_3)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(80, 16777215))
        self.checkBox.setStyleSheet(u"#checkBox\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(80, 16777215))
        self.checkBox_2.setStyleSheet(u"#checkBox_2\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMaximumSize(QSize(80, 16777215))
        self.checkBox_4.setStyleSheet(u"#checkBox_4\n"
"{\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        mz01_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mz01_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        mz01_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mz01_main)
        self.statusbar.setObjectName(u"statusbar")
        mz01_main.setStatusBar(self.statusbar)

        self.retranslateUi(mz01_main)

        QMetaObject.connectSlotsByName(mz01_main)
    # setupUi

    def retranslateUi(self, mz01_main):
        mz01_main.setWindowTitle(QCoreApplication.translate("mz01_main", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("mz01_main", u"\uc774\ubbf8\uc9c0\ub97c \ub4dc\ub798\uadf8\ud574\uc11c \ub123\uc5b4\uc8fc\uc138\uc694.", None))
        self.label_2.setText(QCoreApplication.translate("mz01_main", u"\uc720\ud615", None))
        self.groupBox.setStyleSheet(QCoreApplication.translate("mz01_main", u"0", None))
        self.groupBox.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("mz01_main", u"\uc601\uc0c1", None))
        self.radioButton_2.setText(QCoreApplication.translate("mz01_main", u"\uc774\ubbf8\uc9c0", None))
        self.label_3.setText(QCoreApplication.translate("mz01_main", u"\uc801\uc6a9\ubc94\uc704", None))
        self.checkBox.setText(QCoreApplication.translate("mz01_main", u"\uc0ac\ub78c", None))
        self.checkBox_2.setText(QCoreApplication.translate("mz01_main", u"\uc5bc\uad74", None))
        self.checkBox_4.setText(QCoreApplication.translate("mz01_main", u"\ubc88\ud638\ud310", None))
    # retranslateUi

