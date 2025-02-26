
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sitema Bamboo V-1")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        
        # Toggle Button
        self.pushButton_2.clicked.connect(print("oioi"))
        self.pushButton_2.clicked.connect(self.leftMenu)
        
        # Páginas do sistema
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contatos))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        
        
    def leftMenu(self):
        
        width = self.left_container.width()
        print(width)
        if width == 9:
            newWidth = 200
        elif width > 9:
            newWidth = 9
        print(newWidth)
        
        self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    