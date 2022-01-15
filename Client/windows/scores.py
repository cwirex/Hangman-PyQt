from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Scores(object):
    def __init__(self, windows=None):
        self.windows = windows

    def bind(self):
        self.btn_continue.clicked.connect(self.btn_continue_clicked)
        self.btn_quit.clicked.connect(self.btn_quit_clicked)

    def update(self):
        self.label_header.setText(f"Scores - Game {self.windows.game.game_id}")
        #   Update Players and their Scores:
        self.list_scores.clear()
        arr = []
        for nick in self.windows.game.scores.keys():
            arr.append([self.windows.game.scores[nick], nick])
        arr.sort(reverse=True)
        for i in range(len(arr)):
            item = QtWidgets.QListWidgetItem()
            self.list_scores.addItem(item)
            item = self.list_scores.item(i)
            item.setText(f"{i+1}. {arr[i][1]} ({arr[i][0]})")

    def btn_continue_clicked(self):
        self.windows.show_mainWindow()

    def btn_quit_clicked(self):
        exit(0)

    def setupUi(self, Scores):
        Scores.setObjectName("Scores")
        Scores.resize(743, 453)
        self.btn_quit = QtWidgets.QPushButton(Scores)
        self.btn_quit.setGeometry(QtCore.QRect(400, 390, 141, 41))
        self.btn_quit.setObjectName("btn_quit")
        self.btn_continue = QtWidgets.QPushButton(Scores)
        self.btn_continue.setGeometry(QtCore.QRect(200, 390, 141, 41))
        self.btn_continue.setObjectName("btn_continue")
        self.label_header = QtWidgets.QLabel(Scores)
        self.label_header.setGeometry(QtCore.QRect(0, 10, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(15)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.list_scores = QtWidgets.QListWidget(Scores)
        self.list_scores.setGeometry(QtCore.QRect(160, 90, 421, 241))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.list_scores.setFont(font)
        self.list_scores.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_scores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_scores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.list_scores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_scores.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.list_scores.setFlow(QtWidgets.QListView.TopToBottom)
        self.list_scores.setResizeMode(QtWidgets.QListView.Fixed)
        self.list_scores.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.list_scores.setObjectName("list_scores")
        item = QtWidgets.QListWidgetItem()
        self.list_scores.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_scores.addItem(item)

        self.retranslateUi(Scores)
        QtCore.QMetaObject.connectSlotsByName(Scores)

    def retranslateUi(self, Scores):
        _translate = QtCore.QCoreApplication.translate
        Scores.setWindowTitle(_translate("Scores", "Scores"))
        self.btn_quit.setText(_translate("Scores", "Quit Game"))
        self.btn_continue.setText(_translate("Scores", "Continue"))
        self.label_header.setText(_translate("Scores", "Scores - Game {game_id}"))
        self.list_scores.setSortingEnabled(False)
        __sortingEnabled = self.list_scores.isSortingEnabled()
        self.list_scores.setSortingEnabled(False)
        item = self.list_scores.item(0)
        item.setText(_translate("Scores", "1. player (63)"))
        item = self.list_scores.item(1)
        item.setText(_translate("Scores", "2. nickname (33)"))
        self.list_scores.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scores = QtWidgets.QWidget()
    ui = Ui_Scores()
    ui.setupUi(Scores)
    Scores.show()
    sys.exit(app.exec_())
