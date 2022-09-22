
# Inspired by CoolansX#7127`s Waifu bot
# Many thanks to CoolansX#7127 for his help with Regex

import discord
import requests
from PIL import Image
from io import BytesIO

intents = discord.Intents(guild_messages =  True, guilds = True, messages = True, emojis = True, webhooks = True, message_content = True )
nyabot = discord.Client(intents=intents)

# change the users avatar
async def pfpchange(targetImageUrl):
    print(targetImageUrl)
    reqpfp = requests.get(targetImageUrl)
    await nyabot.user.edit(avatar=reqpfp.content)
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

    if(message.content.startswith('/ping')):
        await message.channel.send('uwu')
        return
    if(message.content.startswith('/help')):
        await message.channel.send()

    if(message.author == nyabot.user):
        return

    if(msgauthor == 'maki#1273'):
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

nyabot.run('MTAxODYzMDc4ODQ0ODc4MDMwOQ.G9CQjh.O0fgomn8P3JugFwM-0g93OFZerbdyb557NVOqE')
