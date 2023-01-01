import discord
import asyncio
import traceback
from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from discord.ext import tasks, commands
from app.handlers import server, output

from app.cogs.vrising import VRising

# from app.handlers import vrising 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.command()
async def load(ctx, extension):
    # await bot.load_extension(f'app.cogs.{extension}')
    await bot.load_extension(
        "app.cogs.vrising"
    )

@bot.command()
async def unload(ctx, extension):
    # await bot.unload_extension(f'app.cogs.{extension}')
    await bot.unload_extension(
        "app.cogs.vrising"
    )

bot.run(DISCORD_AUTH_TOKEN)    
# @bot.group(invoke_without_command=True, case_insensitive=True)
# async def VRising(ctx):
#     print("vrising")


# @VRising.command(name="start", description="Starts the server", aliases=[])
# async def vrising_start(ctx):
    
#     embed = output.vrising_start()
#     message = await ctx.send(embed=embed)

#     try: 
#         response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])    
#         get_ip_address.start(message, Game.V_RISING.value, embed)
#     except Exception as e:
#         await message.edit(embed=output.error(embed, e, traceback.format_exc()))

# @tasks.loop(seconds=2.5)
# async def get_ip_address(message, game, embed):
#     try:
#         ip_address = server.get_ip_address(game)

#         if ip_address is not None:
#             await message.edit(embed=output.server_running(embed, ip_address))
#             get_ip_address.cancel()
#     except Exception as e:
#         await message.edit(embed=output.error(embed, e, traceback.format_exc()))
#         get_ip_address.cancel()

# @VRising.command(name="stop", description="Stops the server", aliases=[])
# async def vrising_stop(ctx):

#     embed = output.vrising_stop()
#     message = await ctx.send(embed=embed)

#     try:
#         response = server.stop_handler(Game.V_RISING.value)
#         stop_server_status.start(message, Game.V_RISING.value, embed)
#     except Exception as e:
#         await message.edit(embed=output.error(embed, e, traceback.format_exc()))

# @tasks.loop(seconds=15)
# async def stop_server_status(message, game, embed):
#     try:
#         if server.get_stop_server_status(game):
#             await message.edit(embed=output.server_stopped(embed))
#             stop_server_status.cancel()
#     except Exception as e:
#         await message.edit(embed=output.error(embed, e, traceback.format_exc()))
#         stop_server_status.cancel()

# @VRising.command(name="status", description="Check the status of the server.", aliases=[])
# async def vrising_status(ctx):

#     embed = output.vrising_status()
#     message = await ctx.send(embed=embed)

#     try:
#         status = server.status_handler(Game.V_RISING.value)
#         await message.edit(embed=output.server_status(embed, status))
#     except Exception as e:
#         await message.edit(embed=output.error(embed, e, traceback.format_exc()))

