import discord
from discord.ext import commands
import wowoa

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,*args):
    toplam = 0
    for i in args:
        toplam += int(i)
    await ctx.send(f"sonuç:{toplam}")

@bot.command()
async def çıkar(ctx, *args):
    çıkan = int(args[0])
    for i in args[1:]:
        çıkan -= int(i)
    await ctx.send(f"Sonuç: {çıkan}")

@bot.command()
async def çarp(ctx, *args):
    çarpım = 1
    for i in args:
        çarpım *= int(i)
    await ctx.send(f"Sonuç: {çarpım}")

@bot.command()
async def böl(ctx, *args):
    bölüm = float(args[0])
    for i in args[1:]:
        bölüm /= float(i)
    await ctx.send(f"Sonuç: {bölüm}")

@bot.command()
async def şifre(ctx,şifre_sayi=0):
    await ctx.send(wowoa.gen_pass(şifre_sayi))

bot.run("00000000000000")
