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
        self.lifes = 10     # const
        self.maxtime = 10   # in seconds
        self.timeleft = self.maxtime

    def next(self):
        self.id += 1

    def next_player(self):
        self.timeleft = self.maxtime
        i = self.players_order.index(self.current_player)
        i += 1
        i %= len(self.players_order)
        self.current_player = self.players_order[i]
        # timer = start
        self.game.windows.mainWindow.update()


    def randomize_order(self):
        random.shuffle(self.players_order)

    def guess_letter(self, letter):
        self.used_letters += letter
        if letter in self.word:
            self.game.scores[self.current_player.nickname] += 1
            # if word guessed:
            word_guessed = True
            for c in self.word:
                if c not in self.used_letters:
                    word_guessed = False
                    break
            if word_guessed:
                self.game.windows.mainWindow.timer_stop()
                # todo
                #   next_round()
        else:
            self.wrong_guess()
        self.next_player()

    def timeout(self):
        self.timeleft -= 1
        if self.timeleft == 0:
            self.next_player()
            self.wrong_guess()


    def guess_word(self, word):
        points = len(self.word)
        for char in self.used_letters:
            for i in range(len(self.word)):
                if self.word[i] == char:
                    points -= 1
        if word == self.word:
            self.game.windows.mainWindow.timer_stop()
            self.game.scores[self.current_player.nickname] += points
            self.game.windows.mainWindow.label_word.setText(self.word.upper())   # Correct word!
            for char in word:
                if char not in self.used_letters:
                    self.used_letters += char
            # todo
            #   next_round()
        else:
            self.game.scores[self.current_player.nickname] -= points
            self.wrong_guess()

    def wrong_guess(self):
        self.lifes -= 1
        self.game.windows.mainWindow.update_img()
        if self.lifes == 1:
            self.game.windows.mainWindow.timer_stop()



