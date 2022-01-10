class Round:
    def __init__(self, game, category=None, word=None):
        self.game = game
        self.id = 1
        self.category = category
        self.word = word

    def next(self):
        self.id += 1
