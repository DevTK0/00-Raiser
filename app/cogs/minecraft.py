import discord
import traceback
from discord.ext import tasks, commands, bridge
from discord.commands import SlashCommandGroup

from app.settings import DISCORD_AUTH_TOKEN, Game, Configs
from app.handlers import output_formatter, server, input_parser

class Minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.user_configs = {}

    minecraft = SlashCommandGroup(name="minecraft", description="Minecraft commands")

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def Minecraft(self, ctx):
        embed = output_formatter.minecraft()
        await ctx.send(embed=embed)

    # Only needed once per guild (used to register commands to the guild through Discord API)
    @Minecraft.command(name="sync", description="Syncs slash commands to the guild", aliases=[])
    async def sync(self, ctx, guild_id):
        
        embed = output_formatter.minecraft_sync()
        message = await ctx.send(embed=embed) # this is a text command so we use ctx.send instead

        try:
            await self.bot.sync_commands(
                guild_ids=[guild_id]
            )
            await message.edit(embed=output_formatter.server_synced(embed, description = f'Synced to {guild_id}'))
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

    @minecraft.command(name="start", description="Starts the server.")
    async def start(self, interaction):

        await interaction.response.defer() 
        embed = output_formatter.minecraft_start()
        message = await interaction.followup.send(embed=embed)
        user_configs = self.user_configs

        try: 
            response = server.start_handler(Game.MINECRAFT.value, Configs[Game.MINECRAFT] | user_configs)    
            self._get_server_details.start(message, Game.MINECRAFT.value, embed)
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

    # Note that config is only saved in RAM and will be lost if the bot restarts.
    @minecraft.command(name="set_instance", description="Configures the AWS instance to run on (temporarily).")
    async def set_instance(self, interaction, instance_type):

        await interaction.response.defer()  

        user_configs = {}

        embed = output_formatter.minecraft_set_instance_success(instance_type)
        
        input_parser.check_instance(embed, user_configs, instance_type)
        
        self.user_configs = user_configs

        await interaction.followup.send(embed=embed)      

    @tasks.loop(seconds=2.5)
    async def _get_server_details(self, message, game, embed):
        try:
            server_details = server.get_server_details(game)

            if server_details is not None:
                await message.edit(embed=output_formatter.server_running(embed, server_details))
                self._get_server_details.cancel()
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))
            self._get_server_details.cancel()

    @minecraft.command(name="stop", description="Stops the server.")
    async def stop(self, interaction):

        await interaction.response.defer() 
        embed = output_formatter.minecraft_stop()
        message = await interaction.followup.send(embed=embed)

        try:
            response = server.stop_handler(Game.MINECRAFT.value)
            self._stop_server_status.start(message, Game.MINECRAFT.value, embed)
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

    @tasks.loop(seconds=15)
    async def _stop_server_status(self, message, game, embed):
        try:
            if server.get_stop_server_status(game):
                await message.edit(embed=output_formatter.server_stopped(embed))
                self._stop_server_status.cancel()
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))
            self._stop_server_status.cancel()

    @minecraft.command(name="status", description="Gets the server status.")
    async def status(self, interaction):

        await interaction.response.defer() 
        embed = output_formatter.minecraft_status()
        message = await interaction.followup.send(embed=embed)

        try:
            status = server.status_handler(Game.MINECRAFT.value)
            await message.edit(embed=output_formatter.server_status(embed, status))
        except Exception as e:
            await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

def setup(bot):
    bot.add_cog(Minecraft(bot))