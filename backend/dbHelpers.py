def getUsersChannels(username):
    channels = {
        "General Bot News":"anna-general",
        "Sports News":"anna-sports",
        "Finance News":"anna-finance"
    }
    return channels

def submitAnnouncement(channel, title, body, url):
    print(f"Sending message to {channel}: {title} {body} {url}")
    return True
