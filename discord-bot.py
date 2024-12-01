# bot.py
import os
import random
import discord
import yt_dlp
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

        
# plays youtube
@bot.command(name='play', help='Plays audio from a YouTube URL.')
async def play(ctx, url: str):
    if not ctx.voice_client: 
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel!")
            return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            return

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(url2), after=lambda e: print(f"Finished playing: {e}"))
    await ctx.send(f"Now playing: {info.get('title', 'Unknown Title')}")

@bot.command(name='stop', help='Stops the current audio.')
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Stopped playing!")
    else:
        await ctx.send("I'm not playing anything!")
bot.run(TOKEN)