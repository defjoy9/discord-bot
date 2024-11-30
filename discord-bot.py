# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True 
bot = commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to {GUILD}!')

# responds to a message
@bot.command(name='yuh', help='Responds with a random text about Ariana Grande')
async def yuh(ctx):
    choices = [
        'YUH!',
        "did you know that, she was born in 1993?",
        "did you know that, she was born in Florida?",
        "did you know that, she's from US?",
        "did you know that, she's a singer?",
        "did you know that, she's an inventor of 'yuh'?"
    ]
    response = random.choice(choices)
    await ctx.send(response)


bot.run(TOKEN)