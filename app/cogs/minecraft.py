import discord
import traceback
from discord.ext import tasks, commands, bridge
from discord.commands import SlashCommandGroup

from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from app.handlers import server, output

class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    minecraft = SlashCommandGroup(name="minecraft", description="Minecraft commands")

    # text command
    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def Minecraft(self, ctx):
        embed = output.minecraft()
        await ctx.send(embed=embed)

    # text command
    @Minecraft.command(name="sync", description="Syncs slash commands to the guild", aliases=[])
    async def sync(self, ctx, guild_id):
        
        embed = output.minecraft_sync()
        message = await ctx.send(embed=embed) # this is a text command so we use ctx.send instead

        try:
            await self.bot.sync_commands(
                guild_ids=[guild_id]
            )
            await message.edit(embed=output.server_synced(embed, description = f'Synced to {guild_id}'))
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @minecraft.command(name="start", description="Starts the server.")
    async def start(self, interaction):

        await interaction.response.defer() 
        embed = output.minecraft_start()
        message = await interaction.followup.send(embed=embed)
        user_configs = {}

        try: 
            response = server.start_handler(Game.MINECRAFT.value, Configs[Game.MINECRAFT] | user_configs)    
            self._get_ip_address.start(message, Game.MINECRAFT.value, embed)
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @tasks.loop(seconds=2.5)
    async def _get_ip_address(self, message, game, embed):
        try:
            ip_address = server.get_ip_address(game)

            if ip_address is not None:
                await message.edit(embed=output.server_running(embed, ip_address))
                self._get_ip_address.cancel()
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))
            self._get_ip_address.cancel()

    @minecraft.command(name="stop", description="Stops the server.")
    async def stop(self, interaction):

        await interaction.response.defer() 
        embed = output.minecraft_stop()
        message = await interaction.followup.send(embed=embed)

        try:
            response = server.stop_handler(Game.MINECRAFT.value)
            self._stop_server_status.start(message, Game.MINECRAFT.value, embed)
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

    @tasks.loop(seconds=15)
    async def _stop_server_status(self, message, game, embed):
        try:
            if server.get_stop_server_status(game):
                await message.edit(embed=output.server_stopped(embed))
                self._stop_server_status.cancel()
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))
            self._stop_server_status.cancel()

    @minecraft.command(name="status", description="Gets the server status.")
    async def status(self, interaction):

        await interaction.response.defer() 
        embed = output.minecraft_status()
        message = await interaction.followup.send(embed=embed)

        try:
            status = server.status_handler(Game.MINECRAFT.value)
            await message.edit(embed=output.server_status(embed, status))
        except Exception as e:
            await message.edit(embed=output.error(embed, e, traceback.format_exc()))

def setup(bot):
    bot.add_cog(Minecraft(bot))