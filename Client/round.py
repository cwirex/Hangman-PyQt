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
        self.lifes = 10  # current lifes; max=10
        self.time = 5  # in seconds
        self.timeleft = self.time

    def next(self):
        self.game.windows.mainWindow.timer_reset()
        if self.id < self.game.rounds_in_game:
            self.id += 1
            self.lifes = 10
            self.used_letters = ""
            self.word = self.game.get_random_word()
            self.timeleft = self.time
            self.game.windows.mainWindow.update()
            self.game.windows.mainWindow.timer_restart()
        else:
            self.game.game_over()

    def next_player(self):
        i = self.players_order.index(self.current_player)
        i += 1
        i %= len(self.players_order)
        self.current_player = self.players_order[i]
        self.game.windows.mainWindow.update_current_player()

    def guess_letter(self, letter):
        self.used_letters += letter
        self.game.windows.mainWindow.set_used_letters(self.used_letters)
        if letter in self.word:
            self.game.windows.mainWindow.update_word()
            self.game.scores[self.current_player.nickname] += 1
            self.game.windows.mainWindow.update_players()
            self.next_player()
            word_guessed = True
            for c in self.word:
                if c not in self.used_letters:
                    word_guessed = False
                    break
            if word_guessed:
                self.game.windows.mainWindow.show_answer()
            else:
                self.game.windows.mainWindow.timer_start()
        else:
            self.wrong_guess()
            self.next_player()

    def guess_word(self, word):
        # oblicz możliwe punkty za trafienie/pudło:
        points = len(self.word)
        for char in self.used_letters:
            for i in range(len(self.word)):
                if self.word[i] == char:
                    points -= 1
        # trafienie czy pudło:
        if word == self.word:
            self.game.scores[self.current_player.nickname] += points
            self.game.windows.mainWindow.update_players()
            self.next_player()
            self.game.windows.mainWindow.show_answer()
        else:
            self.game.scores[self.current_player.nickname] -= points
            self.game.windows.mainWindow.update_players()
            self.next_player()
            self.game.windows.mainWindow.timer_start()

    def timeout(self):
        if self.timeleft > 0:
            self.timeleft -= 1
        else:
            self.timeleft = self.time
            self.next_player()
            self.wrong_guess()

    def wrong_guess(self):
        self.lifes -= 1
        self.game.windows.mainWindow.update_img()
        if self.lifes > 1:
            self.game.windows.mainWindow.timer_start()
        else:
            self.game.windows.mainWindow.show_answer()

    def randomize_order(self):
        random.shuffle(self.players_order)
