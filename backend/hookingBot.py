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



@bot.tree.command(name="listwebhooks", description="List all the webhooks for the current channel")
async def listwebhooks(interaction: discord.Interaction):
	try:
		webhooks = await interaction.channel.webhooks()
	except Exception as e:
		await interaction.response.send_message(str(e))
		return
	
	if not webhooks:
		# create a webhook named anna
		await interaction.response.send_message("No webhooks found in this channel.Creating one for the anna bot")
		return

	for webhook in webhooks:
		if webhook.name == 'anna':
			#check if the channel id is on the database
			conn = get_db_connection()
			cursor = conn.cursor()

			channel_id = interaction.channel_id
			cursor.execute("SELECT * FROM subscriptions WHERE channel_id = %s", (channel_id))

			if not cursor.fetchone():
				await interaction.response.send_message("No subscription found.", ephemeral=True)
				return

	await interaction.response.send_message("\n")

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)