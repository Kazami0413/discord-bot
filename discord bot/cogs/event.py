import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('@'):
        await message.channel.send('快回人家訊息')
    if message.content.startswith('更改狀態'):
        tmp = message.content.split(" ", 1)
        if len(tmp) == 1:
            await message.channel.send("主人,你希望我做什麼？")
        else:
            game = discord.Game(tmp[1])
            await client.change_presence(status=discord.Status.idle, activity=game)