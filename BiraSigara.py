import os
import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True, application_id=1540050040242970824)

# bot token
token = os.getenv("BIRA_PYTHON_TOKEN")

if not token:
    raise RuntimeError("BIRA_PYTHON_TOKEN is not set!")

@bot.event
async def on_ready():
    print(f"{bot.user} has accessed Discord!")

# -------------------- async cog load --------------------
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")  # <- await for async setup

# -------------------- run bot --------------------
async def main():
    async with bot:
        await load_cogs()
        await bot.start(token)
    
asyncio.run(main())
