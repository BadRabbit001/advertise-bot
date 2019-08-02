# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle
from discord.utils import get
 
client = commands.Bot(command_prefix='-')
#client = discord.Client()
 
#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['DM BlackRabbit for advertise in DMs'])

@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
       
    if message.content.startswith('hi'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
       
    if message.content.startswith('Yo'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
       
    if message.content.startswith('Ye'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
       
    if message.content.startswith('Good morning'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
             
    if message.content.startswith('good evening'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
              
    if message.content.startswith('Rabbit'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg
                                                                 
    if message.content.startswith('advertise'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
                                  
    if message.content.startswith('are you there'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
                                                                                                    
    if message.content.startswith('are you here'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)
                                                                    
    if message.content.startswith('eshop'):
        msg = '**DM to BlackRabbit001#3981 {0.author.mention}'.format(message)
        await message.author.send(msg)

   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()
 
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
 
client.run(os.getenv('BOT_TOKEN'))
