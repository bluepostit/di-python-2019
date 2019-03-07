from flask import Flask
from flask import render_template, request, url_for, session, redirect

import auth
import messages

app = Flask(__name__)
app.secret_key = b'aj(>,m&*@#NxmaiOxH23Kkmlb128($'


@app.route("/")
@app.route("/messages/")
def show_messages():
    if 'username' in session:
        msgs = messages.get_messages(session.get('username'))
        return render_template('messages.html', messages=msgs)
    else:
        return redirect(url_for('login'))


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if auth.login(username, password):
            session['username'] = username
            return redirect(url_for('show_messages'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('show_messages'))


@app.route("/message/<int:id>/")
def show_message(id):
    message = messages.get_message(id)
    return render_template('message.html', message=message)


@app.route("/message/compose/", methods=["GET", "POST"])
def compose():
    if request.method == 'GET':
        return render_template('compose.html')
    elif request.method == 'POST':
        msg_to = request.form.get('to', None)
        msg_from = session.get('username')
        msg_subject = request.form.get('subject', None)
        msg_body = request.form.get('body', None)
        messages.add({
            'to': msg_to,
            'from': msg_from,
            'subject': msg_subject,
            'body': msg_body
        })
        return redirect(url_for('show_messages'))