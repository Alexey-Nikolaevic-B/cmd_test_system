from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
import re
import threading
import time

class TestScreen(QDialog):

    signal_update_status = pyqtSignal(str)
    signal_goto_result   = pyqtSignal(int)

    def __init__(self):
        super(TestScreen, self).__init__()

        self.cur_task = 0
        self.correct = 0
        self.c = 300
        self.tasks = ['Создай файл file1.txt на рабочем столе', 'Создай папку TestDir на рабочем столе', 'Переименуй файл file1.txt в myfile.txt']
        self.checks = ['1', 'mkdir TestDir', 'Переименуй файл file1.txt в myfile.txt'] ##echo file1.txt
        self.mark = [1, 2, 3]
        self.correct = [0]*len(self.tasks)
        self.answers = ['']*len(self.tasks)
        
        self.init_ui()
        self.thread_counter = threading.Thread(target=self.counter, daemon=True)
        self.thread_counter.start()

        self.ln_cmd.returnPressed.connect(self.check)

        self.btn_backward.clicked.connect(lambda: self.update(0))
        self.btn_forward.clicked.connect(lambda: self.update(1))
        self.btn_end_test.clicked.connect(self.gotoResultScreen)

    def check(self):
        pattern = re.compile(self.checks[self.cur_task])
        comand = self.ln_cmd.text()
        if pattern.match(comand):
            self.ln_cmd.setStyleSheet("color: rgb(0, 0, 0); font:16pt \"Consolas\"; background-color: rgb(85, 255, 127);")
            self.correct[self.cur_task] = 1
            self.answers[self.cur_task] = comand
    
    def counter(self):
        while self.c >= 0:
            mins, secs = divmod(self.c, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 

            self.c = self.c - 1
            self.lbl_time.setText(str(timer))

            time.sleep(1)
        
        self.gotoResultScreen()

    def update(self, option):
        self.ln_cmd.setStyleSheet("color: rgb(255, 255, 255); font:16pt \"Consolas\"; background-color: rgb(31, 31, 31);")
        if (option == 0) and (self.cur_task > 0): 
            self.cur_task = self.cur_task - 1
        if (option == 1) and (self.cur_task < len(self.tasks)-1):
            self.cur_task = self.cur_task + 1

        self.btn_backward.setEnabled(True)
        self.btn_forward.setEnabled(True)
        self.btn_end_test.hide()
        if (self.cur_task < 1):
            self.btn_backward.setEnabled(False)
        if (self.cur_task == len(self.tasks)-1):
            self.btn_forward.setEnabled(False)
            self.btn_end_test.show()

        self.lbl_task_num.setText("Задание " + str(self.cur_task + 1))
        self.lbl_task.setText(self.tasks[self.cur_task])
        self.ln_cmd.setText('')

        self.signal_update_status.emit(str(self.cur_task) + ' ' + str(self.correct))

    def gotoResultScreen(self):
        mark = self.correct.count(1)
        self.signal_goto_result.emit(self.correct)
        print(mark)

    def set_tasks(self, tasks, checks, c, mark):
        self.tasks  = tasks
        self.checks = checks    
        self.c      = c 
        self.mark   = mark

    def init_ui(self):
        loadUi('C:\dev\cmd_test_system\client\qt\Test.ui', self)
        
        self.btn_backward.setIcon(QtGui.QIcon('C:\dev\cmd_test_system\img/btn_backward.png'))
        self.btn_forward.setIcon(QtGui.QIcon('C:\dev\cmd_test_system\img/btn_forward.png'))
        self.btn_backward.setIconSize(QtCore.QSize(100,40))
        self.btn_forward.setIconSize(QtCore.QSize(100,40))
        style = "QPushButton { font:16pt \"Consolas\"; } QPushButton::hover { background-color : rgb(200, 200, 200)}"
        self.btn_backward.setStyleSheet(style) 
        self.btn_forward.setStyleSheet(style) 
        self.btn_end_test.setStyleSheet(style) 
                             

        self.lbl_task.setText(self.tasks[self.cur_task])

        self.btn_backward.setEnabled(False)
        self.btn_end_test.hide()
