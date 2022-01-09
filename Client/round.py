class Round:
    def __init__(self, game, category=None):
        self.game = game
        self.id = 1
        self.category = category


    def next(self):
        self.id += 1

