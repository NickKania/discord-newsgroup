import discord
import os
from dotenv import load_dotenv
from newsgroup import recent_posts
import asyncio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
guild = None
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

@client.event
async def on_message(message):
    channel = client.get_channel(CHANNEL_ID)
    if 'purge' in message.content:
        await channel.purge()

async def send_chaw_posts():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while True:
        recents = recent_posts(['Sudarshan S Chawathe'])
        if recents:
            print('Found %d new posts, sending to channel' % len(recents))
        else:
            print('No new posts found')
        for r in recents:
            embed = discord.Embed(title=r.title, url=r.post_url, description=str(r.date_posted))
            embed.set_author(name=r.author)
            await channel.send(embed=embed) 
        await asyncio.sleep(1800)


client.loop.create_task(send_chaw_posts())
client.run(TOKEN)
