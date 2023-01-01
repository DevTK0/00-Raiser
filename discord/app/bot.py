import discord
import os
from app.settings import DISCORD_AUTH_TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'app.cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'app.cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@bot.event
async def on_ready():
    for folder in os.listdir('./app/cogs'):
        if folder.endswith('.py'):
            await bot.load_extension(f'app.cogs.{folder[:-3]}')

bot.run(DISCORD_AUTH_TOKEN)