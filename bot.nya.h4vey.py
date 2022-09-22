# Inspired by CoolansX#7127`s Waifu bot
# Many thanks to CoolansX#7127 for his help with Regex

import discord
import requests
import sys
import re

user=sys.argv[1]
token = sys.argv[2]

#discord hate devs
intents = discord.Intents(guild_messages =  True, guilds = True, messages = True, emojis = True, webhooks = True, message_content = True )
nyabot = discord.Client(intents=intents)

# change the users avatar
async def pfpchange(targetImageUrl):
    print(targetImageUrl)
    reqpfp = requests.get(targetImageUrl)
    await nyabot.user.edit(avatar=reqpfp.content)
    return

#default function
async def default():
    await nyabot.user.edit(username = 'nya.bot')

@nyabot.event
async def on_ready():
    print ('Logged in as {0.user}'.format(nyabot))

#if there is a message
@nyabot.event
async def on_message(message):
    msgauthor = str(message.author)
    oldmessage = str(message.content)
    if(len(message.attachments)>0):
        return

    #debug feature
    if(message.content.startswith('/ping')):
        await message.channel.send('uwu')
        return

    #ignore messages from itself
    if(message.author == nyabot.user):
        return

    #get the right messages
    if(msgauthor == user):
        if(message.content.startswith('\>') or message.content.startswith('https://cdn.discordapp.com/emojis/') or (not re.findall("^:([^:]*):$", oldmessage)==list())):
            return

        #command to change the pfp
        if(message.content.startswith('/pfpchange')):
            await pfpchange(message.content.split("|")[1]) #command should look like this: "/pfpchange|link_to_new_pfp"
            await message.delete()
            await message.channel.send("Profile Picture succesfully changed")
            return

        #check for sentense enders
        if(str(message.content)[-1] == '?'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ ?'

        elif(str(message.content)[-1] == '!'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ !'

        elif(str(message.content)[-1] == '?'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~ ?'

        elif(str(message.content)[-1] == '.'):
            btwmessage = oldmessage[:-1]
            newmessage = f'{btwmessage}, nya~'

        elif(str(message.content)[-1] == ','):
            newmessage = f'{oldmessage} nya~'

        else:
            newmessage = f'{oldmessage}, nya~'

        #delete the old message and send a corrected one
        await message.delete()
        await message.channel.send(newmessage)
        return

nyabot.run(token)
