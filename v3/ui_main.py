# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bamboo_v3.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1144, 773)
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
        self.frame_menu.setMinimumSize(QSize(0, 0))
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
        self.frame.setMinimumSize(QSize(200, 0))
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
        self.pushButton_home = QPushButton(self.frame)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.pushButton_home)

        self.pushButton_manipula = QPushButton(self.frame)
        self.pushButton_manipula.setObjectName(u"pushButton_manipula")
        self.pushButton_manipula.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.pushButton_manipula)

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
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
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
        self.label_4.setMaximumSize(QSize(16777215, 65))
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 80))
        self.label_6.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_6.addWidget(self.label_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_home)
        self.page_manipula = QWidget()
        self.page_manipula.setObjectName(u"page_manipula")
        self.verticalLayout_7 = QVBoxLayout(self.page_manipula)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.page_manipula)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.tab_tabela = QWidget()
        self.tab_tabela.setObjectName(u"tab_tabela")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_tabela)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.tab_tabela)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(500, 0))
        self.frame_7.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 11, -1)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tableWidget = QTableWidget(self.frame_10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(225, 225, 225);")
        self.tableWidget.setAlternatingRowColors(True)

        self.verticalLayout_10.addWidget(self.tableWidget)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 80))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_input = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")
        self.plainTextEdit_input.setMinimumSize(QSize(0, 80))
        self.plainTextEdit_input.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit_input.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(4, 255, 0);")

        self.horizontalLayout_8.addWidget(self.plainTextEdit_input)

        self.pushButton_run = QPushButton(self.frame_9)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setMinimumSize(QSize(20, 0))
        self.pushButton_run.setMaximumSize(QSize(16777215, 80))
        self.pushButton_run.setStyleSheet(u"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(138, 138, 138);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(197, 197, 197);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_run)

        self.plainTextEdit_output = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_output.setObjectName(u"plainTextEdit_output")
        self.plainTextEdit_output.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_output.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit_output.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(4, 255, 0);")

        self.horizontalLayout_8.addWidget(self.plainTextEdit_output)


        self.verticalLayout_11.addWidget(self.frame_9)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.tab_tabela)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(120, 0))
        self.frame_8.setMaximumSize(QSize(120, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(60, 30))
        self.frame_12.setMaximumSize(QSize(100, 30))
        self.frame_12.setStyleSheet(u"background-color: rgb(32, 255, 29);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_arquivo = QPushButton(self.frame_12)
        self.pushButton_arquivo.setObjectName(u"pushButton_arquivo")
        self.pushButton_arquivo.setMinimumSize(QSize(0, 30))
        self.pushButton_arquivo.setMaximumSize(QSize(16777215, 30))
        self.pushButton_arquivo.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_arquivo.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(138, 138, 138);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(197, 197, 197);\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_arquivo)

        self.plainTextEdit_sep = QPlainTextEdit(self.frame_12)
        self.plainTextEdit_sep.setObjectName(u"plainTextEdit_sep")
        self.plainTextEdit_sep.setMinimumSize(QSize(15, 30))
        self.plainTextEdit_sep.setMaximumSize(QSize(15, 30))
        self.plainTextEdit_sep.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit_sep.setAutoFillBackground(False)
        self.plainTextEdit_sep.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit_sep)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(60, 30))
        self.frame_13.setMaximumSize(QSize(100, 30))
        self.frame_13.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_atualizar = QPushButton(self.frame_13)
        self.pushButton_atualizar.setObjectName(u"pushButton_atualizar")
        self.pushButton_atualizar.setMinimumSize(QSize(75, 30))
        self.pushButton_atualizar.setMaximumSize(QSize(16777215, 30))
        self.pushButton_atualizar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(138, 138, 138);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(197, 197, 197);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_atualizar)

        self.checkBox_atualizar = QCheckBox(self.frame_13)
        self.checkBox_atualizar.setObjectName(u"checkBox_atualizar")
        self.checkBox_atualizar.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_12.addWidget(self.checkBox_atualizar)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tab_tabela, "")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_info)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_11 = QFrame(self.tab_info)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.plainTextEdit_info = QPlainTextEdit(self.frame_11)
        self.plainTextEdit_info.setObjectName(u"plainTextEdit_info")
        self.plainTextEdit_info.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.plainTextEdit_info)


        self.horizontalLayout_9.addWidget(self.frame_11)

        self.tabWidget.addTab(self.tab_info, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_manipula)
        self.page_visualiza = QWidget()
        self.page_visualiza.setObjectName(u"page_visualiza")
        self.verticalLayout_8 = QVBoxLayout(self.page_visualiza)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.page_visualiza)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_6)

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
        self.pushButton.setMinimumSize(QSize(0, 35))
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
        icon.addFile(u"../v1/icons_bamboo/cardapio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons_bamboo/logo_branca_64.png\"/></p></body></html>", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_manipula.setText(QCoreApplication.translate("MainWindow", u"Manipula\u00e7\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">sistema bamboo</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><img src=\":/icons/icons_bamboo/logo_branca_512.ico\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Welcome user</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bamboo</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Data Cleaning System</span></p></body></html>", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.plainTextEdit_output.setPlainText("")
        self.pushButton_arquivo.setText(QCoreApplication.translate("MainWindow", u"ARQUIVO", None))
        self.plainTextEdit_sep.setPlainText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_atualizar.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.checkBox_atualizar.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tabela), QCoreApplication.translate("MainWindow", u"Tabela", None))
        self.plainTextEdit_info.setPlainText(QCoreApplication.translate("MainWindow", u".", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), QCoreApplication.translate("MainWindow", u"info", None))
        self.pushButton.setText("")
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">20/02/2025</p></body></html>", None))
    # retranslateUi

