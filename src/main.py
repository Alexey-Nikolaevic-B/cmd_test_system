import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class CMDScreen(QDialog):
    def __init__(self):
        super().__init__()
        
        loadUi('qt\CMD.ui', self)
        self.setWindowIcon(QtGui.QIcon('img/icon_cmd.jpg'))
        self.setWindowTitle('Администратор: Командная строка')


class TestScreen(QDialog):
    def __init__(self):
        super(TestScreen, self).__init__()
        loadUi('qt\Test.ui', self)

        self.cmd = CMDScreen()
        self.cmd.show()


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('qt\Login.ui', self)

        self.btn_start_test.clicked.connect(self.gotoTestScreen)

    def gotoTestScreen(self):
        testScreen = TestScreen()
        widget.addWidget(testScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    loginScreen = LoginScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(loginScreen)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')