import discord
from discord.ext import commands
import wowoa
import os
import random
import requests

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

@bot.command()
async def resim(ctx):
    with open("images/bir.png","rb") as f:
        picture=discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    x= random.choice(os.listdir("images"))
    with open(f"images/{x}","rb") as f:
        picture=discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

def get_pokemon_image_url():
    pokemon_id = random.randint(1, 898)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(url)
    data = res.json()
    return data['sprites']['front_default']


@bot.command(name='pokemon')
async def pokemon(ctx):
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

bot.run("00000000000000")
