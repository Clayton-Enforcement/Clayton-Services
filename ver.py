import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Clayton Services is ran by Clayton_Enforcement")
    await client.change_presence(game=Game(name='Ran by Clayton_Enforcement'))

@client.event
async def on_message(message):
    if message.content.startswith('!graphics'):
            msg = 'Hello {0.author.mention} You may find the information for graphics on the Clayton Services Trello here: https://trello.com/c/VxipridF/2-graphic-project-pricing'.format(message)
            await client.send_message(message.channel, msg)
    if message.content.startswith('!bot'):
            msg = 'Hello {0.author.mention} You may find the information for bots on the Clayton Services Trello here: https://trello.com/c/9F8v8o0j/3-bot-project-pricing'.format(message)
            await client.send_message(message.channel, msg)
    if message.content.startswith('!development'):
            msg = 'Hello {0.author.mention} You may find the information for development on the Clayton Services Trello here: https://trello.com/c/T2dgVkWk/4-development-project-pricing'.format(message)
            await client.send_message(message.channel, msg)
            


client.run(os.getenv('TOKEN')


