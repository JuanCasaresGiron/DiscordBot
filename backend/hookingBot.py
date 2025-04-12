import discord
import mysql.connector
from discord.ext import commands
from discord import app_commands

#env variables
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.webhooks = True

bot = commands.Bot(command_prefix="!", intents=intents)
DB_CONFIG = {
    "host": "localhost",
    "user": "fabio",
    "password": "fabio",
    "database": "anna"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@bot.event
async def on_ready():
	await bot.tree.sync()
	print('Bot ready')

async def getChannelWebHook(context: discord.Interaction):
	webhooks = await context.channel.webhooks()
	#get a list of webhooks that are named anna
	annaWebHook = list(filter(lambda webhook: webhook.name =='anna',webhooks))
	if not annaWebHook:
		annaWebHook = await context.channel.create_webhook(name='anna')
	else:
		annaWebHook = annaWebHook[0]
	return annaWebHook.url

@bot.tree.command(name="subscribe", description="Subscribe this channel to a news feed (e.g. anna-general)")
@app_commands.describe(link="The news category to subscribe to")
async def subscribe(interaction: discord.Interaction, link: str):
	#get the current channel id and webhooks
	channelId = interaction.channel_id
	#get the webhook url
	try:
		webhookUrl = await getChannelWebHook(context=interaction)
	except Exception as e:
		await interaction.response.send_message("Please modify the bot's permissions to allow \"Manage WebHooks.\"")
		return

	#open db connection
	conn = get_db_connection()
	cursor = conn.cursor()

	#make sure the link is valid
	#parametized query to prevent sql injection
	cursor.execute("SELECT * FROM channels WHERE link = %s",(link,))
	if not cursor.fetchone():
		await interaction.response.send_message("The link is not valid. Please double check.")
		return
	
	cursor.execute("SELECT link, webhook_url FROM subscriptions WHERE channel_id = %s AND link = %s", (channelId, link))
	subscription = cursor.fetchone()
	if subscription:
		#discord api only allows one response per command so the message needs to go into an array of lines
		messageLines = []
		messageLines.append(f"This channel is already subscribed to `{link}`.")
		#Update the webhook url in case the user messed it up on their end
		fetchedUrl = subscription[1]
		if fetchedUrl != webhookUrl:
			cursor.execute("UPDATE subscriptions SET webhook_url = %s WHERE channel_id = %s AND link = %s", (webhookUrl, channelId, link))
			conn.commit()
			messageLines.append("Webhook URL mismatch. Updated Webhook URL!")
		await interaction.response.send_message("\n".join(messageLines))
	else:
		cursor.execute("INSERT INTO subscriptions (channel_id, link, webhook_url) VALUES (%s, %s, %s)", (channelId, link, webhookUrl))
		conn.commit()
		await interaction.response.send_message(f"This channel has been subscribed to `{link}`!")
	
	cursor.close()
	conn.close()


load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)