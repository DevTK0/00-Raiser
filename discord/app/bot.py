import boto3

import discord
from settings import DISCORD_AUTH_TOKEN, GAMING_INSTANCE_NAME, LAUNCH_TEMPLATE
from discord.ext import commands
from handlers import vrising
from handlers import server
import requests
from status import Game

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

aws = boto3.client("ec2")
ec2 = boto3.resource("ec2")

games = {"VRising": Game("VRising")}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.group(invoke_without_command=True, case_insensitive=True)
async def Server(ctx):
    await vrising.help_handler(ctx)


@Server.command(
    name="start", description="Starts the 00-Raiser Server", aliases=["s", "up", "on"]
)
async def server_start(ctx):
    print("Checking if server is already started")
    print("Starting server")
    await server.start_handler(
        ctx.message, ec2, aws, GAMING_INSTANCE_NAME, LAUNCH_TEMPLATE
    )
    print("Server started")


@Server.command(
    name="stop", description="Stops the 00-Raiser Server", aliases=["down", "off"]
)
async def server_start(ctx):
    print("Check if any running games")
    print("Stopping server")
    await server.stop_handler(ctx.message, ec2, GAMING_INSTANCE_NAME)
    print("Server stopped")


@Server.command(
    name="status", description="Gets the 00-Raiser Server status", aliases=[]
)
async def vrising_status(ctx):
    await server.status_handler(ctx.message, ec2, GAMING_INSTANCE_NAME)


@bot.group(invoke_without_command=True, case_insensitive=True)
async def VRising(ctx):
    await vrising.help_handler(ctx)


@VRising.command(name="start", description="Starts the VRising server", aliases=[])
async def vrising_start(ctx):

    vrising = games["VRising"]
    if vrising.expired():
        vrising.launch()
        print(f"starting v-rising for {vrising.end - vrising.start} hours")
    else:
        print("Game is already running")


@VRising.command(name="stop", description="Stops the VRising server", aliases=[])
async def vrising_stop(ctx):

    vrising = games["VRising"]
    if vrising.expired():
        print("Game is not running")
    else:
        print("VRising terminated")
        vrising.terminate()


@VRising.command(name="extend", description="Starts the VRising server", aliases=[])
async def vrising_status(ctx):

    vrising = games["VRising"]
    if vrising.expired():
        vrising.launch()
        print(f"starting v-rising for {vrising.end - vrising.start} hours")
    else:
        vrising.extend()
        print(f"End time extended to {vrising.end}")


async def print(message):
    print(message)


bot.run(DISCORD_AUTH_TOKEN)
