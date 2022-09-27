# Inspired by CoolansX#7127`s Waifu bot
# Many thanks to CoolansX#7127 for his help with Regex

import discord
import requests
import sys
import re
import random

user = sys.argv[1]
token = sys.argv[2]

#discord hate devs
intents = discord.Intents(guild_messages =  True, guilds = True, messages = True, emojis = True, webhooks = True, message_content = True )
nyabot = discord.Client(intents=intents)


add_nya_flag = False

# change the users avatar
async def pfpchange(targetImageUrl):
    print(targetImageUrl)
    reqpfp = requests.get(targetImageUrl)
    await nyabot.user.edit(avatar=reqpfp.content)
    return

# edit the message
async def msg_edit(message,edit):
    message.edit(content=edit)
    return

#add 1 nya randomly inbetween the words. One nya per message. CoolansX wrote this funktion
#async def add_nya(string):
#    l = string.split(" ")
#    l.insert(random.randint(0,(len(l)-1)),"nya,")
#    return " ".join(i for i in l)

#add nya randomly in between the words. Multiple nyas per message
async def add_nya(string):
    res = ""
    l = string.split(" ")
    for i in l[:-1]:
        if( len(i) > 3 and random.randint(0,10) > 6):
            res += f'{i} nya, '
        else:
            res += f'{i} '
    res += f'{l[-1]}'
    return res

@nyabot.event
async def on_ready():
    print ('Logged in as {0.user}'.format(nyabot))

#if there is a message
@nyabot.event
async def on_message(message):
    msgauthor = str(message.author)
    global add_nya_flag

    #check if the feature is active
    if(add_nya_flag):
        oldmessage = await add_nya(str(message.content))
    else:
        oldmessage = str(message.content)

    #ignore messages with attachments
    if(len(message.attachments)>0):
        return

    #debug feature
    if(message.content.startswith('nya|ping')):
        await message.channel.send('uwu')
        return

    #ignore messages from itself
    if(message.author == nyabot.user):
        return

    #get the right messages
    if(msgauthor == user):

        #toggle the add_nya_flag
        if(message.content == 'nya|toggle'):
            add_nya_flag = not add_nya_flag
            await message.channel.send(f'{add_nya_flag}')
            return

        #command to change the pfp
        if(message.content.startswith('nya|pfpchange')):
            await pfpchange(message.content.split("|")[2]) #command should look like this: "/pfpchange|link_to_new_pfp"
            await message.delete()
            await message.channel.send("Profile Picture succesfully changed")
            return

        #ignore message if it starts with a escape sequence
        if(message.content.startswith('\>') or message.content.startswith('https://cdn.discordapp.com/emojis/') or (not re.findall("^:([^:]*):$", oldmessage)==list()) or message.content.startswith('nya')):
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

#        elif(str(message.content)[-1] == ' '):
#            btwmessage = oldmessage[:-1]
#            newmessage = f'{btwmessage}, nya~'

        else:
            newmessage = f'{oldmessage}, nya~'

        #delete the old message and send a corrected one
        await message.delete()
        await message.channel.send(newmessage)
        return

nyabot.run(token)
