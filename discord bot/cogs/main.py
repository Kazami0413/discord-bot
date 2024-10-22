import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def Hello(self, ctx: commands.Context):
        await ctx.send("主人,你好")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "kurumi":
            await message.channel.send("主人,叫我嗎?")

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))