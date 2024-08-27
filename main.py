import discord
import random
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

bot.run("Rahasia Dong")



  
