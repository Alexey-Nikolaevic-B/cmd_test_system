from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

class LessonsScreen(QDialog):

    signal_goto_login    = pyqtSignal()
    signal_goto_settings = pyqtSignal()

    def __init__(self):
        super(LessonsScreen, self).__init__()
        self.init_ui()

        self.btn_online_menu.clicked.connect(self.gotoLoginScreen)
        self.btn_settings.clicked.connect(self.gotoSettingsScreen)

    
    def gotoLoginScreen(self):
        self.signal_goto_login.emit()
    
    def gotoSettingsScreen(self):
        self.signal_goto_settings.emit()


    def init_ui(self):
        loadUi('C:\dev\cmd_test_system\client\qt\Lessons.ui', self)
        style = "QPushButton { color: rgb(255, 255, 255); font: 75 14pt \"Consolas\"; } QPushButton::hover { color: rgb(0, 0, 0); background-color : rgb(200, 200, 200)}"
        self.setStyleSheet("background-color: rgb(255, 117, 117);")
        self.btn_offline_menu.setStyleSheet(style)
        self.btn_online_menu.setStyleSheet(style)
        self.btn_settings.setStyleSheet(style)