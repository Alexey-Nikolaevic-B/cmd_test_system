from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal

class MainScreen(QDialog):

    signal_toggle_test = pyqtSignal(str)

    def __init__(self):
        super(MainScreen, self).__init__()
        self.init_ui()

        self.number_of_tasks = 10
        self.test_settings = ''

        self.btn_start_test.clicked.connect(self.launch_test)
        self.btn_save_settings.clicked.connect(self.save_settings)

    def save_settings(self):    
        self.test_settings = self.time.text()
        print(self.test_settings)


    def launch_test(self):
        self.btn_start_test.setText('Закончить тест')
        self.signal_toggle_test.emit(str(self.test_settings)) #data
        print(self.test_settings)

    def update_users(self, id, name, current, correct):

        current = round(100 / self.number_of_tasks * current)
        correct = round(100 / self.number_of_tasks * correct)

        if id == '1':
            self.lbl_name.setText(name)
            self.pb_completed.setValue(correct)
            self.pb_current.setValue(current)
            self.person.show()
        if id == '2':
            self.lbl_name_2.setText(name)
            self.pb_completed_2.setValue(correct)
            self.pb_current_2.setValue(current)
            self.person_2.show()
        if id == '3':
            self.lbl_name_3.setText(name)
            self.pb_completed_3.setValue(correct)
            self.pb_current_3.setValue(current)
            self.person_3.show()

    def set_name(self, data):
        self.label.setText(data)
        self.person.show()

    def init_ui(self):
        loadUi('C:\dev\cmd_test_system\server\qt\Main.ui', self)
        self.person.hide()
        self.person_2.hide()
        self.person_3.hide()
        self.person_4.hide()
        self.person_5.hide()
        self.person_6.hide()
        self.person_7.hide()
        self.person_8.hide()
        self.person_9.hide()
        self.person_10.hide()
        self.person_11.hide()
        self.person_12.hide()