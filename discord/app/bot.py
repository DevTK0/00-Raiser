import boto3

import discord
from settings import DISCORD_AUTH_TOKEN, Game, Configs
from discord.ext import tasks, commands
from handlers import server

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
    response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])
    ctx.message.channel.send(response)
    get_ip_address(ctx, Game.V_RISING.value)

@VRising.command(name="stop", description="Stops the VRising server", aliases=[])
async def vrising_stop(ctx):
    response = server.stop_handler(Game["V_RISING"])
    ctx.message.channel.send(response)

@tasks.loop(seconds=1.0)
async def get_ip_address(ctx, game):
    ip_address = server.get_ip_address(game)

    if ip_address is not None:
        ctx.message.channel.send(f"Server is running at {ip_address}")
        get_ip_address.cancel()
    

async def print(message):
    print(message)


bot.run(DISCORD_AUTH_TOKEN)
