# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 640)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(207, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.rb_audio = QRadioButton(self.frame_2)
        self.rb_audio.setObjectName(u"rb_audio")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.rb_audio.setFont(font1)
        self.rb_audio.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.rb_audio)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.rb_video = QRadioButton(self.frame_2)
        self.rb_video.setObjectName(u"rb_video")
        self.rb_video.setFont(font1)
        self.rb_video.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.rb_video)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.rb_playlist = QRadioButton(self.frame_2)
        self.rb_playlist.setObjectName(u"rb_playlist")
        self.rb_playlist.setFont(font1)
        self.rb_playlist.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.rb_playlist)

        self.horizontalSpacer_6 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(223, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.txt_link = QLineEdit(self.frame)
        self.txt_link.setObjectName(u"txt_link")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.txt_link.setFont(font2)
        self.txt_link.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_link)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.btn_donwload = QPushButton(self.frame)
        self.btn_donwload.setObjectName(u"btn_donwload")
        self.btn_donwload.setMinimumSize(QSize(0, 35))
        self.btn_donwload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_donwload.setStyleSheet(u"QPushButton{background-color:#fff; color:black; border: solid 0px; font: 75 16px; border-radius:7px; margin-left:100px; margin-right:100px} \n"
"QPushButton:hover{background-color:rgb(227, 24, 54); color:#fff}")

        self.verticalLayout_3.addWidget(self.btn_donwload)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(207, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_file = QLineEdit(self.tab_2)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setPointSize(10)
        self.txt_file.setFont(font3)
        self.txt_file.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tab_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(100, 35))
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{background-color:#fff; color:black; border: solid 0px; font: 75 16px; border-radius:7px} \n"
"QPushButton:hover{background-color:rgb(227, 24, 54); color:#fff}")

        self.horizontalLayout_4.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.txt_seg_inicial = QLineEdit(self.tab_2)
        self.txt_seg_inicial.setObjectName(u"txt_seg_inicial")
        self.txt_seg_inicial.setFont(font3)
        self.txt_seg_inicial.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_seg_inicial.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.txt_seg_inicial)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.txt_seg_final = QLineEdit(self.tab_2)
        self.txt_seg_final.setObjectName(u"txt_seg_final")
        self.txt_seg_final.setFont(font3)
        self.txt_seg_final.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_seg_final.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.txt_seg_final)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.btn_corvert = QPushButton(self.tab_2)
        self.btn_corvert.setObjectName(u"btn_corvert")
        self.btn_corvert.setMinimumSize(QSize(0, 35))
        self.btn_corvert.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_corvert.setStyleSheet(u"QPushButton{background-color:#fff; color:black; border: solid 0px; font: 75 16px; border-radius:7px; margin-left:100px; margin-right:100px} \n"
"QPushButton:hover{background-color:rgb(227, 24, 54); color:#fff}")

        self.verticalLayout_7.addWidget(self.btn_corvert)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TUBE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"YOUTUBER DONWLOADER", None))
        self.rb_audio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.rb_video.setText(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
        self.rb_playlist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cole o link do v\u00eddeo na caixa abaixo", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link para do v\u00eddeo para download", None))
        self.btn_donwload.setText(QCoreApplication.translate("MainWindow", u"BAIXAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TUBE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CORTAR PARTES DO V\u00cdDEO", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"selecione o v\u00eddeo", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"tempo inicial", None))
        self.txt_seg_inicial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"segundo inicial", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"tempo final", None))
        self.txt_seg_final.setPlaceholderText(QCoreApplication.translate("MainWindow", u"segundo final", None))
        self.btn_corvert.setText(QCoreApplication.translate("MainWindow", u"CONVERTER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

