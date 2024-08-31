import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send("Guess a number between 1 and 10.")

@bot.command()
async def answer(ctx, n):
    if n == random.randint(1, 10):
        await ctx.send('Nice guessing!!!')
    else:
        await ctx.send('Nahhh...., You wrong!!!')

@bot.command()
async def coins(ctx):
    await ctx.send("Guess a side coins between tails or heads.")
@bot.command()
async def coinside(ctx, ans):
    side = ["tails","head"]
    m = (random.choice(side))
    if ans == m:
        await ctx.send('Nice guessing!!!')
        await ctx.send('the coins side is', m)
    else:
        await ctx.send('Nahhh...., You wrong!!!')
        await ctx.send('the true coins side is', m)

@bot.command()
async def meme(ctx):
    images = os.listdir('images')
    with open('images/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def Joke_Gelap(ctx):
    await ctx.send("Negara apa yang gampang kalah dalam permainan catur??")
    
@bot.command()
async def Jawab(ctx, jawab):
    if jawab == 'UK':
        await ctx.send("Selamat Kamu Benar!!!")
        await ctx.send("Karena ratunya mati awokawok")
    else:
        await ctx.send("Salah Nyet!!!....")
        await ctx.send("Yang bener UK!!!....")
        await ctx.send("Karena ratunya mati :)")


bot.run("Rahasia Dong")



  
