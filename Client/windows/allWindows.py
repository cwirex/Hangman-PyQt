from PyQt5 import QtWidgets
from Client.windows.mainWindow import Ui_mainWindow
from Client.windows.form_nickname import Ui_formNickname
from Client.windows.form_player import Ui_formPlayer


class Windows:
    def __init__(self, game):
        self.game = game
        self.QmainWindow = QtWidgets.QMainWindow()
        self.QformNickname = QtWidgets.QWidget()
        self.QformPlayer = QtWidgets.QWidget()
        self.mainWindow = Ui_mainWindow(self)
        self.mainWindow.setupUi(self.QmainWindow)
        self.formNickname = Ui_formNickname(self)
        self.formNickname.setupUi(self.QformNickname)
        self.formPlayer = Ui_formPlayer(self)
        self.formPlayer.setupUi(self.QformPlayer)
        self.mainWindow.bind()
        self.formNickname.bind()
        self.formPlayer.bind()

    def show_mainWindow(self):
        self.QmainWindow.show()
        self.QformNickname.hide()
        self.QformPlayer.hide()

    def show_formNickname(self):
        self.QformNickname.show()
        self.QformPlayer.hide()
        self.QmainWindow.hide()

    def show_formPlayer(self):
        self.QformPlayer.show()
        self.QmainWindow.hide()
        self.QformNickname.hide()







