import os
from flask import Flask,render_template, request, redirect, url_for, session
from dbHelpers import getUsersChannels, submitAnnouncement, validateUser, getSubscriptions, createChannel
import webhooks

app = Flask(__name__)

app.secret_key = "your_secret_key"  # Change this!

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
        if validateUser(username=username,password=password):
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

    #check if user owns the channel
    username = session['username']
    userChannels = getUsersChannels(username)

    if not userChannels.get(link):
        print('User does not own the specified channel') #Return this to user.
        return redirect(url_for('index'))

    #get all webhook urls
    webhookURLs = getSubscriptions(link)
    webhookURLs = [webhookURL[0] for webhookURL in webhookURLs]
    
    if(submitAnnouncement(link, title, body, image, url)):
        webhooks.announce(link, title, body, image, url, link ,webhookURLs)

    return redirect(url_for('index'))

@app.route('/create_channel', methods=['POST'])
def create_channel():
    if 'username' not in session:
        return redirect(url_for('login'))

    channel_name = request.form['channel_name']
    channel_link = request.form['channel_link']
    username = session['username']
    
    if not createChannel(channel_name, channel_link, username): 
        print('Issues creating the channel') # send a notification on the site in the future
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



#app.run(host='10.108.243.5', port=5000, debug=True)
app.run(host='192.168.1.203', port=5000, debug=True)
