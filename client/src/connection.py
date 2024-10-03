from PyQt5.QtCore import QObject, pyqtSignal
import socket
import time
import json

host = '172.18.4.48'
port = 2620

class SocketWorker(QObject):

    signal_server_on = pyqtSignal(bool)
    signal_data_recived = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self.socket = socket.socket()
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = 'empty'
        self.stop_check = False
        self.receivedJson = {}
        self.test_started = False
        # self.socket.bind((socket.gethostname(), 1234))
        

    def check_server(self):
        while True:
            if self.stop_check:
                break
            self.socket = socket.socket()
            result = self.socket.connect_ex((socket.gethostname(), 1234))
            # self.socket.close()
            if result:
                #print('problem with socket!')
                status = 0
            else:
                #print('everything is ok!')
                status = 1
                self.stop_check = True
            self.signal_server_on.emit(status)
            # time.sleep(0.1)  


    def message_exchange(self):
        data = 'empty'
        self.socket.send(data.encode('utf-8'))
        while True:

            # print('sending msg'
            # print("sending", self.data)
            # self.data = 'empty'


            # print('catching msg')
            # data = self.socket.recv(2048).decode('utf-8')
            # if (data != 'empty') and (data is not None):
            #     print(data)
            #     self.signal_data_recived.emit(data)
            try:
                # print('sending msg')
                self.socket.send(self.data.encode('utf-8'))
                # print("sending", self.data)
                self.data = 'empty'
            except:
                pass
            
            try:
                # print('catching msg')
                data = self.socket.recv(2048).decode('utf-8')
                if (data != 'empty') or (data is not None):
                    # print('catched' + data)
                    self.signal_data_recived.emit(data)
            except:
                pass
            time.sleep(0.5) 
        
    def send_message(self, data):
        self.data = data