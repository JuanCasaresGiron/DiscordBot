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

    return bcrypt.checkpw(password,storedPassword)
    

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

    print(link)
    print(title)
    print(body)
    print(img)
    print(url)
        

    # TODO validate this

    #this statement is vulnerable to sql injection btw
    cursor.execute(f"""
                    INSERT INTO announcements(link,title,body,picture,url)
                    VALUES ('{link}','{title}','{body}','{img}','{url}')
                   """)
    conn.commit()
    cursor.close()
    return True
