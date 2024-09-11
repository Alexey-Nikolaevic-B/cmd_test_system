import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

import socket as socket
import threading
import connection

import ui_main

class QT_Controler(QObject):

    signal_data_recived     = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self.main   = ui_main.MainScreen()
        self.worker = connection.SocketWorker()
        self.widget = QtWidgets.QStackedWidget()
        
        self.test_is_started = False
        self.users = []

        self.signals()
        self.run()
        

    def run(self):
        self.checker = threading.Thread(target=self.worker.process, daemon=True)
        self.checker.start()
        
        self.widget.addWidget(self.main)
        self.widget.show()
        # self.widget.showFullScreen()


    def signals(self):
        self.worker.signal_data_recived.connect(self.process_recived_data)

        self.main.signal_toggle_test.connect(self.toggle_test)

    def toggle_test(self):
        if not self.test_is_started:    
            message = "start tasks:"
            self.worker.send_message(message)
            self.test_is_started = True
        else:
            message = "end filler:"
            self.worker.send_message(message)

    def process_recived_data(self, data):
        self.student_name = data
        self.signal_data_recived.emit(self.student_name)

        pattern_name = re.compile('(\d+) (\w+) (.+)')
        grouped_data = pattern_name.search(data)
        user_id = grouped_data.group(1)
        key = grouped_data.group(2)
        info = grouped_data.group(3)

        if key == 'name':
            self.users.append(info)
            self.main.update_users(user_id, info, 0 , 0)
            #print("UPDATE NAME ", self.users)

        if key == 'status':
            pattern_info = re.compile('(\d+) (\d+)')
            grouped_info = pattern_info.search(info)

            current = grouped_info.group(1)
            correct = grouped_info.group(2)
            # print("correct {" + correct + "}")
            # print("correct {" + current + "}")

            self.main.update_users(user_id, self.users[int(user_id)-1], int(current), int(correct))
            #print("UPDATE STATUS ", user_id + ' ' + info)

        if key == 'finished':
            pass




        