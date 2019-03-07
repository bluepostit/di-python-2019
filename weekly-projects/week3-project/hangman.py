import random
import json

ALLOWED_GUESSES = 10


class Hangman:
    def __init__(self):
        # 1. Load the words from the file
        with open('data/sowpods.txt') as f:
            self.words = [line.strip() for line in f]

        #2. Load the game state from the json file
        self.load()

    def new_game(self):
        self.secret_word = random.choice(self.words)
        self.public_word = list("_" * len(self.secret_word))
        self.guesses = []

    def guess(self, text):
        text = text.strip().lower()
        if text in self.guesses:
            return

        self.guesses.append(text)
        if text == self.secret_word:
            self.public_word = self.secret_word
        else:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == text:
                    self.public_word[i] = text

    def has_guessed_word(self):
        return '_' not in self.public_word

    def load(self):
        with open('data/game-state.json') as f:
            state = json.load(f)
            self.secret_word = state['secret_word']
            self.public_word = state['public_word']
            self.guesses = state['guesses']

    def save(self):
        data = {
            'secret_word': self.secret_word,
            'public_word': self.public_word,
            'guesses': self.guesses
        }
        with open('data/game-state.json', 'w') as f:
            json.dump(data, f)
