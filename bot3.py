import discord
from discord.ext import commands
import random
import bot3mantik

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yazitura(ctx,secim="yazi"):
    await ctx.send(bot3mantik.yazitura(secim))

@bot.command()
async def tahmin(ctx,sayi:int):
    await ctx.send(bot3mantik.tahminoyunu(sayi))






bot.run("000000000000")
