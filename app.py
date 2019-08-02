# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix='ú')
#client = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['DM BlackRabbit001#3981 for advertise in DM'])
 
    
@client.event
async def on_ready():
    print("Bot Was Deployed Sucessfully !")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!helddlo'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)

    if message.content.startswith('!forddtnite'):
        randomlist = ['https://filemedia/fortnite','https://up-to-do27527/fortnite02','https://filemedia.net/27527/fortnite2']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('?bddan'):
        msg = 'https://gifimage.net/wp-content//ban-hammer-gif-14.gif'.format(message)
        await message.channel.send(msg)
                
    if message.content.startswith('!Spotifddy'):
        randomlist = ['https://direct-link.ne,'https://directify4','https://direct-link.nespotify2']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('rsssabbit'):
        msg = 'https://i.pinimg.com/orb167972d4121152caded1bcf4.gif'.format(message)
        await message.channel.send(msg)  
            
    if message.content.startswith('!stosddck'):
        randomlist = ['visit #how-to-gen for + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!nossrd'):
        randomlist = ['https://filenet/27527/NordVPN','https://filemedia.ordVPN2','https://filemedia.net/27527/NoN3']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!spsssotify'):
        randomlist = ['https://direct-link.net/27spotify4','https://direct-link.net/7/spotify4','https:irect-link.net/27527/spotify3']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('!origisssn'):
        randomlist = ['https://link-to.net/275origin','httpsink-to.net/27527/origin','https://link-to.net27/origin']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!hulssu'):
        randomlist = ['https://filemedinet/27527/lu2','https://emedia.ne7527/hulu','https://filemedia/27527/hulu2']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!stesssam'):
        randomlist = ['https://filemedia.net/277/steam	','https://filemedia.net/277/steam	','https://filemedia.net/27/steam	']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!udssemy'):
        randomlist = ['https://filemedia.net/275udemy2','https://up-to-down27527/udemy','https://up-to-.net/27527/udemy']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!uplassy'):
        randomlist = ['https://up-to-do.net/27527/uplay2','https://up-to-wn.net/27527/uplay2','https://up-tdown.net/27527/uplay']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!crunchyrssoll'):
        randomlist = ['https://up-to-down.net/27527/cruyroll','https://up-to-down.n27527/crunchyroll','https://up-to-dn.net/27527/crunchyroll']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!scrissbd'):
        randomlist = ['https://direct-link.net/227/Scribd','https://direct-lin.net/27527/Scribd','https://drect-link.net/2727/Scribd']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                        
    if message.content.startswith('!famissslyowner'):
        randomlist = ['https://direct-link.net/2727/familyowner','https://direct-link.net/27527familyowner','https://dirct-link.net/27527/familyowner']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                                
    if message.content.startswith('hello'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!help'):
        await message.author.send("https://rabbit001.cf/bot/commands.html")
        
        
    if message.content.startswith('!purge'):
        args = message.content.split(" ")
        a = int(args[1])
        await message.channel.purge(limit=a)
    await client.process_commands(message)
    
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
