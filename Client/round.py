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

    def guess_letter(self, letter):
        self.used_letters += letter
        if letter in self.word:
            self.game.scores[self.current_player.nickname] += 1
            # todo
            #   self.current_player = self.next_player()
            #   if word guessed: next_round()
        else:
            pass

    def guess_word(self, word):
        points = len(self.word)
        for char in self.used_letters:
            for i in range(len(self.word)):
                if self.word[i] == char:
                    points -= 1
        if word == self.word:
            self.game.scores[self.current_player.nickname] += points
            self.game.windows.mainWindow.label_word.setText(self.word.upper())   # Correct word!
            self.used_letters = word
            # todo
            #   next_round()
        else:
            self.game.scores[self.current_player.nickname] -= points



