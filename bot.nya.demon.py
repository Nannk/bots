
# Inspired by CoolansX#7127`s Waifu bot
# Many thanks to CoolansX#7127 for his help with Regex

import discord
import requests
from PIL import Image
from io import BytesIO

intents = discord.Intents(guild_messages =  True, guilds = True, messages = True, emojis = True, message_content = True )
nyabot = discord.Client(intents=intents)

async def pfpchange(targetImageUrl):
    print(targetImageUrl)
    newpfp = requests.get(targetImageUrl)
    with Image.open(BytesIO(newpfp.content)) as imagePfp:
        #img=Image.open(BytesIO(newpfp.content))
        await nyabot.user.edit(avatar=imagePfp)
    return

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

    if(msgauthor == 'DemonKingSwarn#0951'):
        if(message.content.startswith('\>') or message.content.startswith('https://cdn.discordapp.com/emojis/')):
            return

        if(message.content.startswith('/pfpchange')):
            await pfpchange(message.content.split("|")[1]) #command should look like this: "/pfpchange|link_to_new_pfp"
            await message.delete()
            await message.channel.send("Profile Picture succesfully changed")
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

nyabot.run('MTAyMDc5OTQ4MjMxODgyMzQ4NQ.GT64bx.2_JTVx5x-cmZQqjLPoAYwMFN0YaMTjNLntdCns')
