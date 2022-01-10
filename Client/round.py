import random


class Round:
    def __init__(self, game, category=None, word=None):
        self.game = game
        self.id = 1
        self.category = category
        self.word = word
        if self.game.players:
            self.players_order = self.game.players.copy()
            self.current_player = self.players_order[0]
        self.used_letters = ""

    def next(self):
        self.id += 1

    def randomize_order(self):
        random.shuffle(self.players_order)


