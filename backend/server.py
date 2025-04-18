import os
from flask import Flask,render_template, request, redirect, url_for, session
from dbHelpers import getUsersChannels, submitAnnouncement
import webhooks

app = Flask(__name__)

app.secret_key = "your_secret_key"  # Change this!

users = {
    "anna": "anna123",
    "testuser": "password123",
    "admin": "adminpass"
}

@app.route("/")
def index():
    if 'username' in session:
        channels = getUsersChannels(session['username'])
        return render_template('index.html',channels=channels)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
    if 'username' in session:
        print(session)
        return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/submit', methods=['POST'])
def submit():
    if 'username' not in session:
        return redirect(url_for('login'))
    link = request.form['link']
    title = request.form['title']
    body = request.form['body']
    image = request.form['image']
    url = request.form['url']
    webhookURL = 'https://discord.com/api/webhooks/1358528304268709918/ZMWCZrQRB5J2PGAnP_zOINmZEacpuf9W6RXMFpZUpADfeLFdExVkgB_2QPi-WBHIwChu'

    if(submitAnnouncement(link, title, body, image, url)):
        webhooks.announce(link, title, body, image, url, webhookURL)     

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



#app.run(host='10.108.243.5', port=5000, debug=True)
app.run(host='192.168.1.203', port=5000, debug=True)
