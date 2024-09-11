from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore

class TestScreen(QDialog):

    signal_update_status = pyqtSignal(str)

    def __init__(self):
        super(TestScreen, self).__init__()
        self.init_ui()

        self.cur_task = 0
        self.correct = 0
        
        self.btn_backward.clicked.connect(lambda: self.update(0))
        self.btn_forward.clicked.connect(lambda: self.update(1))

    def update(self, option):
        if (option == 0) and (self.cur_task > 0): 
            self.cur_task = self.cur_task - 1
        if (option == 1) and (self.cur_task < 10): ################
            self.cur_task = self.cur_task + 1

        self.btn_backward.setEnabled(True)
        self.btn_forward.setEnabled(True)
        self.btn_end_test.hide()
        if (self.cur_task < 1):
            self.btn_backward.setEnabled(False)
        if (self.cur_task == 10):                   ################
            self.btn_forward.setEnabled(False)
            self.btn_end_test.show()

        self.lbl_task_num.setText("Задание " + str(self.cur_task + 1))

        self.signal_update_status.emit(str(self.cur_task) + ' ' + str(self.correct))
        # self.lbl_task.setText("\t" + str(self.appData.task[self.cur_task]))

    def init_ui(self):
        loadUi('C:\dev/new\client\qt\Test.ui', self)
        
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
