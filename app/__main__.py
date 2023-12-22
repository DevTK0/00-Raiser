import discord
import os
import traceback
from app.settings import DISCORD_AUTH_TOKEN
from discord.ext import commands, tasks
from app.handlers import output_formatter

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

# Only needed once per guild (used to register commands to the guild through Discord API)
@bot.command(name="sync", description="Syncs slash commands to the guild", aliases=[])
async def sync(ctx, guild_id):
    
    embed = output_formatter.OOR_sync()
    message = await ctx.send(embed=embed) # this is a text command so we use ctx.send instead

    try:
        await bot.sync_commands(
            guild_ids=[guild_id]
        )
        await message.edit(embed=output_formatter.server_synced(embed, description = f'Synced to {guild_id}'))
    except Exception as e:
        await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

@bot.slash_command(description="Loads an extension")
async def load(interaction, extension):

    await interaction.response.defer()
    embed = output_formatter.embed(title="Load Extension", description = f'Loading {extension}')
    message = await interaction.followup.send(embed=embed)

    try:
        bot.load_extension(f'app.cogs.{extension}')
        await message.edit(embed=output_formatter.update(embed, description = f'Loaded {extension}'))
    except Exception as e:
        await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

@bot.slash_command(description="Reloads an extension")
async def reload(interaction, extension):

    await interaction.response.defer()
    embed = output_formatter.embed(title="Reload Extension", description = f'Reloading {extension}')
    message = await interaction.followup.send(embed=embed)

    try:
        bot.reload_extension(f'app.cogs.{extension}')
        await message.edit(embed=output_formatter.update(embed, description = f'Reloaded {extension}'))
    except Exception as e:
        await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))

@bot.slash_command(description="Unloads an extension")
async def unload(interaction, extension):

    await interaction.response.defer()
    embed = output_formatter.embed(title="Unload Extension", description = f'Unloading {extension}')
    message = await interaction.followup.send(embed=embed)
    
    try:
        bot.unload_extension(f'app.cogs.{extension}')
        await message.edit(embed=output_formatter.update(embed, description = f'Unloaded {extension}'))
    except Exception as e:
        await message.edit(embed=output_formatter.error(embed, e, traceback.format_exc()))
    

@tasks.loop(count=1)
async def wait_until_ready():
    for folder in os.listdir('./app/cogs'):
        if folder.endswith('.py'):
            bot.load_extension(f'app.cogs.{folder[:-3]}')

def main():
    wait_until_ready.start()
    bot.run(DISCORD_AUTH_TOKEN)

if __name__ == "__main__":
    main()