import sys
from PyQt5 import QtWidgets
from Server.dbase import Base, Session, engine
from Client.windows.allWindows import Windows
from Server.player import Player

class Game:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.windows = Windows(self)
        self.game_id = 1
        self.round = 1
        self.category = None
        self.words = []
        self.players = []
        self.online = False
        self.session = None

    def run(self):
        self.windows.show_formNickname()
        sys.exit(self.app.exec_())

    def player_add(self, nickname, email, avatar, gender):
        if nickname not in [p.nickname for p in self.players]:
            self.players = Player(nickname, email, avatar, gender)
        # Todo update mainWindow player list

    def player_remove(self, name):
        for i in range(len(self.players)):
            if self.players[i].nickname == name:
                self.players.remove(i)
                break

    def player_remove_all(self):
        self.players = []

    def set_category(self, name):
        self.category = name

    def set_game_id(self, id):
        self.game_id = id

    def set_online(self):
        self.online = True
        Base.metadata.create_all(engine)
        self.session = Session()
        self.update_words()
        self.set_game_id(self.get_game_id())

    def update_words(self):     # Todo pobierz plik json z bazy słów
        pass

    def get_game_id(self):      # Todo wyszukaj dostępne (kolejne) id w bazie
        pass


