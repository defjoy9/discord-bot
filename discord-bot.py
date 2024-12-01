# bot.py
import os
import random
import discord
import yt_dlp as youtube_dl
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


@bot.command(name='join', help='Joins the voice channel you are in.')
async def join(ctx):
    if ctx.author.voice: 
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel.name}!")
    else:
        await ctx.send("You are not in a voice channel!")

@bot.command(name='leave', help='Leaves the voice channel.')
async def leave(ctx):
    if ctx.voice_client: 
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel!")
    else:
        await ctx.send("I'm not in a voice channel!")

bot.run(TOKEN)