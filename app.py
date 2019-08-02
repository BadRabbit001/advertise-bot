# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix='!')
#client = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['www.rabbit001.cf', 'With BlackRabbit', 'with Generator', 'with accounts'])

@client.command()
async def lala(ctx):
    check_role = get(ctx.message.guild.roles, name='Leader')
    if check_role in ctx.author.roles:
        await ctx.send("Yes, you are the leader.")

    else:
        await ctx.send("You can't use this")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx):
    check_role = get(ctx.message.guild.roles, name='BAN-SQUAD')
    if check_role in ctx.author.roles:
        await ctx.send("https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif")
    else:
        await ctx.send("You can't use this")
    
@client.event
async def on_ready():
    print("Bot Was Deployed Sucessfully !")
    while True:
        await client.change_presence(game=Game(name='with BadRabbit'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='with Generator'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='this Server', type = 3))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Viktor Sheen', type = 2))
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
                
    if message.content.startswith('!uplassy'):
        randomlist = ['https://up-to-do.net/27527/uplay2','https://up-to-wn.net/27527/uplay2','https://up-tdown.net/27527/uplay']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

                                
    if message.content.startswith('hello'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
                                
    if message.content.startswith('yo'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
                                
    if message.content.startswith('hi'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
                                 
    if message.content.startswith('ye'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('rabbit'):
        randomlist = ['**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**','**DM TO BlackRabbit001#3981**']
        msg = 'Hello ' + author + '   '
        await message.author.send(msg + (random.choice(randomlist)))
    
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
