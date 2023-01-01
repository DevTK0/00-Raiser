import discord
import traceback
from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from discord.ext import tasks, commands
from app.handlers import server, output

class VRising(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def VRising(self, ctx):
        print("vrising")

    @VRising.command(name="start", description="Starts the server", aliases=[])
    async def vrising_start(self, ctx):
        
        embed = output.vrising_start()
        message = await ctx.send(embed=embed)

        try: 
            response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])    
            self._get_ip_address.start(message, Game.V_RISING.value, embed)
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @tasks.loop(seconds=2.5)
    async def _get_ip_address(self, message, game, embed):
        try:
            ip_address = server.get_ip_address(game)

            if ip_address is not None:
                await message.edit(embed=output.server_running(embed, ip_address))
                get_ip_address.cancel()
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))
            get_ip_address.cancel()

    @VRising.command(name="stop", description="Stops the server", aliases=[])
    async def vrising_stop(self, ctx):

        embed = output.vrising_stop()
        message = await ctx.send(embed=embed)

        try:
            response = server.stop_handler(Game.V_RISING.value)
            self._stop_server_status.start(message, Game.V_RISING.value, embed)
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @tasks.loop(seconds=15)
    async def _stop_server_status(self, message, game, embed):
        try:
            if server.get_stop_server_status(game):
                await message.edit(embed=output.server_stopped(embed))
                stop_server_status.cancel()
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))
            stop_server_status.cancel()

    @VRising.command(name="status", description="Check the status of the server.", aliases=[])
    async def vrising_status(self, ctx):

        embed = output.vrising_status()
        message = await ctx.send(embed=embed)

        try:
            status = server.status_handler(Game.V_RISING.value)
            await message.edit(embed=output.server_status(embed, status))
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

async def setup(bot):
    await bot.add_cog(VRising(bot))