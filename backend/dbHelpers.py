import mysql.connector
import os, bcrypt
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database="anna"
)

#Logs the user in, Returns true if the login is valid
def validateUser(username, password:str):
    cursor = conn.cursor()
    cursor.execute("select * from users where username = %s",(username,))
    user = cursor.fetchone()
    #salt for hashing
    salt = bcrypt.gensalt(rounds=12)
    storedPassword:str = user[2]

    #encode to utf
    password = password.encode('utf-8')
    storedPassword = storedPassword.encode('utf-8')

    cursor.close()
    return bcrypt.checkpw(password,storedPassword)

#get all channel subscriptions.
def getSubscriptions(link):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT webhook_url from subscriptions where link = %s",(link,))
    rows = cursor.fetchall()
    return rows
    

#returns a dictionary of all the channels the user owns
def getUsersChannels(username):
    cursor = conn.cursor()

    #this statement is vulnerable to sql injection btw
    cursor.execute(f"""
                    SELECT channels.link, channels.channel_name 
                    FROM channels 
                    LEFT JOIN users ON users.id = channels.owner 
                    WHERE users.username = '{username}' 
                   """)
    rows = cursor.fetchall()
    keys = []
    values = []
    for row in rows:
        keys.append(row[0])
        values.append(row[1])
    
    channels = dict(zip(keys,values))
    cursor.close()
    return channels

def submitAnnouncement(link, title, body, img, url):
    cursor = conn.cursor()

    # TODO validate this

    #this statement is vulnerable to sql injection btw
    cursor.execute(f"""
                    INSERT INTO announcements(link,title,body,picture,url)
                    VALUES ('{link}','{title}','{body}','{img}','{url}')
                   """)
                   
    conn.commit()
    cursor.close()
    return True

def createChannel (channelName, channelLink, username):
    cursor = conn.cursor()
    sql = """
        INSERT INTO channels(channel_name,link,owner) VALUES(
        	%(channelName)s,
	        %(channelLink)s,
	        (select id from users where username = %(username)s)
        )
    """
    params = {'channelName':channelName, 'channelLink':channelLink, 'username':username}
    cursor.execute(sql, params)
    if cursor.rowcount > 0:
        conn.commit()
        cursor.close()
        return True
    else:
        conn.rollback() #I think this does not do anything but just in case
        cursor.close()
        return False
