# bot.py
import os

import discord
from dotenv import load_dotenv

# .env
DISCORD_TOKEN={NzA4NzA4MTA0MTgyNjkzODk4.XrbnJw.D4Xm0dkMjdH-WCPj9U3-W5G2Al4}
DISCORD_GUILD={"test 0001's realm"}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)
