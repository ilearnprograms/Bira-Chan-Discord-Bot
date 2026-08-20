import discord
from discord.ext import commands
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ---------------------------------------- TURKBIRA ----------------------------------------

class TurkBira(commands.Cog):
    def __ini__(self, bot):
        self.bot = bot

    @commands.command(name= "turkbira",aliases= ['bira','tuborg','efes',"türkbira"])
    async def turkira(self, ctx):
        await ctx.send("Biralar dolduruluyor. Birazcık bekle.")

        # setting up headless chrome
        options = Options()
        options.add_argument("--headless=new")  # <-- newer, better headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)

        try:
            driver.get("https://turkbira.net/")
            
            # click random button
            random_btn = driver.find_element("class name", "random-btn")
            random_btn.click()

            # wait for image to load
            await asyncio.sleep(1)

            # find img
            img_tag = driver.find_element("tag name", "img")
            img_url = img_tag.get_attribute("src")

            embed = discord.Embed(title="TürkBira'dan rastgele bir resim 🍺", color=discord.Color.yellow())
            embed.set_image(url=img_url)
            await ctx.send(embed=embed)

        finally:
            driver.quit()

async def setup(bot):
    await bot.add_cog(TurkBira(bot))  