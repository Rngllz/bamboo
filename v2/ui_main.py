# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bamboo_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1211, 612)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(200, 0))
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgba(32, 33, 36, 1);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 90))
        self.frame_2.setStyleSheet(u"background-color: rgba(32, 33, 36, 1);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 20, 0, 10)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 90))

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 36, 1);\n"
"}\n"
"	\n"
"QPushButton:hover{\n"
"	background-color: rgb(72, 74, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(32, 33, 36, 1);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: rgba(39, 40, 43, 1);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.frame_head = QFrame(self.frame_main)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setMaximumSize(QSize(16777215, 58))
        self.frame_head.setStyleSheet(u"background-color: rgba(39, 40, 43, 1);")
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_head)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 0, 5)
        self.label_3 = QLabel(self.frame_head)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_head)

        self.frame_middle = QFrame(self.frame_main)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setStyleSheet(u"background-color: rgba(45, 46, 50, 1);")
        self.frame_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_middle)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.page_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgba(45, 46, 50, 1);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(45, 46, 50, 1);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_home)
        self.page_manipula = QWidget()
        self.page_manipula.setObjectName(u"page_manipula")
        self.stackedWidget.addWidget(self.page_manipula)
        self.page_visualiza = QWidget()
        self.page_visualiza.setObjectName(u"page_visualiza")
        self.stackedWidget.addWidget(self.page_visualiza)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_middle)

        self.frame_footer = QFrame(self.frame_main)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMaximumSize(QSize(16777215, 40))
        self.frame_footer.setStyleSheet(u"background-color: rgba(39, 40, 43, 1);")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.pushButton = QPushButton(self.frame_footer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 60))
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(39, 40, 43, 1);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons_bamboo/cardapio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label_data = QLabel(self.frame_footer)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_data)


        self.verticalLayout.addWidget(self.frame_footer)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons_bamboo/logo_branca_64.png\"/></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Manipula\u00e7\u00e3o", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Visualiza\u00e7\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">sistema bamboo</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><img src=\":/icons/icons_bamboo/logo_branca_512.ico\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Welcome user</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">Bamboo</span></p><p><span style=\" font-size:36pt;\">Data cleaning</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">20/02/2025</p></body></html>", None))
    # retranslateUi

