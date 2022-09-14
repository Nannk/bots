import discord
import requests
import re
from io import BytesIO

nyabot = discord.Client()

async def fake(message):
    targetuserid = message.author.id
    targetusername = str( message.author).split('#')[0]
    # targetavatarurl = message.author.avatar_url 
    # response = requests.get(targetavatarurl)
    # with BytesIO(response.content) as image:
    await nyabot.user.edit(username = 'h4vey0uwutr1edZsh')

async def default():
    await nyabot.user.edit(username = 'nya.bot')

@nyabot.event
async def on_ready():
    print ('Logged in as {0.user}'.format(nyabot))

@nyabot.event
async def on_message(message):
    msgauthor = str(message.author)
    oldmessage = str(message.content)
    if(len(message.attachments)>0):
        return

    # if(message.content.startswith('/start')):
        # await default()
        # await message.channel.send('Uwu')
        # print('Started by: '+ str(message.author))
        # return
    
    if(message.content.startswith('/ping')):
        await message.channel.send('uwu')
        return

    if(message.author == nyabot.user):
        return

    if(msgauthor == 'h4vey0utr1edZsh#2027'):
        if(message.content.startswith('\>') or message.content.startswith('https://cdn.discordapp.com/emojis/') or (not re.findall("^:([^:]*):$", oldmessage)==list())):
            return

        if(list(message.content)[-1] == '?'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ ?'

        elif(list(message.content)[-1] == '!'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ !'

        elif(list(message.content)[-1] == '?'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ ?'

        elif(list(message.content)[-1] == '.'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~'

        elif(list(message.content)[-1] == ','):
            newmessage = f'{oldmessage} nya~'

        else:
            newmessage = f'{oldmessage}, nya~'

        await message.delete()
        # print(f'author: {msgauthor} | edit: {oldmessage}, nya~')
        # newmessage = f'{oldmessage}, nya~'
        # await fake(message)    
        await message.channel.send(newmessage)
        return

nyabot.run('MTAwOTk5MzIwNzI0MjgzODA5Ng.G1Dlsm.XSZQtMhNE0hgCRQWlB5zI14lz8kI8lgX1HJnfg')
