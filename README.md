# discord-newsgroup

This project was done in an effort to automate notifications for posts made by the professor who uses a USENET newsgroup for the main form of notofications and announcements.

## Instructions
1. Create a .env file with the following schema
```
DISCORD_TOKEN="{your discord bot token here}"
DISCORD_GUILD="{name of the server that will recive notifications}"
DISCORD_CHANNEL_ID="{channel id to recive the messages}"
NEWSGROUP_USR="{newsgroup username}"
NEWSGROUP_PASS="{newsgroup password}"
```
2. Install required libraries `pip install -r requirements.txt`
3. To start the bot, simply run `bot.py`. `python bot.py`