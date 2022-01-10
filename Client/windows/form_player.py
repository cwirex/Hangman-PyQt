from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formPlayer(object):
    def __init__(self, windows=None, nickname=None):
        self.windows = windows
        self.playerName = nickname

    def bind(self):
        self.pushButton_confirm.clicked.connect(self.clicked)
        self.spinBox_avatar.valueChanged.connect(self.changeAvatar)
        self.img_avatar.setPixmap(QtGui.QPixmap(f'/home/mateusz/PycharmProjects/Hangman/Client/img/a{self.spinBox_avatar.text()}_small.jpg'))

    def clicked(self):
        if self.lineEdit_email.text():
            email = self.lineEdit_email.text()
            gender = self.radioButton_male.isChecked()
            avatar = self.spinBox_avatar.text()
            self.windows.game.player_add(self.playerName, email, avatar, gender)
            self.windows.show_mainWindow()
            self.lineEdit_email.setText("")
            self.radioButton_male.setChecked(True)
            self.spinBox_avatar.setValue(1)
        else:
            self.label_invalid.setText('Invalid values!')
            self.label_invalid.setStyleSheet("color: red;")

    def changeAvatar(self):
        self.img_avatar.setPixmap(
            QtGui.QPixmap(f'/home/mateusz/PycharmProjects/Hangman/Client/img/a{self.spinBox_avatar.text()}_small.jpg'))

    def set_player_name(self, name):
        self.playerName = name
        self.label_header.setText(f"Create {self.playerName}")

    def setupUi(self, formPlayer):
        formPlayer.setObjectName("QformPlayer")
        formPlayer.resize(401, 350)
        self.label_header = QtWidgets.QLabel(formPlayer)
        self.label_header.setGeometry(QtCore.QRect(0, 10, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.gridLayoutWidget = QtWidgets.QWidget(formPlayer)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 180, 253, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_selectavatar = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_selectavatar.setObjectName("label_selectavatar")
        self.gridLayout.addWidget(self.label_selectavatar, 0, 0, 1, 1)
        self.spinBox_avatar = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_avatar.setMinimum(1)
        self.spinBox_avatar.setMaximum(6)
        self.spinBox_avatar.setDisplayIntegerBase(10)
        self.spinBox_avatar.setObjectName("spinBox_avatar")
        self.gridLayout.addWidget(self.spinBox_avatar, 0, 1, 1, 1)
        self.img_avatar = QtWidgets.QLabel(formPlayer)
        self.img_avatar.setGeometry(QtCore.QRect(310, 180, 71, 71))
        self.img_avatar.setObjectName("img_avatar")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(formPlayer)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 130, 251, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_male = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_male.setChecked(True)
        self.radioButton_male.setObjectName("radioButton_male")
        self.gridLayout_2.addWidget(self.radioButton_male, 0, 0, 1, 1)
        self.radioButton_female = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_female.setChecked(False)
        self.radioButton_female.setObjectName("radioButton_female")
        self.gridLayout_2.addWidget(self.radioButton_female, 0, 1, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(formPlayer)
        self.lineEdit_email.setGeometry(QtCore.QRect(80, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.pushButton_confirm = QtWidgets.QPushButton(formPlayer)
        self.pushButton_confirm.setGeometry(QtCore.QRect(130, 270, 141, 41))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.label_invalid = QtWidgets.QLabel(formPlayer)
        self.label_invalid.setEnabled(True)
        self.label_invalid.setGeometry(QtCore.QRect(0, 320, 401, 21))
        self.label_invalid.setText("")
        self.label_invalid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_invalid.setObjectName("label_invalid")

        self.retranslateUi(formPlayer)
        QtCore.QMetaObject.connectSlotsByName(formPlayer)

    def retranslateUi(self, formPlayer):
        _translate = QtCore.QCoreApplication.translate
        formPlayer.setWindowTitle(_translate("QformPlayer", "Form"))
        self.label_header.setText(_translate("QformPlayer", "Create new playerName"))
        self.label_selectavatar.setText(_translate("QformPlayer", "Select avatar"))
        self.img_avatar.setText(_translate("QformPlayer", ""))
        self.radioButton_male.setText(_translate("QformPlayer", "Male"))
        self.radioButton_female.setText(_translate("QformPlayer", "Female"))
        self.lineEdit_email.setPlaceholderText(_translate("QformPlayer", "Your email"))
        self.pushButton_confirm.setText(_translate("QformPlayer", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formPlayer = QtWidgets.QWidget()
    ui = Ui_formPlayer()
    ui.setupUi(formPlayer)
    formPlayer.show()
    sys.exit(app.exec_())
