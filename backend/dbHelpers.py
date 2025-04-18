import mysql.connector
import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="fabio",
    password="fabio",
    database="anna"
)

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
