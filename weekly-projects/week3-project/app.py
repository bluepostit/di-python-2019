from flask import Flask
from flask import render_template, request, url_for, redirect

from hangman import Hangman


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/game/")
def show_game():
    hangman = Hangman()
    has_guessed = hangman.has_guessed_word()
    return render_template('game.html', word=hangman.public_word,
                           guesses=hangman.guesses, has_guessed=has_guessed)


@app.route("/game/new/")
def new_game():
    hangman = Hangman()
    hangman.new_game()
    hangman.save()
    return redirect(url_for('show_game'))


@app.route("/game/guess/", methods=['POST'])
def guess_text():
    text = request.form['guess']
    text = text.strip()
    if len(text) > 0:
        hangman = Hangman()
        hangman.guess(text)
        hangman.save()
    return redirect(url_for('show_game'))


@app.route("/stats/")
def show_stats():
    return render_template('stats.html')


# issues
# 1. don't allow guessing once the word is guessed
# 2. don't allow guesses of length > 1
# 3. don't allow guesses beyond the allowed amount
