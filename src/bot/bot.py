import os
import discord
from dotenv import load_dotenv
from image_manager import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MAINTAINER = os.getenv('MAINTAINER')
client = discord.Client()



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break 

    message = "{}, is operating in {}".format(client.user, guild.name)
    print(message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    match(message.content.lower()):
        case '!miku':
            await message.channel.send(file=discord.File(retrieve_image('miku')))
        case '!doge':
            await message.channel.send(file=discord.File(retrieve_image('doge')))

        case _:
            file = discord.File(retrieve_image('default'))
            await message.channel.send('Not yet implemented, ask the maintainer({}) to support that character!!'.format(MAINTAINER), file=file)
        

def run_bot():
    client.run(TOKEN)