# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import config
import asyncio
from database import init_db

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# DEBUG
print("Token loaded:", DISCORD_TOKEN is not None)

intents = discord.Intents.default()
intents.message_content = True  # REQUIRED to read messages.
intents.members = True # REQUIRED for join/leave messages.

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents, help_command = None)

@bot.event
async def on_ready():
    # Mostly for debugging. If the bot turns on, this message should print in the console
    print(f"Logged in as {bot.user}")


# Loads extensions (events, commands, etc.) on boot-up
async def main():
    init_db()

    await bot.load_extension("commands.help")
    await bot.load_extension("commands.leaderboard")
    await bot.load_extension("commands.xp")
    await bot.load_extension("commands.daily")
    await bot.load_extension("commands.poke")
    await bot.load_extension("commands.rolecreate")
    await bot.load_extension("commands.roleremove")
    await bot.load_extension("commands.restrictword")
    await bot.load_extension("commands.removeword")
    await bot.load_extension("commands.restrictedwords")
    
    await bot.load_extension("events.message")
    await bot.load_extension("events.member")

    await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
