import discord ,os ,asyncio
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(commands_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")
    game = discord.Game('好無聊~~')
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.command()
async def load(ctx: commands.context, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loadad {extension} done.")


@bot.command()
async def unload(ctx: commands.Context, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unload {extension} done.")


@bot.command()
async def reload(ctx: commands.Context, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reload {extension} done.")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions
        await bot.start("BOt TOKEN")

if __name__ == "__main__" :
        asyncio.run(main())