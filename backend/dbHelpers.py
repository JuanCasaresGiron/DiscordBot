import mysql.connector


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

    return channels

def submitAnnouncement(channel, title, body, url):
    print(f"Sending message to {channel}: {title} {body} {url}")
    return True

print(getUsersChannels("anna"))
