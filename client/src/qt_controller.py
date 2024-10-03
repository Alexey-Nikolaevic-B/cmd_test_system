import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

import threading
import connection

import ui_lessons
import ui_lobby
import ui_login 
import ui_result
import ui_test
import ui_settings



class QT_Controler(QObject):

    server_on            = pyqtSignal(int)
    signal_goto_lobby    = pyqtSignal(list)
    signal_data_recived  = pyqtSignal(str)
    signal_update_status = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)

        self.widget   = QtWidgets.QStackedWidget()
        self.login    = ui_login.LoginScreen()
        self.settings = ui_settings.SettingsScreen()
        self.lobby    = ui_lobby.LobbyScreen()
        self.lessons  = ui_lessons.LessonsScreen()
        self.test     = ui_test.TestScreen()
        self.result   = ui_result.ResultScreen()

        self.worker  = connection.SocketWorker()

        self.signals()
        self.run()
        
    def run(self):
        self.connection = threading.Thread(target=self.worker.check_server, daemon=True)
        self.connection.start()

        self.widget.addWidget(self.test)
        self.widget.show()
        # self.widget.showFullScreen()

    def signals(self):
        self.worker.signal_server_on.connect(self.set_server_status)
        self.worker.signal_data_recived.connect(self.process_recived_data)        

        self.login.signal_goto_lobby.connect(self.gotoLobbyScreen)
        self.login.signal_goto_lessons.connect(self.gotoLessonsScreen)
        self.login.signal_goto_settings.connect(self.gotoSettingsScreen)

        self.lessons.signal_goto_login.connect(self.gotoLoginScreen)
        self.lessons.signal_goto_settings.connect(self.gotoSettingsScreen)

        self.settings.signal_goto_lessons.connect(self.gotoLessonsScreen)
        self.settings.signal_goto_login.connect(self.gotoLoginScreen)

        self.test.signal_update_status.connect(self.update_status)
        self.test.signal_goto_result.connect(self.gotoReslutScreen)

    
    def update_status(self, data):
        self.student_name = data
        self.signal_update_status.emit(self.student_name)
        self.worker.send_message('status ' + data)
        #print(data)


    def process_recived_data(self, data):
        self.student_name = data
        self.signal_data_recived.emit(self.student_name)

        pattern_name = re.compile('(\w+) (.+)')
        grouped_data = pattern_name.search(data)

        print(data)
        print(grouped_data)
        
        if (grouped_data is not None):
            key = grouped_data.group(1)
            info = grouped_data.group(2)

            print("-> ", key)

            if key == 'start':
                print("--> ", data)
                self.gotoTestScreen()

            if key == 'end':
                self.gotoReslutScreen()


    def set_server_status(self, status):
        self.server_status = status
        self.server_on.emit(self.server_status)
        if self.server_status:
            self.login.server_is_on()


    def gotoLoginScreen(self):
        self.widget.addWidget(self.login)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def gotoLessonsScreen(self):
        self.widget.addWidget(self.lessons)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def gotoSettingsScreen(self):
        self.widget.addWidget(self.settings)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def gotoLobbyScreen(self, name):
        self.student_name = name
        self.signal_goto_lobby.emit(self.student_name)
        #print(self.student_name)

        self.connections = threading.Thread(target=self.worker.message_exchange, daemon=True)
        self.connections.start()
        self.worker.send_message('name ' + str(self.student_name[1]))

        self.widget.addWidget(self.lobby)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)    

    def gotoTestScreen(self):
        self.widget.addWidget(self.test)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def gotoReslutScreen(self):
        self.widget.addWidget(self.result)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)  

    # def countDownTimer(self):
    #     while True:
    #         if self.worker.test_started:
    #             self.test_started = self.worker.test_started
    #             self.startTestClicked.emit(self.test_started)

    #             t = int(self.main_timer.split(":")[0]) * 60
    #             while t and self.worker.test_started:
    #                 mins, secs = divmod(t, 60)
    #                 timer = '{:02d}:{:02d}'.format(mins, secs)
    #                 self.main_timer = timer
    #                 self.mainTimerUpdated.emit(self.main_timer)
    #                 print(timer, end="\r")
    #                 time.sleep(1)
    #                 t -= 1
    #             print('Timer stopped')
    #             break    