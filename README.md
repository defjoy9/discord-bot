# Valorant-Themed Discord Bot

A Python Discord bot I built for fun and to get more comfortable with **async programming, Discord’s API**, and **basic voice/audio streaming** using FFmpeg + yt_dlp.
It includes Valorant-themed randomizers, chat commands, and full voice channel music playback.

---

# 1. Why I Built This

I wanted a small project that let me experiment with:

* Discord’s command/event system
* Asynchronous tasks in Python
* Working with voice channels (which is trickier than text commands)
* Integrating YouTube audio streaming via FFmpeg
* Token management and environment configuration

This bot started as a fun Valorant randomizer, then grew into a full audio-enabled Discord bot.

---

# 2. Features

### 🎲 Valorant Randomizers

Random selection for:

* weapons
* primary/secondary categories
* agent roles
* individual agents

Useful for challenge rounds or just messing around in voice chat.

### 🗨️ Fun Chat Commands

A lightweight example of responding to text commands (Ariana Grande trivia, etc.).

### 🔊 Voice Channel Interaction

The bot can:

* join your current voice channel
* leave on command
* report errors if you're not in a channel

### 🎵 Music Playback (YouTube)

Using `yt_dlp` + FFmpeg, the bot can:

* stream YouTube audio directly into Discord
* stop playback on command
* handle invalid URLs gracefully

---

# 3. How the Bot Works (Architecture)

```
Discord API Events
       │
       ▼
discord.py Command Handler
       │
       ├── Text Commands (randomizers, fun replies)
       │
       └── Voice Commands
              │
              ├─ Join / Leave VC
              └─ Play Audio (yt_dlp → FFmpeg → Discord VoiceClient)
```

Key points:

* Everything runs asynchronously (`async def`, `await`).
* Audio streaming uses subprocess piping from FFmpeg into Discord’s voice protocol.
* Sensitive credentials stay in `.env` (not committed).

---

# 4. Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/defjoy9/discord-bot.git
cd discord-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

You’ll need Python **3.8+**.

### 3. Install FFmpeg

FFmpeg must be installed and available on your PATH.

Download: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### 4. Create `.env`

```env
DISCORD_TOKEN=your-bot-token
DISCORD_GUILD=your-server-name
```

The bot token must stay private — `.env` is ignored by Git.

---

# 5. Available Commands

| Command       | Description                         |
| ------------- | ----------------------------------- |
| `!yuh`        | Fun Ariana Grande fact              |
| `!sidearms`   | Random Valorant sidearm             |
| `!primary`    | Random primary weapon               |
| `!agents`     | Random agent                        |
| `!role`       | Random role                         |
| `!sentinel`   | Random sentinel                     |
| `!initiator`  | Random initiator                    |
| `!dualist`    | Random dualist                      |
| `!controller` | Random controller                   |
| `!join`       | Bot joins your voice channel        |
| `!leave`      | Bot leaves the channel              |
| `!play <url>` | Plays YouTube audio in your channel |
| `!stop`       | Stops playing audio                 |

---

# 6. Error Handling

The bot handles common failure cases:

* Trying to join a channel when the user isn’t in one
* Invalid YouTube URLs
* Missing FFmpeg installation
* Permission errors inside Discord
* Attempting to stop audio when nothing is playing

These failure points helped me practice defensive coding around async functions and exceptions.

---

# 7. Future Improvements

I may expand this project with:

* Slash commands (`/play`, `/agent`, `/pick`)
* Queue system for multiple songs
* Auto-disconnect when idle
* Rich embeds for Valorant data
* Dockerized deployment
* Caching YouTube metadata for faster responses

---

# 8. License

This project is for educational and entertainment use — not affiliated with Riot Games or Discord.
