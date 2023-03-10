import discord
import os
import traceback
from app.settings import DISCORD_AUTH_TOKEN
from discord.ext import commands, tasks
from app.handlers import output

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=("00R "), case_insensitive=True, intents=intents)

@bot.slash_command(description="Loads an extension")
async def load(interaction, extension):

    await interaction.response.defer()
    embed = output.embed(title="Load Extension", description = f'Loading {extension}')
    message = await interaction.followup.send(embed=embed)

    try:
        bot.load_extension(f'app.cogs.{extension}')
        await message.edit(embed=output.update(embed, description = f'Loaded {extension}'))
    except Exception as e:
        await message.edit(embed=output.error(embed, e, traceback.format_exc()))

@bot.slash_command(description="Reloads an extension")
async def reload(interaction, extension):

    await interaction.response.defer()
    embed = output.embed(title="Reload Extension", description = f'Reloading {extension}')
    message = await interaction.followup.send(embed=embed)

    try:
        bot.reload_extension(f'app.cogs.{extension}')
        await message.edit(embed=output.update(embed, description = f'Reloaded {extension}'))
    except Exception as e:
        await message.edit(embed=output.error(embed, e, traceback.format_exc()))

@bot.slash_command(description="Unloads an extension")
async def unload(interaction, extension):

    await interaction.response.defer()
    embed = output.embed(title="Unload Extension", description = f'Unloading {extension}')
    message = await interaction.followup.send(embed=embed)
    
    try:
        bot.unload_extension(f'app.cogs.{extension}')
        await message.edit(embed=output.update(embed, description = f'Unloaded {extension}'))
    except Exception as e:
        await message.edit(embed=output.error(embed, e, traceback.format_exc()))
    

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