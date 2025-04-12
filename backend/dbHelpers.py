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

def uploadImage(image):
    url = "https://api.imgur.com/3/upload"
    clientId = os.getenv("IMGUR_CLIENT_ID")
    headers = {"Authorization": f"Client-ID {clientId}"}
    with open(image, "rb") as image_file:
        payload = {
            "image": image_file.read()
    }

    response = requests.post(url, headers=headers, files=payload)
    # Check if the upload was successful
    if response.status_code == 200:
        json_response = response.json()
        # The uploaded image link is available in json_response["data"]["link"]
        image_url = json_response["data"]["link"]
        return image_url
    else:
        # Return error information from the response
        return f"Error: {response.status_code} - {response.json()}"


def submitAnnouncement(channel, title, body, img, url):
    cursor = conn.cursor()

    #validate this
    cursor.execute(f"select id from channels where link = '{channel}' LIMIT 1")
    channelId = cursor.fetchall()[0][0]

    #this statement is vulnerable to sql injection btw
    cursor.execute(f"""
                    INSERT INTO news(channel,title,body,picture,url)
                    VALUES ({channelId},'{title}','{body}','{img}','{url}')
                   """)
    conn.commit()
    cursor.close()
    return True
