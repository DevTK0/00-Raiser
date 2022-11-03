import boto3

import discord
from settings import DISCORD_AUTH_TOKEN, GAMING_INSTANCE_NAME, LAUNCH_TEMPLATE
from discord.ext import commands
from handlers import vrising
from handlers import core
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

aws = boto3.client("ec2")
ec2 = boto3.resource("ec2")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.group(invoke_without_command=True, case_insensitive=True)
async def Server(ctx):
    await vrising.help_handler(ctx)


@Server.command(name="test", description="Testing APIs", aliases=["t"])
async def server_test(ctx):
    response = requests.get(
        "https://localhost:8000/", verify="./flask/cert/cert.pem"
    ).json()
    await ctx.message.channel.send(response)


@Server.command(name="vrising", description="Testing APIs", aliases=["vr"])
async def server_vrising(ctx):
    response = requests.get(
        "https://localhost:8000/vrising", verify="./flask/cert/cert.pem"
    ).json()
    await ctx.message.channel.send(response)


@bot.group(invoke_without_command=True, case_insensitive=True)
async def VRising(ctx):
    await vrising.help_handler(ctx)


@VRising.command(
    name="start", description="Starts the V Rising Server", aliases=["s", "up", "on"]
)
async def vrising_start(ctx):
    print("start")
    await vrising.start_handler(
        ctx.message, ec2, aws, GAMING_INSTANCE_NAME, LAUNCH_TEMPLATE
    )


@VRising.command(
    name="stop", description="Stops the V Rising Server", aliases=["down", "off"]
)
async def vrising_stop(ctx):
    print("stop")
    await vrising.stop_handler(ctx.message, ec2, GAMING_INSTANCE_NAME)


@VRising.command(
    name="status", description="Gets the V Rising Server status", aliases=[]
)
async def vrising_status(ctx):
    await vrising.status_handler(ctx.message, ec2, GAMING_INSTANCE_NAME)


bot.run(DISCORD_AUTH_TOKEN)
