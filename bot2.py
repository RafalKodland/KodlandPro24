import discord
from discord.ext import commands
import main
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    slowa = ["Cześć!", "Witaj!", "Dzień Dobry!"]
    await ctx.send(random.choice(slowa))

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def generate_password(ctx, length = 8):
    await ctx.send(main.gen_pass(length))

@bot.command()
async def mem(ctx):
    nazwy = os.listdir("images")
    losowy_obrazek = random.choice(nazwy)
    with open('images/' + losowy_obrazek, 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
    # Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

bot.run("")
