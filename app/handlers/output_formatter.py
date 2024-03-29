import discord
# import logging.config

DEFAULT=0x2a82c9
LOADING=0xdfca1f
RUNNING=0x33df1b
SUCCESS=0x33df1b
STOPPED=0x747474
ERROR=0xdf0f1a

VRISING_THUMBNAIL="https://cdn.discordapp.com/icons/803241158054510612/a_7dcd3bca6f450e85ea1c2802a35b6808.gif?size=32"
MINECRAFT_THUMBNAIL="https://cdn.discordapp.com/icons/302094807046684672/a_4a2d4c71d0ec0c7f72792d7280a6529d.webp?size=32"
COREKEEPER_THUMBNAIL="https://cdn.discordapp.com/icons/851842678340845600/1288f168ce7d27e283fd922569e458d0.webp?size=32"
PALWORLD_THUMBNAIL="https://cdn.discordapp.com/icons/505994577942151180/b03aa1253c3b1017a6b78c4a58489b1d.png?size=32"
DEFAULT_THUMBNAIL="https://cdn.discordapp.com/avatars/1016970522791260194/50e1bc4a18d23f6cbf4863a2f541acd1.webp?size=32"

# logging.config.fileConfig("app/logging.conf")

def embed(title="", description="", thumbnail=None, color=LOADING, url=None):
    embed = discord.Embed(title=title, description=description, color=color, url=url) 
    if thumbnail is not None:
        embed.set_thumbnail(url=thumbnail)
    return embed

# def update(embed, description="", color=DEFAULT):
#     embed.description=description
#     embed.color=color
#     return embed

def restart(embed):
    embed.description="Server is restarting."
    embed.color=LOADING
    return embed


def set_instance_error(embed, instance_type):

    embed.color=ERROR
    embed.description=f"{instance_type} is not a valid instance."

    embed.add_field(name="Testing", value="t2.small, t2.medium", inline=False)
    # embed.add_field(name="GPU", value="g4dn.xlarge", inline=False)
    embed.add_field(name="Budget", value="c5a.large, r5a.large, r6a.large", inline=False)
    embed.add_field(name="Normal", value="c5a.xlarge, r5a.xlarge, r6a.xlarge", inline=False)
    embed.add_field(name="Performance", value="c5a.2xlarge, r5a.2xlarge, r6a.2xlarge", inline=False)


def OOR_sync():
    return embed("00 Raiser", "00R is syncing.", DEFAULT_THUMBNAIL, LOADING)

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
    help.add_field(name="/vrising restart", value="Restarts the server.", inline=False)
    help.add_field(name="/vrising status", value="Gets the server status.", inline=False)
    help.add_field(name="/vrising set_instance", value="Changes the instance type.", inline=False)
    help.add_field(name="00R vrising sync <guild_id>", value="Syncs slash commands to the server.", inline=False)
    return help

def vrising_status():
    return embed("V Rising", "Getting server status.", VRISING_THUMBNAIL, LOADING)

def vrising_set_instance_success(instance_type):
    return embed("V Rising", f"Instance Configured to {instance_type}.", VRISING_THUMBNAIL, SUCCESS)

def vrising_start():
    return embed("V Rising", "Server is starting.", VRISING_THUMBNAIL, LOADING)

def vrising_stop():
    return embed("V Rising", "Server is stopping.", VRISING_THUMBNAIL, LOADING)

def vrising_restart():
    return embed("V Rising", "Server is restarting.", VRISING_THUMBNAIL, LOADING)

def vrising_sync():
    return embed("V Rising", "Server is syncing.", VRISING_THUMBNAIL, LOADING)

