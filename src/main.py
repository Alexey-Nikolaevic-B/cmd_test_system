import sys, os
import re

from datetime import datetime

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

import cmd_interface


class AppData():
    vzvod = 0
    name = ""
    mark = 0
    task = []
    check_regex = []
    checks = []
    cur_task = 0


class CMDScreen(QtWidgets):
    appData = AppData()
    input_cmd = ''
    def __init__(self, input: AppData):
        self.appData = input
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        loadUi('C:\dev\cmd_test_system\qt\CMD.ui', self)
        self.setWindowIcon(QtGui.QIcon('C:\dev\cmd_test_system\img\icon_cmd.jpg'))
        self.setWindowTitle('Администратор: Командная строка')

        self.label.setText(os.getcwd() + ">")
        self.lineEdit.returnPressed.connect(self.enter)

    def enter(self):
        self.input_cmd = self.lineEdit.text()
        result = cmd_interface.exec_command(self.input_cmd)
        self.label_2.setText(result)

        self.lineEdit.setText('')
        self.label_4.setText('')    

        check_pattern = re.compile(self.appData.check_regex[self.appData.cur_task])

        if check_pattern.match(self.input_cmd):
            self.appData.checks[self.appData.cur_task] = 1
            self.appData.mark = self.appData.mark + 1
            self.label_4.setText('МОЛОДЕЦ')


