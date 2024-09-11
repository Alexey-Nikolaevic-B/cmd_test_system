from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class ResultScreen(QDialog):
    def __init__(self):
        super(ResultScreen, self).__init__()
        loadUi('C:\dev/new\client\qt\Result.ui', self)