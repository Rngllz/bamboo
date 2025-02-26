# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bamboo_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 626)
        MainWindow.setStyleSheet(u"background-color: rgb(39, 40, 43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(0, 0))
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setAutoFillBackground(False)
        self.left_container.setStyleSheet(u"background-color: 	rgb(32, 33, 36);")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(36, 37, 40);\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:hover{\n"
"	background-color: rgb(72, 74, 79);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        font1 = QFont()
        font1.setPointSize(9)
        self.toolBox.setFont(font1)
        self.toolBox.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(72, 74, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(41, 42, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 86, 454))
        self.page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setSizeIncrement(QSize(0, 0))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setSizeIncrement(QSize(0, 0))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setSizeIncrement(QSize(0, 0))
        self.btn_contatos.setFont(font1)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 78, 454))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setAutoFillBackground(False)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.head_frame = QFrame(self.main_container)
        self.head_frame.setObjectName(u"head_frame")
        self.head_frame.setFrameShape(QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.head_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.head_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))
        self.pushButton_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.label = QLabel(self.head_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.head_frame)

        self.main_frane = QFrame(self.main_container)
        self.main_frane.setObjectName(u"main_frane")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frane.sizePolicy().hasHeightForWidth())
        self.main_frane.setSizePolicy(sizePolicy)
        self.main_frane.setStyleSheet(u"background-color: rgb(45, 46, 50);")
        self.main_frane.setFrameShape(QFrame.StyledPanel)
        self.main_frane.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frane)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages = QStackedWidget(self.main_frane)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_7.addWidget(self.logo)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.verticalLayout_11 = QVBoxLayout(self.tab_cadastro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Empresas = QLabel(self.tab_cadastro)
        self.Empresas.setObjectName(u"Empresas")
        self.Empresas.setMaximumSize(QSize(16777215, 60))
        self.Empresas.setStyleSheet(u"color: rgb(0, 99, 148);")

        self.verticalLayout_11.addWidget(self.Empresas)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.frame_4 = QFrame(self.tab_cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255,255,255);\n"
"	font: 10pt \"Ms Shell Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(20, 0, 20, 20)
        self.lineEdit_CNPJ = QLineEdit(self.frame_4)
        self.lineEdit_CNPJ.setObjectName(u"lineEdit_CNPJ")
        self.lineEdit_CNPJ.setMinimumSize(QSize(0, 40))
        self.lineEdit_CNPJ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_CNPJ, 1, 0, 1, 1)

        self.lineEdit_Logradouro = QLineEdit(self.frame_4)
        self.lineEdit_Logradouro.setObjectName(u"lineEdit_Logradouro")
        self.lineEdit_Logradouro.setMinimumSize(QSize(0, 40))
        self.lineEdit_Logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Logradouro, 2, 0, 1, 4)

        self.lineEdit_uf = QLineEdit(self.frame_4)
        self.lineEdit_uf.setObjectName(u"lineEdit_uf")
        self.lineEdit_uf.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_uf, 4, 1, 1, 2)

        self.lineEdit_CEP = QLineEdit(self.frame_4)
        self.lineEdit_CEP.setObjectName(u"lineEdit_CEP")
        self.lineEdit_CEP.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_CEP, 4, 3, 1, 1)

        self.lineEdit_Municpio = QLineEdit(self.frame_4)
        self.lineEdit_Municpio.setObjectName(u"lineEdit_Municpio")
        self.lineEdit_Municpio.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Municpio, 4, 0, 1, 1)

        self.lineEdit_Numero = QLineEdit(self.frame_4)
        self.lineEdit_Numero.setObjectName(u"lineEdit_Numero")
        self.lineEdit_Numero.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Numero, 3, 0, 1, 1)

        self.lineEdit_Bairro = QLineEdit(self.frame_4)
        self.lineEdit_Bairro.setObjectName(u"lineEdit_Bairro")
        self.lineEdit_Bairro.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Bairro, 3, 3, 1, 1)

        self.lineEdit_nomeEmpresarial = QLineEdit(self.frame_4)
        self.lineEdit_nomeEmpresarial.setObjectName(u"lineEdit_nomeEmpresarial")
        self.lineEdit_nomeEmpresarial.setMinimumSize(QSize(0, 40))
        self.lineEdit_nomeEmpresarial.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_nomeEmpresarial, 1, 1, 1, 3)

        self.lineEdit_Email = QLineEdit(self.frame_4)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Email, 7, 1, 1, 3)

        self.lineEdit_Telefone = QLineEdit(self.frame_4)
        self.lineEdit_Telefone.setObjectName(u"lineEdit_Telefone")
        self.lineEdit_Telefone.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Telefone, 7, 0, 1, 1)

        self.lineEdit_Complemento = QLineEdit(self.frame_4)
        self.lineEdit_Complemento.setObjectName(u"lineEdit_Complemento")
        self.lineEdit_Complemento.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_Complemento, 3, 1, 1, 2)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.pushButton = QPushButton(self.tab_cadastro)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 30))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_cadastro, "")
        self.tab_empresas = QWidget()
        self.tab_empresas.setObjectName(u"tab_empresas")
        self.verticalLayout_10 = QVBoxLayout(self.tab_empresas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.tab_empresas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 60))
        self.label_5.setStyleSheet(u"color: rgb(0, 99, 148);")

        self.verticalLayout_10.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.tab_empresas)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 9):
            self.tableWidget.setRowCount(9)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_empresas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_gerarExcel = QPushButton(self.frame_3)
        self.btn_gerarExcel.setObjectName(u"btn_gerarExcel")
        self.btn_gerarExcel.setMinimumSize(QSize(80, 40))

        self.verticalLayout_9.addWidget(self.btn_gerarExcel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(80, 40))

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(80, 40))

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_empresas, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_9)

        self.pages.addWidget(self.pg_sobre)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frane)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pytax", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Sistema bamboo</p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Bamboo System</span></p></body></html>", None))
        self.Empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">EMPRESAS</span></p></body></html>", None))
        self.lineEdit_CNPJ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_Logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"logradouro", None))
        self.lineEdit_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"uf", None))
        self.lineEdit_CEP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_Municpio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.lineEdit_Numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.lineEdit_Bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lineEdit_nomeEmpresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.lineEdit_Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_Telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEdit_Complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">TABELA</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cnpj", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.btn_gerarExcel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">47 99601-7187</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sobre</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"""<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Página Inicial Simples</title><style>body {font-family: Arial, sans-serif; margin: 0; padding: 0; text-align: center;}header {background-color: #4CAF50; color: white; padding: 1em;}section {margin: 2em;}footer {background-color: #f1f1f1; padding: 1em; position: fixed; width: 100%; bottom: 0;}</style></head><body><header><h1>Bem-vindo à Minha Página</h1></header><section><p>Esta é uma página inicial simples criada em uma única linha de código Python.</p></section><footer><p>&copy; 2025 Meu Site</p></footer></body></html>""", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">11:41 20/02/2025</p></body></html>", None))
    # retranslateUi