class TestScreen(QtWidgets):
    appData = AppData()

    def __init__(self, input: AppData):
        self.appData = input
        self.c = 300
        super(TestScreen, self).__init__()
        loadUi('C:\dev\cmd_test_system\qt\Test.ui', self)

        self.btn_backward.setIcon(QtGui.QIcon('C:\dev\cmd_test_system\img/btn_backward.png'))
        self.btn_forward.setIcon(QtGui.QIcon('C:\dev\cmd_test_system\img/btn_forward.png'))
        self.btn_backward.setIconSize(QtCore.QSize(100,40))
        self.btn_forward.setIconSize(QtCore.QSize(100,40))
        style = "QPushButton { font: 75 14pt \"MS Shell Dlg 2\"; } QPushButton::hover { background-color : rgb(197, 255, 149)}"
        self.btn_backward.setStyleSheet(style) 
        self.btn_forward.setStyleSheet(style) 
        self.btn_end_test.setStyleSheet(style) 
                             

        self.btn_backward.setEnabled(False)
        self.btn_end_test.hide()

        self.cmd = CMDScreen(self.appData)
        self.cmd.show()

        self.lbl_task_num.setText("Задание " + str(self.appData.cur_task + 1))
        self.lbl_task.setText("\t" + str(self.appData.task[self.appData.cur_task]))

        self.btn_end_test.clicked.connect(self.gotoReslutScreen)

        self.btn_backward.clicked.connect(lambda: self.update(0))
        self.btn_forward.clicked.connect(lambda: self.update(1))

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.counter)
        self.timer.start()
        
        self.lbl_time.setText(str(self.c))

    def counter(self):
        mins, secs = divmod(self.c, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        # print(timer, end="\r") 

        self.c = self.c - 1
        self.lbl_time.setText(str(timer))

    def update(self, option):
        if (option == 0) and (self.appData.cur_task > 0): 
            self.appData.cur_task = self.appData.cur_task - 1
        if (option == 1) and (self.appData.cur_task < len(self.appData.task) - 1):
            self.appData.cur_task = self.appData.cur_task + 1

        self.btn_backward.setEnabled(True)
        self.btn_forward.setEnabled(True)
        self.btn_end_test.hide()
        if (self.appData.cur_task < 1):
            self.btn_backward.setEnabled(False)
        if (self.appData.cur_task == len(self.appData.task) - 1):
            self.btn_forward.setEnabled(False)
            self.btn_end_test.show()

        self.lbl_task_num.setText("Задание " + str(self.appData.cur_task + 1))
        self.lbl_task.setText("\t" + str(self.appData.task[self.appData.cur_task]))

        self.cmd.update()

    def approve(self):
        self.setStyleSheet("background-color: rgb(85, 255, 127);")

    def gotoReslutScreen(self):
        self.cmd.close()
        resultScreen = ResultScreen(self.appData)
        widget.addWidget(resultScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LessonsScreen(QtWidgets):
    appData = AppData()

    def __init__(self, input: AppData):
        self.appData = input
        super(LessonsScreen, self).__init__()
        loadUi('C:\dev\cmd_test_system\qt\Lessons.ui', self)

        style = "QPushButton { font: 75 14pt \"MS Shll Dlg 2\"; } QPushButton::hover { background-color : rgb(197, 255, 149)}"
        self.btn_lesson.setStyleSheet(style)
        self.btn_lesson_2.setStyleSheet(style) 
        self.btn_lesson_3.setStyleSheet(style) 
        self.btn_lesson_4.setStyleSheet(style) 

        self.btn_lesson.clicked.connect(self.gotoTestScreen)

    def gotoTestScreen(self):
        self.appData.task =  ["Узнайте имя текущего пользователя c помощью команды", "Получите имя текущей папки с помощью команды", "Узнайте содержание папки", "Пропингуйте гугл", "Создайте папку test",  "Заблокируйте все права доступа для текущего пользователя\n к папке test"]
        data.check_regex = ["[ ]*whoami[ ]*", "[ ]*cd[ ]*", "[ ]*dir[ ]*", "[ ]*ping[ ]+google.com[ ]*", "[]*mkdir[ ]+test", "icacls\s+test\s+\/deny\s+([A-Za-z0-9_]+):\(OI\)\(CI\)F"]
        testScreen = TestScreen(self.appData)
        widget.addWidget(testScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)       
        

class LoginScreen(QtWidgets):
    appData = AppData()

    def __init__(self, input: AppData):
        self.appData = input
        super(LoginScreen, self).__init__()
        loadUi('C:\dev\cmd_test_system\qt\Login.ui', self)

        style = "QPushButton { font: 75 14pt \"MS Shll Dlg 2\"; } QPushButton::hover { background-color : rgb(197, 255, 149)}"
        self.btn_offline_test.setStyleSheet(style)
        self.btn_start_test.setStyleSheet(style)

        self.btn_offline_test.clicked.connect(self.gotoLessonsScreen)
        self.btn_start_test.clicked.connect(self.gotoTestScreen)

    def gotoTestScreen(self):
        data.vzvod_num = self.lbl_vzvod_num.text()
        data.name = self.lbl_student_name.text()
        if (len(data.vzvod_num) == 0 or len(data.name) == 0):
            self.lbl_error.setText("Введите данные")
        # else:
        #     testScreen = TestScreen(self.appData)
        #     widget.addWidget(testScreen)
        #     widget.setCurrentIndex(widget.currentIndex()+1)en

    def gotoLessonsScreen(self):
        lessonsScreen = LessonsScreen(self.appData)
        widget.addWidget(lessonsScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)



class ResultScreen(QtWidgets):
    appData = AppData()
    def __init__(self, input: AppData):
        self.appData = input
        super(ResultScreen, self).__init__()
        loadUi('C:\dev\cmd_test_system\qt\Result.ui', self)

        if self.appData.checks.count(1) > 5:
            self.appData.mark = 5
        elif self.appData.checks.count(1) > 4:
            self.appData.mark = 4
        elif self.appData.checks.count(1) > 3:
            self.appData.mark = 3
        else:
            self.appData.mark = 2    

        self.lbl_result.setText(str(self.appData.mark))
        self.lbl_result1.setText(str(self.appData.checks.count(1)) + " / " + str(len(self.appData.task)))

        if (self.appData.mark == 2):
            self.setStyleSheet("background-color: rgb(255, 117, 117);")
        elif (self.appData.mark == 3):
            self.setStyleSheet("background-color: rgb(255, 184, 96);")
        elif (self.appData.mark == 4):
            self.setStyleSheet("background-color: rgb(243, 255, 135);")
        elif (self.appData.mark == 5):
            self.setStyleSheet("background-color: rgb(85, 255, 127);")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    data = AppData()
    data.task = ["Узнайте имя текущего пользователя c помощью команды", "Получите имя текущей папки с помощью команды", "Узнайте содержание папки", "Пропингуйте гугл", "Создайте папку test",  "Заблокируйте все права доступа для текущего пользователя"]
    data.check_regex = ["[ ]*whoami[ ]*", "[ ]*cd[ ]*", "[ ]*dir[ ]*", "[ ]*ping[ ]+google.com[ ]*"]
    data.checks = [0] * len(data.task)

    loginScreen = LoginScreen(data)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(loginScreen)
    widget.showFullScreen()

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')