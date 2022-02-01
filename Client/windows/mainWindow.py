# Created by: PyQt5 UI code generator 5.15.4
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_mainWindow(object):
    """
    Window class which allows to play the game
    """
    def __init__(self, windows=None):
        """
        Initialize object

        :param windows: Windows (parent)
        """
        self.windows = windows
        self.e_players = []
        self.e_scores = []
        self.e_categories = []
        self.timer_s_start = 100
        self.timer_answer_s_start = 300
        self.timer = QTimer()
        self.timer_answer = QTimer()
        self.timer_s = self.timer_s_start
        self.timer_answer_s = self.timer_answer_s_start

    def bind(self):
        """
        Bind function to window
        """
        self.line_letter.textChanged.connect(self.trim_letter)
        self.btn_letter.clicked.connect(self.btn_GuessLetter_clicked)
        self.btn_word.clicked.connect(self.btn_GuessWord_clicked)
        self.action_AddPlayer.triggered.connect(self.add_player)
        self.action_RemovePlayer.triggered.connect(self.remove_player)
        self.action_Remove_all.triggered.connect(self.remove_all)
        self.Start_Game.triggered.connect(self.start_game)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer_answer.timeout.connect(self.show_answer_update)

    def start_game(self):
        """
        Start game (when button pressed)
        """
        self.windows.game.start_game()

    def add_player(self):
        """
        Call function to add a new player

        :return:
        """
        self.windows.show_formNickname()

    def remove_player(self):  # (na później)
        pass

    def remove_all(self):
        """
        Call function to remove all players
        """
        self.windows.game.player_remove_all()

    def set_guessing_player(self, nick):
        """
        Update window to show current player (form given nick)

        :param nick: string representing the player
        """
        self.label_current_player.setText(f"Now: {nick}")

    def timer_timeout(self):
        """
        Update bar timer, eventually call function round.timeout()
        """
        if self.timer_s > 0:
            self.timer_s -= 1
        else:
            self.timer_s = 100
            self.windows.game.round.timeout()
        time = ((self.windows.game.round.timeleft - 1 + self.timer_s / self.timer_s_start)
                / self.windows.game.round.time) * 100
        self.bar_timer.setValue(time)

    def timer_restart(self):
        """
        Starts the timer from max value
        """
        self.timer_s = self.timer_s_start
        self.timer_start()

    def timer_reset(self):
        """
        Stops timer and sets its max value
        """
        self.timer.stop()
        self.bar_timer.setValue(100)
        self.timer_s = self.timer_s_start
        self.windows.game.round.timeleft = self.windows.game.round.time

    def timer_start(self):
        """
        Start timer
        """
        self.timer.start(10)  # przerwania co 10 ms

    def timer_stop(self):
        """
        Stop timer
        """
        self.timer.stop()

    def show_answer(self):
        """
        Display answer and reset timer
        """
        self.timer_reset()
        self.timer_answer_s = self.timer_answer_s_start
        self.label_word.setText(self.windows.game.round.word.upper())
        self.timer_answer.start(10)

    def show_answer_update(self):
        """
        Update bar timer while showing answer
        """
        self.timer_answer_s -= 1
        self.bar_timer.setValue(int(self.timer_answer_s / self.timer_answer_s_start * 100))
        if self.timer_answer_s == 0:
            self.timer_answer.stop()
            self.windows.game.round.next()

    def set_used_letters(self, string):
        """
        Update used letters and display them

        :param string: string representing the letters used
        """
        final = ""
        for char in string:
            final += char + " "
        final = final.upper()
        self.used_letters.setText(final)

    def update(self):
        """
        Update everything
        """
        self.update_game_id()
        self.update_players()
        self.update_categories()
        self.update_category()
        self.update_current_player()
        self.update_word()
        self.set_used_letters(self.windows.game.round.used_letters)
        self.update_img()
        self.update_time()
        self.update_round()

    def update_word(self):
        """
        Update current word display
        """
        word = self.windows.game.round.word
        result = ""
        for char in word:
            if char in self.windows.game.round.used_letters:
                result += char.upper()
            else:
                result += "_"
        self.label_word.setText(result)

    def update_img(self):
        """
        Update current image display
        """
        lifes = self.windows.game.round.lifes
        img = f'img/h{lifes}_small.jpeg'
        try:
            self.img_hangman.setPixmap(QtGui.QPixmap(img))
        except:
            print('Img not found')

    def update_time(self):
        """
        Update bar time display
        """
        time = ((self.windows.game.round.timeleft - 1 + self.timer_s / 100) / self.windows.game.round.time) * 100
        self.bar_timer.setValue(time)

    def update_round(self):
        """
        Update current round number display
        """
        self.label_round.setText(f"Round {self.windows.game.round.id}/{self.windows.game.rounds_in_game}")

    def update_current_player(self):
        """
        Update current player name display
        """
        self.label_current_player.setText(f"Now: {self.windows.game.get_current_nickname()}")

    def update_game_id(self):
        """
        Update current game id display
        """
        self.label_game.setText(f'Game {self.windows.game.game_id}')

    def update_categories(self):
        """
        Update current game categories display
        """
        while len(self.e_categories) > 0:
            self.menuChoose_category.removeAction(self.e_categories.pop())
        for i in range(len(self.windows.game.categories)):
            self.e_categories.append(QtWidgets.QAction(self.windows.QmainWindow))
            self.e_categories[i].setObjectName(f"category_{i}")
            self.menuChoose_category.addAction(self.e_categories[i])
            self.e_categories[i].setText(f"{self.windows.game.categories[i].capitalize()}")
            self.e_categories[i].triggered.connect(self.create_lambda(self.e_categories[i].text().lower()))

    def update_players(self):
        """
        Update table with players and their scores.
        """
        for i in range(self.formLayout.rowCount() - 1):
            self.formLayout.removeRow(1)
        self.e_players = []
        self.e_scores = []
        players = self.windows.game.players
        for i in range(len(players)):
            self.e_players.append(QtWidgets.QLabel(self.formLayoutWidget))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.e_players[i].setFont(font)
            self.e_players[i].setObjectName(f"player_{players[i].nickname}")
            self.formLayout.setWidget(i + 1, QtWidgets.QFormLayout.LabelRole, self.e_players[i])
            self.e_scores.append(QtWidgets.QLabel(self.formLayoutWidget))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.e_scores[i].setFont(font)
            self.e_scores[i].setAlignment(QtCore.Qt.AlignCenter)
            self.e_scores[i].setObjectName(f"score_{players[i].nickname}")
            self.formLayout.setWidget(i + 1, QtWidgets.QFormLayout.FieldRole, self.e_scores[i])
            self.e_players[i].setText(f"{players[i].nickname}")
            player_score = self.windows.game.scores[players[i].nickname]
            self.e_scores[i].setText(f'{player_score}')

    def update_category(self):
        """
        Update current category display
        """
        category = self.windows.game.round.category
        self.label_category.setText(f'Category: {category.capitalize()}')

    def trim_letter(self):
        """
        Update entered letter to be at max length 1
        """
        text = self.line_letter.text()
        if len(text) > 1:
            text = text[-1]
        self.line_letter.setText(text.upper())

    def btn_GuessLetter_clicked(self):
        """
        Check if letter is correct and call function to check if is in word
        """
        letter = self.line_letter.text().lower()
        self.line_letter.setText("")
        if letter not in self.windows.game.round.used_letters:
            self.timer_reset()
            self.windows.game.round.guess_letter(letter)
            # self.timer_start()

    def btn_GuessWord_clicked(self):
        """
        Call function to check if word is correct
        """
        self.timer_reset()
        word = self.line_word.text().lower()
        self.line_word.setText("")
        self.windows.game.round.guess_word(word)
        # self.timer_start()

    def create_lambda(self, text):
        """
        Create function to bind category label with action

        :param text: string representing category
        :return: function lambda
        """
        return lambda: self.windows.game.set_category(text)

    def setupUi(self, mainWindow):
        """
        Setup the UI

        :param mainWindow: mainWindow
        """
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1600, 900)
        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bar_timer = QtWidgets.QProgressBar(self.centralwidget)
        self.bar_timer.setGeometry(QtCore.QRect(370, 20, 861, 31))
        self.bar_timer.setProperty("value", 100)
        self.bar_timer.setFormat("")
        self.bar_timer.setObjectName("bar_timer")
        self.label_current_player = QtWidgets.QLabel(self.centralwidget)
        self.label_current_player.setGeometry(QtCore.QRect(0, 770, 731, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_current_player.setFont(font)
        self.label_current_player.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_current_player.setAutoFillBackground(False)
        self.label_current_player.setText("")
        self.label_current_player.setTextFormat(QtCore.Qt.AutoText)
        self.label_current_player.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_player.setObjectName("label_current_player")
        self.img_hangman = QtWidgets.QLabel(self.centralwidget)
        self.img_hangman.setGeometry(QtCore.QRect(510, 90, 571, 571))
        self.img_hangman.setText("")
        self.img_hangman.setObjectName("img_hangman")
        self.label_word = QtWidgets.QLabel(self.centralwidget)
        self.label_word.setGeometry(QtCore.QRect(0, 670, 1601, 71))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(34)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_word.setFont(font)
        self.label_word.setTextFormat(QtCore.Qt.AutoText)
        self.label_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word.setWordWrap(False)
        self.label_word.setObjectName("label_word")
        self.label_letters = QtWidgets.QLabel(self.centralwidget)
        self.label_letters.setGeometry(QtCore.QRect(40, 70, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.label_letters.setFont(font)
        self.label_letters.setObjectName("label_letters")
        self.used_letters = QtWidgets.QLabel(self.centralwidget)
        self.used_letters.setGeometry(QtCore.QRect(40, 130, 91, 591))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.used_letters.setFont(font)
        self.used_letters.setText("")
        self.used_letters.setTextFormat(QtCore.Qt.AutoText)
        self.used_letters.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.used_letters.setWordWrap(True)
        self.used_letters.setObjectName("used_letters")
        self.line_word = QtWidgets.QLineEdit(self.centralwidget)
        self.line_word.setGeometry(QtCore.QRect(990, 770, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.line_word.setFont(font)
        self.line_word.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.line_word.setText("")
        self.line_word.setAlignment(QtCore.Qt.AlignCenter)
        self.line_word.setPlaceholderText("")
        self.line_word.setObjectName("line_word")
        self.line_letter = QtWidgets.QLineEdit(self.centralwidget)
        self.line_letter.setGeometry(QtCore.QRect(730, 770, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.line_letter.setFont(font)
        self.line_letter.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.line_letter.setText("")
        self.line_letter.setAlignment(QtCore.Qt.AlignCenter)
        self.line_letter.setPlaceholderText("")
        self.line_letter.setObjectName("line_letter")
        self.btn_letter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_letter.setGeometry(QtCore.QRect(780, 770, 91, 51))
        self.btn_letter.setObjectName("btn_letter")
        self.btn_word = QtWidgets.QPushButton(self.centralwidget)
        self.btn_word.setGeometry(QtCore.QRect(1330, 770, 151, 51))
        self.btn_word.setObjectName("btn_word")
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(0, 50, 1601, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_category.setFont(font)
        self.label_category.setAlignment(QtCore.Qt.AlignCenter)
        self.label_category.setObjectName("label_category")
        self.label_round = QtWidgets.QLabel(self.centralwidget)
        self.label_round.setGeometry(QtCore.QRect(1320, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_round.setFont(font)
        self.label_round.setText("")
        self.label_round.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_round.setObjectName("label_round")
        self.label_game = QtWidgets.QLabel(self.centralwidget)
        self.label_game.setGeometry(QtCore.QRect(1320, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_game.setFont(font)
        self.label_game.setText("")
        self.label_game.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_game.setObjectName("label_game")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1350, 120, 251, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.t_players = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t_players.setFont(font)
        self.t_players.setObjectName("t_players")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.t_players)
        self.t_score = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.t_score.setFont(font)
        self.t_score.setAlignment(QtCore.Qt.AlignCenter)
        self.t_score.setObjectName("t_score")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t_score)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 23))
        self.menubar.setObjectName("menubar")
        self.menuGra = QtWidgets.QMenu(self.menubar)
        self.menuGra.setObjectName("menuGra")
        self.Menage_players = QtWidgets.QMenu(self.menuGra)
        self.Menage_players.setObjectName("Menage_players")
        self.menuChoose_category = QtWidgets.QMenu(self.menuGra)
        self.menuChoose_category.setObjectName("menuChoose_category")
        self.menuOpcje = QtWidgets.QMenu(self.menubar)
        self.menuOpcje.setObjectName("menuOpcje")
        self.menuGame_speed = QtWidgets.QMenu(self.menuOpcje)
        self.menuGame_speed.setObjectName("menuGame_speed")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action_category_yours = QtWidgets.QAction(mainWindow)
        self.action_category_yours.setObjectName("action_category_yours")
        self.action_AddPlayer = QtWidgets.QAction(mainWindow)
        self.action_AddPlayer.setObjectName("action_AddPlayer")
        self.action_RemovePlayer = QtWidgets.QAction(mainWindow)
        self.action_RemovePlayer.setObjectName("action_RemovePlayer")
        self.Start_Game = QtWidgets.QAction(mainWindow)
        self.Start_Game.setObjectName("Start_Game")
        self.actionSlow = QtWidgets.QAction(mainWindow)
        self.actionSlow.setObjectName("actionSlow")
        self.actionNormal = QtWidgets.QAction(mainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actionFast = QtWidgets.QAction(mainWindow)
        self.actionFast.setObjectName("actionFast")
        self.actionNew_game = QtWidgets.QAction(mainWindow)
        self.actionNew_game.setObjectName("actionNew_game")
        self.actionShow_scores = QtWidgets.QAction(mainWindow)
        self.actionShow_scores.setObjectName("actionShow_scores")
        self.action_Remove_all = QtWidgets.QAction(mainWindow)
        self.action_Remove_all.setObjectName("action_Remove_all")
        self.actionNew_Game = QtWidgets.QAction(mainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.New_game = QtWidgets.QAction(mainWindow)
        self.New_game.setObjectName("New_game")
        self.Pause_game = QtWidgets.QAction(mainWindow)
        self.Pause_game.setObjectName("Pause_game")
        self.actionShow_top_scores = QtWidgets.QAction(mainWindow)
        self.actionShow_top_scores.setObjectName("actionShow_top_scores")
        self.ShowTopScores = QtWidgets.QAction(mainWindow)
        self.ShowTopScores.setObjectName("ShowTopScores")
        self.category_1 = QtWidgets.QAction(mainWindow)
        self.category_1.setObjectName("category_1")
        self.Menage_players.addAction(self.action_AddPlayer)
        self.Menage_players.addAction(self.action_Remove_all)
        self.Menage_players.addAction(self.action_RemovePlayer)
        self.Menage_players.addSeparator()
        self.menuChoose_category.addAction(self.action_category_yours)
        self.menuChoose_category.addSeparator()
        self.menuGra.addAction(self.Menage_players.menuAction())
        self.menuGra.addAction(self.menuChoose_category.menuAction())
        self.menuGra.addSeparator()
        self.menuGra.addAction(self.Start_Game)
        self.menuGame_speed.addAction(self.actionSlow)
        self.menuGame_speed.addAction(self.actionNormal)
        self.menuGame_speed.addAction(self.actionFast)
        self.menuOpcje.addAction(self.menuGame_speed.menuAction())
        self.menuOpcje.addSeparator()
        self.menuOpcje.addAction(self.Pause_game)
        self.menuOpcje.addAction(self.New_game)
        self.menubar.addAction(self.menuGra.menuAction())
        self.menubar.addAction(self.menuOpcje.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        """
        Retranslate the UI

        :param mainWindow: mainWindow
        """
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label_word.setText(_translate("mainWindow", "Add Players & Start "))
        self.label_letters.setText(_translate("mainWindow", "Letters used:"))
        self.btn_letter.setText(_translate("mainWindow", "Guess"))
        self.btn_word.setText(_translate("mainWindow", "Guess word"))
        self.label_category.setText(_translate("mainWindow", "Choose category"))
        self.t_players.setText(_translate("mainWindow", "Player"))
        self.t_score.setText(_translate("mainWindow", "Score"))
        self.menuGra.setTitle(_translate("mainWindow", "Start"))
        self.Menage_players.setTitle(_translate("mainWindow", "Menage players"))
        self.menuChoose_category.setTitle(_translate("mainWindow", "Choose category"))
        self.menuOpcje.setTitle(_translate("mainWindow", "Options"))
        self.menuGame_speed.setTitle(_translate("mainWindow", "Game speed"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.action_category_yours.setText(_translate("mainWindow", "Your category"))
        self.action_AddPlayer.setText(_translate("mainWindow", "Add"))
        self.action_RemovePlayer.setText(_translate("mainWindow", "Remove"))
        self.Start_Game.setText(_translate("mainWindow", "Start Game"))
        self.actionSlow.setText(_translate("mainWindow", "Slow"))
        self.actionNormal.setText(_translate("mainWindow", "Normal"))
        self.actionFast.setText(_translate("mainWindow", "Fast"))
        self.actionNew_game.setText(_translate("mainWindow", "New game"))
        self.actionShow_scores.setText(_translate("mainWindow", "Show"))
        self.action_Remove_all.setText(_translate("mainWindow", "Remove all"))
        self.actionNew_Game.setText(_translate("mainWindow", "New Game"))
        self.New_game.setText(_translate("mainWindow", "New game"))
        self.Pause_game.setText(_translate("mainWindow", "Pause game"))
        self.actionShow_top_scores.setText(_translate("mainWindow", "Show top scores"))
        self.ShowTopScores.setText(_translate("mainWindow", "Show"))
        self.category_1.setText(_translate("mainWindow", "Pustynia"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
