import discord
# import logging.config

DEFAULT=0x2a82c9
LOADING=0xdfca1f
RUNNING=0x33df1b
STOPPED=0x747474
ERROR=0xdf0f1a

VRISING_THUMBNAIL="https://cdn.discordapp.com/icons/803241158054510612/a_7dcd3bca6f450e85ea1c2802a35b6808.gif?size=32"
MINECRAFT_THUMBNAIL="https://cdn.discordapp.com/icons/302094807046684672/a_4a2d4c71d0ec0c7f72792d7280a6529d.webp?size=32"
COREKEEPER_THUMBNAIL="https://cdn.discordapp.com/icons/851842678340845600/1288f168ce7d27e283fd922569e458d0.webp?size=32"
DEFAULT_THUMBNAIL="https://cdn.discordapp.com/avatars/1016970522791260194/50e1bc4a18d23f6cbf4863a2f541acd1.webp?size=32"

# logging.config.fileConfig("app/logging.conf")

def embed(title="", description="", thumbnail=None, color=LOADING, url=None):
    embed = discord.Embed(title=title, description=description, color=color, url=url) 
    if thumbnail is not None:
        embed.set_thumbnail(url=thumbnail)
    return embed

def update(embed, description="", color=DEFAULT):
    embed.description=description
    embed.color=color
    return embed

def vrising():
    help = embed(
        title="V Rising",
        description="A vampire survival experience. Build your castle, hunt for blood, and rise in power. Conquer the world of the living in a gothic Multiplayer Survival Game.", 
        thumbnail=VRISING_THUMBNAIL, 
        color=DEFAULT,
        url="https://playvrising.com"
        )
    help.add_field(name="/vrising start", value="Starts the server.", inline=False)
    help.add_field(name="/vrising stop", value="Stops the server.", inline=False)
    help.add_field(name="/vrising status", value="Gets the server status.", inline=False)
    help.add_field(name="00R vrising sync <guild_id>", value="Syncs slash commands to the server.", inline=False)
    return help

def vrising_status():
    return embed("V Rising", "Getting server status.", VRISING_THUMBNAIL, LOADING)

def vrising_start():
    return embed("V Rising", "Server is starting.", VRISING_THUMBNAIL, LOADING)

def vrising_stop():
    return embed("V Rising", "Server is stopping.", VRISING_THUMBNAIL, LOADING)

def vrising_sync():
    return embed("V Rising", "Server is syncing.", VRISING_THUMBNAIL, LOADING)

def corekeeper():
    help = embed(
        title="Core Keeper", 
        description="Core Keeper is a survival sandbox game featuring mining, crafting, farming and exploration in a procedurally generated underground world.", 
        thumbnail=COREKEEPER_THUMBNAIL, 
        color=DEFAULT,
        url="https://store.steampowered.com/app/1621690/Core_Keeper/"
        )
    help.add_field(name="/corekeeper start", value="Starts the server.", inline=False)
    help.add_field(name="/corekeeper stop", value="Stops the server.", inline=False)
    help.add_field(name="/corekeeper status", value="Gets the server status.", inline=False)
    help.add_field(name="00R corekeeper sync <guild_id>", value="Syncs slash commands to the server.", inline=False)
    return help

def corekeeper_status():
    return embed("Core Keeper", "Getting server status.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_start():
    return embed("Core Keeper", "Server is starting.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_stop():
    return embed("Core Keeper", "Server is stopping.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_sync():
    return embed("Core Keeper", "Server is syncing.", COREKEEPER_THUMBNAIL, LOADING)

def minecraft():
    help = embed(
        title="Minecraft", 
        description="Minecraft is a sandbox game that allows players to build and explore virtual worlds made up of blocks. Players gather resources, such as wood, stone, and dirt, to craft a variety of items and structures.", 
        thumbnail=MINECRAFT_THUMBNAIL, 
        color=DEFAULT,
        url="https://www.minecraft.net/en-us"
        )
    help.add_field(name="/minecraft start", value="Starts the server.", inline=False)
    help.add_field(name="/minecraft stop", value="Stops the server.", inline=False)
    help.add_field(name="/minecraft status", value="Gets the server status.", inline=False)
    help.add_field(name="00R minecraft sync <guild_id>", value="Syncs slash commands to the server.", inline=False)
    return help

def minecraft_status():
    return embed("Minecraft", "Getting server status.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_start():
    return embed("Minecraft", "Server is starting.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_stop():
    return embed("Minecraft", "Server is stopping.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_sync():
    return embed("Minecraft", "Server is syncing.", MINECRAFT_THUMBNAIL, LOADING)

def server_running(embed, ip):
    embed.description="Server is running."
    embed.color=RUNNING
    embed.add_field(name="IP Address", value=ip, inline=False)

    return embed

def server_stopped(embed):
    embed.description="Server is stopped."
    embed.color=STOPPED

    return embed

def server_status(embed, server):
    embed.description=server["description"]
    
    set_status_color(embed, server["status"])

    if ("ip_address" in server):
        embed.add_field(name="IP Address", value=server["ip_address"], inline=False)

    return embed

def server_synced(embed, description):
    embed.description=description
    embed.color=DEFAULT

    return embed

def set_status_color(embed, status):
    if status == "running":
        embed.color=RUNNING
    elif status == "stopped":
        embed.color=STOPPED

    return embed

def error(embed, error, traceback=None):
    embed.description="Encounted an error."
    embed.color=ERROR
    embed.add_field(name="Cause", value=error, inline=False)

    # logging.error(error)
    # logging.error(traceback)

    return embed