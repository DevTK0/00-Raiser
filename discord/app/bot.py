import discord
from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from discord.ext import tasks, commands
from app.handlers import server

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.group(invoke_without_command=True, case_insensitive=True)
async def VRising(ctx):
    print("vrising")


@VRising.command(name="start", description="Starts the VRising server", aliases=[])
async def vrising_start(ctx):
    try:
        response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])
        await ctx.message.channel.send(response)
        get_ip_address.start(ctx, Game.V_RISING.value)
    except Exception as e:
        await ctx.message.channel.send(f"Error: {e}")

@VRising.command(name="stop", description="Stops the VRising server", aliases=[])
async def vrising_stop(ctx):
    try:
        response = server.stop_handler(Game.V_RISING.value)
        await ctx.message.channel.send(response)
    except Exception as e:
        await ctx.message.channel.send(f"Error: {e}")

@tasks.loop(seconds=2.5)
async def get_ip_address(ctx, game):
    try:
        ip_address = server.get_ip_address(game)

        if ip_address is not None:
            await ctx.message.channel.send(f"Server is running at {ip_address}")
            get_ip_address.cancel()
    except Exception as e:
        await ctx.message.channel.send(f"Error: {e}")
        get_ip_address.cancel()
    
@bot.command(name="test", description="Test command", aliases=[])
async def print(ctx, message):
    await ctx.message.channel.send(message)


bot.run(DISCORD_AUTH_TOKEN)
