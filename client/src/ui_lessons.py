from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class LessonsScreen(QDialog):
    def __init__(self):
        super(LessonsScreen, self).__init__()
        loadUi('C:\dev/new\client\qt\Lessons.ui', self)