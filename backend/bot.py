'''
OLD SCRIPT, NOT BEING USED.
NEW VERSION IS CALLED: HookingBot.py
'''

import discord
import mysql.connector
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime

import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

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
    print(f"✅ Logged in as {bot.user}")
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("✅ Bot connected!")
                await bot.tree.sync()
            except:
                pass
    check_news_updates.start()

@bot.tree.command(name="subscribe", description="Subscribe this channel to a news feed (e.g. anna-general)")
@app_commands.describe(link="The news category to subscribe to")
async def subscribe(interaction: discord.Interaction, link: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    channel_id = interaction.channel_id
    cursor.execute("SELECT * FROM channels WHERE link = %s", (link,))
    if not cursor.fetchone():
        await interaction.response.send_message("That news channel does not exist.", ephemeral=True)
        return

    cursor.execute("SELECT * FROM subscriptions WHERE channel_id = %s AND link = %s", (channel_id, link))
    if cursor.fetchone():
        await interaction.response.send_message(f"This channel is already subscribed to `{link}`.", ephemeral=True)
    else:
        cursor.execute("INSERT INTO subscriptions (channel_id, link) VALUES (%s, %s)", (channel_id, link))
        conn.commit()
        await interaction.response.send_message(f"This channel has been subscribed to `{link}`!", ephemeral=True)

    cursor.close()
    conn.close()

@tasks.loop(minutes=1)
async def check_news_updates():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM news WHERE displayed = 0 ORDER BY timestamp ASC")
    news_items = cursor.fetchall()

    for row in news_items:
        link = row['channel']

        embed = discord.Embed(
            title=row['title'],
            description=row['body'],
            url=row['url'],
            color=discord.Color.blue()
        )
        if row['timestamp']:
            embed.set_footer(text=row['timestamp'].strftime("%Y-%m-%d %H:%M"))
        if row['picture']:
            embed.set_image(url=row['picture'])

        cursor.execute("SELECT channel_id FROM subscriptions WHERE link = %s", (link,))
        subscribed_channels = cursor.fetchall()

        for sub in subscribed_channels:
            channel = bot.get_channel(int(sub['channel_id']))
            if channel:
                try:
                    await channel.send(embed=embed)
                except:
                    continue

        cursor.execute("UPDATE news SET displayed = 1 WHERE id = %s", (row['id'],))
        conn.commit()

    cursor.close()
    conn.close()

# Load variables from .env file
load_dotenv()

# Access the variables
token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
