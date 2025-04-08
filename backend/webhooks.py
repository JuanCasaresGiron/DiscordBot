import requests

#change this to a manually created webhook for testing 
url = 'https://discord.com/api/webhooks/1358528304268709918/ZMWCZrQRB5J2PGAnP_zOINmZEacpuf9W6RXMFpZUpADfeLFdExVkgB_2QPi-WBHIwChu'

data = {
  "content": None,
  "embeds": [
    {
      "title": "New minecraft server is out",
      "description": "You can log in to our new minecraft server on this",
      "url": "https://www.google.com",
      "color": 5814783,
      "fields": [
        {
          "name": "The IP:",
          "value": "127.0.0.1:1212"
        }
      ],
      "image": {
        "url": "https://wow.zamimg.com/uploads/blog/images/47908-darkmoon-faire-returns-april-6th-boost-cartels-renown-darkfuse-reputation-turn.jpg"
      }
    }
  ],
  "username": "Anna",
  "avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3c11a4e-961b-47ec-8f72-acebce4c4562/dhlnryl-471ce946-0d3b-4908-8327-f509a4821007.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzYzExYTRlLTk2MWItNDdlYy04ZjcyLWFjZWJjZTRjNDU2MlwvZGhsbnJ5bC00NzFjZTk0Ni0wZDNiLTQ5MDgtODMyNy1mNTA5YTQ4MjEwMDcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.ozv0wJFZW8_fzjvuDynX45n4U2mXu9uKngbYGOjomDg",
  "attachments": []
}

response = requests.post(url=url, json=data)
print(response.status_code)

