from PyQt5.QtCore import QObject, pyqtSignal
import socket
from _thread import *
import json
import time


host = '172.18.4.48'
port = 2620
dataPackageSize = 1024



class SocketWorker(QObject):

    signal_data_recived = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)

        self.data = ['empty'] * 12

        self.ThreadCount = 0
        self.sendJSON = {}
        self.clients = []

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def process(self):
        #print('Ждем студентов...')
        try:
            # self.socket.bind((host, port))
            self.socket.bind((socket.gethostname(), 1234))
            self.socket.listen(20)
        except socket.error as e:
            print(str(e))

        while True:
            client, address = self.socket.accept()
            #print('Connected to: ' + address[0] + ' : ' + str(address[1]))
            self.clients.append((client,))
            start_new_thread(self.threaded_client, (client,))

            self.ThreadCount += 1
            #print('Thread Number: ' + str(self.ThreadCount))
        self.socket.close()


    def threaded_client(self, connection):

        thread_number = self.ThreadCount
        # connection.send('empty'.encode('utf-8'))
        while True:
            try:
                # print('sending msg')
                data = self.data[thread_number]
                # print(data)
                connection.send(data.encode('utf-8'))
                self.data[thread_number] = 'empty'
            except:
                pass

            try:
                # print('reciving msg')
                data = connection.recv(2048).decode('utf-8')
                if data != 'empty':
                    data = str(thread_number) + ' ' + data 
                    self.signal_data_recived.emit(data)
                    # print(data)

                if not data:
                    break
            except:
                pass
            time.sleep(0.1) 

        connection.close()
        self.ThreadCount -= 1

    def send_message(self, data):
        for x in range(12):
            self.data[x] = data
