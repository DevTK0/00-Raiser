import discord
import traceback
from discord.ext import tasks, commands, bridge

from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from app.handlers import server, output

class VRising(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def VRising(self, interaction):
        print("vrising")

    @VRising.command(name="sync", description="Syncs slash commands to the guild", aliases=[])
    async def sync(self, ctx):
        
        embed = output.embed(title="Sync", description = f'Syncing slash commands')
        message = await ctx.send(embed=embed)

        try:
            response = await self.bot.sync_commands(guild_ids=[1016971777764765746])
            await message.edit(embed=output.update(embed, description = f'Synced {response}'))
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @commands.slash_command(name="v_rising_start", description="Starts the server.")
    async def start(self, interaction):

        await interaction.response.defer() 
        embed = output.vrising_start()
        message = await interaction.followup.send(embed=embed)

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

    @commands.slash_command(name="v_rising_stop", description="Stops the server.")
    async def stop(self, interaction):

        await interaction.response.defer() 
        embed = output.vrising_stop()
        message = await interaction.followup.send(embed=embed)

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

    @commands.slash_command(name="v_rising_status", description="Gets the server status.")
    async def status(self, interaction):

        await interaction.response.defer() 
        embed = output.vrising_status()
        message = await interaction.followup.send(embed=embed)

        try:
            status = server.status_handler(Game.V_RISING.value)
            await message.edit(embed=output.server_status(embed, status))
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

def setup(bot):
    bot.add_cog(VRising(bot))