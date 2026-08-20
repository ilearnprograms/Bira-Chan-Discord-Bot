import discord
from discord.ext import commands
import aiohttp, asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# ---------------------------------------- HELLO COMMAND ----------------------------------------
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------- COMMANDS ----------------------------------------
    @commands.command()
    async def komutlar(self, ctx):
        await ctx.send(
            "```"
            "Selam! Ben Bira Chan. Kushimoto'nun Python test botuyum. "
            "Bi sigara olsa da bira ile içsem...🚬\n\n"
            "!turksigara, !sigara veya !cigara — Rastgele bir turksigara.net resmi çağırır. 🚬\n\n"
            "!turkbira, !bira !tuborg veya !efes — Rastgele bir turkbira.net resmi çağırır. 🍺\n\n"
            "Hepsi bu kadar. Bu arada, bi sigara var mı be? 🙄"
            "```\n")
        await ctx.send("https://klipy.com/gifs/yani-neko-chainsmoker-cat")

async def setup(bot):
    await bot.add_cog(Fun(bot))