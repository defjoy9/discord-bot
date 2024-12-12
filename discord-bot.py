# bot.py
import os
import random
import discord
import yt_dlp
from dotenv import load_dotenv
from discord.ext import commands

def random_weaponoragent(type):
    #guns
    sidearms = ['Classic','Shorty','Frenzy','Ghost','Sherif']
    primary = ['Bucky','Judge','Bulldog','Guardian','Phantom','Vandal','Marshal','Outlaw','Operator','Ares','Odin']
    #agents
    role = "Sentinel", "Initiator","Dualist","Controller"
    agents = "Brimstone", "Viper","Omen","Killjoy","Cypher","Sova","Sage","Phoenix","Jett","Reyna","Raze","Breach","Skye","Yoru","Astra","KAY/O","Chamber","Neon","Fade","Harbor","Gekko","Deadlock","Iso","Clove","Vyse"
    sentinels = "Killjoy", "Cypher", "Sage", "Chamber","Deadlock","Vyse"
    initiators = "Sova","Breach","Skye","KAY/O","Fade","Gekko"
    dualists = "Phoenix","Jett","Reyna","Raze","Yoru","Neon","Iso"
    controllers = "Brimstone", "Viper", "Omen", "Astra","Harbor", "Clove"


    match type:
        case "sidearms":
            random_index = random.randint(0,4)
            return sidearms[random_index]
        
        case "primary":
            random_index = random.randint(0,9)
            return primary[random_index]
        case "agents":
            random_index = random.randint(0,24)
            return agents[random_index]
        case "role":
            random_index = random.randint(0,3)
            return role[random_index]
        case "sentinels":
            random_index = random.randint(0,5)
            return sentinels[random_index]
        case "initiators":
            random_index = random.randint(0,5)
            return initiators[random_index]
        case "dualists":
            random_index = random.randint(0,6)
            return dualists[random_index]
        case "controllers":
            random_index = random.randint(0,5)
            return controllers[random_index]
        

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

#valorant theme
@bot.command(name='sidearms', help='Randomly chooses a sidearm gun from valorant')
async def sidearms(ctx):
    response = random_weaponoragent("sidearms")
    await ctx.send(response)

@bot.command(name='primary', help='Randomly chooses a primary gun from valorant')
async def primary(ctx):
    response = random_weaponoragent("primary")
    await ctx.send(response)

@bot.command(name='role', help='Randomly chooses an agent role from valorant')
async def sidearms(ctx):
    response = random_weaponoragent("role")
    await ctx.send(response)

@bot.command(name='agents', help='Randomly chooses an agent from valorant')
async def sidearms(ctx):
    response = random_weaponoragent("agents")
    await ctx.send(response)

@bot.command(name='sentinel', help='Randomly chooses a sentinel agent from valorant')
async def sentinels(ctx):
    response = random_weaponoragent("sentinels")
    await ctx.send(response)

@bot.command(name='initiator', help='Randomly chooses a initiator agent from valorant')
async def sentinels(ctx):
    response = random_weaponoragent("initiators")
    await ctx.send(response)

@bot.command(name='dualist', help='Randomly chooses a dualist agent from valorant')
async def sentinels(ctx):
    response = random_weaponoragent("dualists")
    await ctx.send(response)

@bot.command(name='controller', help='Randomly chooses a controller agent from valorant')
async def sentinels(ctx):
    response = random_weaponoragent("sentinels")
    await ctx.send(response)
# ----

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