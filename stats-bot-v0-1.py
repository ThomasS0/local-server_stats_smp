#notes: it doesn't send a message if you start the minecraft client, ONLY when you launch your server it'll send a message
#also, the server must run in the same machine as the bot since this is a personal SMP stats bot
import os
import asyncio
import discord
import time

#function to get the task names and try to find the server one("java.exe")
def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        if name in r[i]:
            return True
    return False

TOKEN = 'your-token-here'
idserver = your-server-id
idchat = your-chat-id

client = discord.Client()
process = 'java.exe'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')#confirming in the console that your bot is connected
    print(f'{client.get_guild(idserver)} || server ||')#another confirmation but this one is to confirm the server id matches the desired server
    while True:
        if getTasks(process):
            await client.get_channel(idchat).send('server online!')
        else:
            await client.get_channel(idchat).send('server offline.')
        time.sleep(900)#i've choosen 15 min because i think lower would be a spam in the chat and higher would be too slow

client.run(TOKEN)
