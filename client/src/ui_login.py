from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal



class LoginScreen(QDialog):

    signal_goto_lessons = pyqtSignal()
    signal_goto_lobby = pyqtSignal(list)

    def __init__(self):
        super(LoginScreen, self).__init__()
        self.init_ui()
        self.is_connected = False
        self.user_data = ['', '']

        self.btn_offline_test.clicked.connect(self.gotoLessonsScreen)
        self.btn_start_test.clicked.connect(self.gotoLobbyScreen)

    def server_is_on(self):
        self.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.is_connected = True
        
    def gotoLessonsScreen(self):
        self.signal_goto_lessons.emit()

    def gotoLobbyScreen(self):
        self.user_data[0] = self.lbl_vzvod_num.text()
        self.user_data[1] = self.lbl_student_name.text()
        if (len(self.user_data[0]) == 0 or len(self.user_data[1]) == 0):
            self.lbl_error.setText("Введите данные")
        elif self.is_connected:
            self.signal_goto_lobby.emit(self.user_data)

    def init_ui(self):
        loadUi('C:/dev/new/client/qt/Login.ui', self)
        style = "QPushButton { font: 75 14pt \"MS Shll Dlg 2\"; } QPushButton::hover { background-color : rgb(197, 255, 149)}"
        self.setStyleSheet("background-color: rgb(255, 117, 117);")
        self.btn_offline_test.setStyleSheet(style)
        self.btn_start_test.setStyleSheet(style)