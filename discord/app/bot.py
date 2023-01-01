import discord
import os
from app.settings import DISCORD_AUTH_TOKEN
from discord.ext import commands
from app.handlers import output

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.command()
async def load(ctx, extension):

    embed = output.embed(title="Load Extension", description = f'Loading {extension}')
    message = await ctx.send(embed=embed)

    try:
        await bot.load_extension(f'app.cogs.{extension}')
        await message.edit(embed=output.update(embed, description = f'Loaded {extension}'))
    except Exception as e:
        await message.edit(embed=output.error(embed, e))

@bot.command()
async def unload(ctx, extension):

    embed = output.embed(title="Unload Extension", description = f'Unloading {extension}')
    message = await ctx.send(embed=embed)

    try:
        await bot.unload_extension(f'app.cogs.{extension}')
        await message.edit(embed=output.update(embed, description = f'Unloaded {extension}'))
    except Exception as e:
        await message.edit(embed=output.error(embed, e))

@bot.event
async def on_ready():
    for folder in os.listdir('./app/cogs'):
        if folder.endswith('.py'):
            await bot.load_extension(f'app.cogs.{folder[:-3]}')

bot.run(DISCORD_AUTH_TOKEN)