def palworld():
    help = embed(
        title="Palworld", 
        description="Fight, farm, build and work alongside mysterious creatures called \"Pals\" in this completely new multiplayer, open world survival and crafting game!", 
        thumbnail=PALWORLD_THUMBNAIL, 
        color=DEFAULT,
        url="https://store.steampowered.com/app/1621690/Core_Keeper/"
        )
    help.add_field(name="/palworld start", value="Starts the server.", inline=False)
    help.add_field(name="/palworld stop", value="Stops the server.", inline=False)
    help.add_field(name="/palworld restart", value="Restarts the server.", inline=False)
    help.add_field(name="/palworld status", value="Gets the server status.", inline=False)
    help.add_field(name="/palworld set_instance", value="Changes the instance type.", inline=False)
    help.add_field(name="00R palworld sync <guild_id>", value="Syncs slash commands to the server.", inline=False)

    return help

def palworld_status():
    return embed("Palworld", "Getting server status.", PALWORLD_THUMBNAIL, LOADING)

def palworld_set_instance_success(instance_type):
    return embed("Palworld", f"Instance Configured to {instance_type}.", PALWORLD_THUMBNAIL, SUCCESS)

def palworld_start():
    return embed("Palworld", "Server is starting.", PALWORLD_THUMBNAIL, LOADING)

def palworld_stop():
    return embed("Palworld", "Server is stopping.", PALWORLD_THUMBNAIL, LOADING)

def palworld_restart():
    return embed("Palworld", "Server is restarting.", PALWORLD_THUMBNAIL, LOADING)

def palworld_sync():
    return embed("Palworld", "Server is syncing.", PALWORLD_THUMBNAIL, LOADING)

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
    help.add_field(name="/corekeeper restart", value="Restarts the server.", inline=False)
    help.add_field(name="/corekeeper status", value="Gets the server status.", inline=False)
    help.add_field(name="/corekeeper set_instance", value="Changes the instance type.", inline=False)
    help.add_field(name="00R corekeeper sync <guild_id>", value="Syncs slash commands to the server.", inline=False)

    return help

def corekeeper_status():
    return embed("Core Keeper", "Getting server status.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_set_instance_success(instance_type):
    return embed("Core Keeper", f"Instance Configured to {instance_type}.", COREKEEPER_THUMBNAIL, SUCCESS)

def corekeeper_start():
    return embed("Core Keeper", "Server is starting.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_stop():
    return embed("Core Keeper", "Server is stopping.", COREKEEPER_THUMBNAIL, LOADING)

def corekeeper_restart():
    return embed("Core Keeper", "Server is restarting.", COREKEEPER_THUMBNAIL, LOADING)

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
    help.add_field(name="/minecraft restart", value="Restarts the server.", inline=False)
    help.add_field(name="/minecraft status", value="Gets the server status.", inline=False)
    help.add_field(name="/minecraft set_instance", value="Changes the instance type.", inline=False)
    help.add_field(name="00R minecraft sync <guild_id>", value="Syncs slash commands to the server.", inline=False)
    return help

def minecraft_status():
    return embed("Minecraft", "Getting server status.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_set_instance_success(instance_type):
    return embed("Minecraft", f"Instance Configured to {instance_type}.", MINECRAFT_THUMBNAIL, SUCCESS)

def minecraft_start():
    return embed("Minecraft", "Server is starting.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_stop():
    return embed("Minecraft", "Server is stopping.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_restart():
    return embed("Minecraft", "Server is restarting.", MINECRAFT_THUMBNAIL, LOADING)

def minecraft_sync():
    return embed("Minecraft", "Server is syncing.", MINECRAFT_THUMBNAIL, LOADING)

def server_running(embed, server_details):
    print(server_details)
    embed.description="Server is running."
    embed.color=RUNNING
    embed.add_field(name="IP Address", value=server_details["ip_address"], inline=False)
    embed.add_field(name="Instance Type", value=server_details["instance_type"], inline=False)

    return embed

def server_stopped(embed):
    embed.description="Server is stopped."
    embed.color=STOPPED

    return embed

def server_status(embed, server_details):
    embed.description=server_details["description"]
    
    set_status_color(embed, server_details["status"])

    if ("ip_address" in server_details):
        embed.add_field(name="IP Address", value=server_details["ip_address"], inline=False)
        embed.add_field(name="Instance Type", value=server_details["instance_type"], inline=False)

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