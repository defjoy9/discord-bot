# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#greets new guild member
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# responds to a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    choices = [
        'YUH!',
        (
            'Ariana Grande has the best yuh'
        ),
    ]

    if message.content == 'yuh':
        response = random.choice(choices)
        await message.channel.send(response)

client.run(TOKEN)