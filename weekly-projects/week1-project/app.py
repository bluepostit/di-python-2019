from flask import Flask
from flask import render_template
app = Flask(__name__)

from profiles import profiles, find_profile
from statuses import statuses


@app.route("/")
def index():
    return render_template('index.html', profiles=profiles)


@app.route("/profiles/<username>")
def profile(username):
    profile = find_profile(username)

    user_statuses = []
    for status in statuses:
        if status['user_id'] == profile['id']:
            user_statuses.append(status)

    return render_template('profile.html', profile=profile,
                           statuses=user_statuses)


@app.route("/profiles/<username>/friends")
def friends(username):
    profile = find_profile(username)

    friends = []
    for friend_id in profile['friends']:
        for friend_profile in profiles:
            if friend_id == friend_profile['id']:
                friends.append(friend_profile)

    return render_template('friends.html', profile=profile, friends=friends)
