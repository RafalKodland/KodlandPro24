import discord
from discord.ext import commands
import main

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def generate_password(ctx, length = 8):
    await ctx.send(main.gen_pass(length))

bot.run("MTI0NTA1OTgxMDc4MTU2MDk3NQ.GtTtgM.M4EjurojhJ2f42b5IjfZ4TuxOL1F9GGFdlEHAA")
