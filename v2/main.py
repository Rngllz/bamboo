
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sitema Bamboo V-2")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        
        # Toggle Button
        self.pushButton.clicked.connect(self.leftMenu_animacao)
        
        # Páginas do sistema
        self.pushButton_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.pushButton_manipula.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_manipula))
        self.pushButton_visualiza.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_visualiza))
        
        
    def leftMenu_animacao(self):
        
        width = self.frame_menu.width()
        print(width)
        if width == 0:
            newWidth = 200
        elif width == 200:
            newWidth = 0
        print(newWidth)
        
        self.animation = QPropertyAnimation(self.frame_menu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    app.exec()
    