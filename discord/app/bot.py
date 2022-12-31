import boto3

import discord
from settings import DISCORD_AUTH_TOKEN
from discord.ext import commands
from handlers import server
from games import Game

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.group(invoke_without_command=True, case_insensitive=True)
async def VRising(ctx):
    print("vrising")


@VRising.command(name="start", description="Starts the VRising server", aliases=[])
async def vrising_start(ctx):
    response = server.start_handler(Game.V_RISING)
    ctx.message.channel.send(response)

@VRising.command(name="stop", description="Stops the VRising server", aliases=[])
async def vrising_stop(ctx):
    response = server.stop_handler(Game.V_RISING)
    ctx.message.channel.send(response)

async def print(message):
    print(message)


bot.run(DISCORD_AUTH_TOKEN)
