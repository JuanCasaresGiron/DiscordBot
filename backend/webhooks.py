import requests

#change this to a manually created webhook for testing 

def announce(channel, title, body, image, url,linkName, webhookURL):
	print(f"Resolve for webhookurl using {channel}")
	data = {
		"content": None,
  		"embeds": [
    	{
			"title": title,
			"description": body,
			"url": url,
			"color": 5814783,
			"fields": [
				{
				  "name": "link:",
				  "value": linkName
				}
      		],
			"image": {
				"url": image
			}
		}],
		"username": "Anna",
		"avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3c11a4e-961b-47ec-8f72-acebce4c4562/dhlnryl-471ce946-0d3b-4908-8327-f509a4821007.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzYzExYTRlLTk2MWItNDdlYy04ZjcyLWFjZWJjZTRjNDU2MlwvZGhsbnJ5bC00NzFjZTk0Ni0wZDNiLTQ5MDgtODMyNy1mNTA5YTQ4MjEwMDcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.ozv0wJFZW8_fzjvuDynX45n4U2mXu9uKngbYGOjomDg",
		"attachments": []
	}	
	response = requests.post(url=webhookURL, json=data)
	print(response.status_code)

