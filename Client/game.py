import random
import sys
from PyQt5 import QtWidgets
from Server.dbase import Base, Session, engine
from Client.windows.allWindows import Windows
from Client.round import Round
from Server.player import Player
from Server.score import Score
from Server.word import Word


class Game:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.game_id = 1
        self.players = []
        self.words = []
        self.categories = []
        self.online = False
        self.session = None
        self.round = Round(self)
        self.windows = Windows(self)

    def run(self):
        self.windows.show_formNickname()
        sys.exit(self.app.exec_())

    def start_game(self):
        cat = self.round.category
        word = self.get_random_word()
        self.round = Round(self, cat, word)
        self.windows.mainWindow.update()

    def get_current_nickname(self):
        return self.round.current_player.nickname

    def player_add(self, nickname, email, avatar, gender):
        if nickname not in [p.nickname for p in self.players]:
            player = Player(nickname, email, avatar, gender)
            self.players.append(player)
            if self.online:
                try:
                    if nickname not in [p.nickname for p in self.session.query(Player).all()]:
                        self.session.add(player)
                        self.session.commit()
                except:
                    print("Registering new player to the db failed.")
        self.windows.mainWindow.update_players()

    def player_remove(self, name):
        for i in range(len(self.players)):
            if self.players[i].nickname == name:
                self.players.remove(i)
                break
        self.windows.mainWindow.update_players()

    def player_remove_all(self):
        self.players = []
        self.windows.mainWindow.update_players()

    def playerExists(self, nick):
        players = self.players
        if self.online:
            try:
                players = self.session.query(Player).all()
            except:
                print("Query from db failed.")
        for p in players:
            if p.nickname == nick:
                return True
        return False

    def playerLogin(self, nick):
        players = self.players
        if self.online:
            try:
                players = self.session.query(Player).all()
            except:
                print("Query from db failed.")
        for p in players:
            if p.nickname == nick:
                self.player_add(p.nickname, p.email, p.avatar, p.gender)

    def set_category(self, name):
        self.round.category = name
        self.windows.mainWindow.update_category()
        self.update_words()

    def update_words(self):  # Todo add Offline mode, pobierz plik json z bazy słów
        if self.online:
            self.words = []
            cat = self.round.category
            words = self.session.query(Word).all()
            for w in words:
                if w.category == cat:
                    self.words.append(w.word)

    def set_game_id(self, id):
        self.game_id = id
        self.windows.mainWindow.update_game_id()

    def set_online(self):
        self.online = True
        Base.metadata.create_all(engine)
        self.session = Session()
        # self.update_words()       #Todo
        self.update_categories()
        self.set_game_id(self.get_game_id())

    def update_categories(self):  # Todo if !online
        try:
            words = self.session.query(Word).all()
            temp = []
            [temp.append(w.category) for w in words if w.category not in temp]  # uniq(categories)
            self.categories = temp
            self.categories.sort()
            self.windows.mainWindow.update_categories()
        except:
            print("Fetching categories from db failed")

    def get_game_id(self):  # wyszukaj dostępne (kolejne) id w bazie
        scores = self.session.query(Score).all()
        return 1 + max([s.game_id for s in scores])

    def get_random_word(self):
        words = self.words.copy()
        if self.round.word in words:
            words.remove(self.round.word)
        return random.choice(words)


