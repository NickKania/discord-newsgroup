import discord
import os
from dotenv import load_dotenv
from newsgroup import get_posts

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
guild = None
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected to the following guild: {guild.name}')


async def send_chaw_posts():
    await client.wait_until_ready()
    channel = client.get_channel(805918787822944297)
    posts = get_posts(['Sudarshan S Chawathe'])
    await channel.send(posts[0].title)


client.loop.create_task(send_chaw_posts())
client.run(TOKEN)
