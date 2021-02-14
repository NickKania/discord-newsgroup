import discord
import os
from dotenv import load_dotenv
from newsgroup import recent_posts
import asyncio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
guild = None
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

async def send_chaw_posts():
    await client.wait_until_ready()
    channel = client.get_channel(805918787822944297)
    while True:
        recents = recent_posts(['Sudarshan S Chawathe'])
        if recents:
            print('Found %d new posts, sending to channel' % len(recents))
        else:
            print('No new posts found')
        for r in recents:
            await channel.send(r)
        await asyncio.sleep(1800)


client.loop.create_task(send_chaw_posts())
client.run(TOKEN)
