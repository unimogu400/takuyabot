import discord
from discord.ext import commands
from discord.ext import tasks

import random

DISCORD_TOKEN = ''

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('ログインしました')

    
@client.event

async def on_message(message):
    if message.author.bot: #Botに反応しない
            return
        
    def check(msg):
        return msg.author==message.author
    
    if message.content == 'おお':
        await message.channel.send('おおじゃないが')
        rdm=random.randint(0, 100)
        if rdm < 4:
            await message.channel.send('これはおおだろ')

client.run(DISCORD_TOKEN)