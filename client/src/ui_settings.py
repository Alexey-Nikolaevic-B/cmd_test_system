from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal



class SettingsScreen(QDialog):

    signal_goto_login   = pyqtSignal()
    signal_goto_lessons = pyqtSignal()

    def __init__(self):
        super(SettingsScreen, self).__init__()
        self.init_ui()

        # self.btn_apply.clicked.connect(self.gotoLobbyScreen)
        self.btn_offline_menu.clicked.connect(self.gotoLessonsScreen)
        self.btn_online_menu.clicked.connect(self.gotoLoginScreen)

    
    def gotoLoginScreen(self):
        self.signal_goto_login.emit()
    
    def gotoLessonsScreen(self):
        self.signal_goto_lessons.emit()


    def init_ui(self):
        loadUi('C:\dev\cmd_test_system\client\qt\Settings.ui', self)
        style = "QPushButton { color: rgb(255, 255, 255); font: 75 14pt \"Consolas\"; } QPushButton::hover { color: rgb(0, 0, 0); background-color : rgb(200, 200, 200)}"
        self.setStyleSheet("background-color: rgb(255, 117, 117);")
        self.btn_offline_menu.setStyleSheet(style)
        self.btn_online_menu.setStyleSheet(style)
        self.btn_settings.setStyleSheet(style)
        self.btn_apply.setStyleSheet(style)