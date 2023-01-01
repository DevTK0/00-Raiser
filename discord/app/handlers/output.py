import discord

DEFAULT=0x2a82c9
LOADING=0xdfca1f
RUNNING=0x33df1b
STOPPED=0x747474
ERROR=0xdf0f1a

VRISING_THUMBNAIL="https://cdn.discordapp.com/icons/803241158054510612/a_7dcd3bca6f450e85ea1c2802a35b6808.gif?size=32"
MINECRAFT_THUMBNAIL="https://cdn.discordapp.com/icons/302094807046684672/a_4a2d4c71d0ec0c7f72792d7280a6529d.webp?size=32"
COREKEEPER_THUMBNAIL="https://cdn.discordapp.com/icons/851842678340845600/1288f168ce7d27e283fd922569e458d0.webp?size=32"

def embed(title, description, thumbnail):
    embed = discord.Embed(title=title, description=description, color=LOADING) 
    embed.set_thumbnail(url=thumbnail)
    return embed

def vrising_start():
    return embed("V Rising", "Server is starting.", VRISING_THUMBNAIL)

def vrising_stop():
    return embed("V Rising", "Server is stopping.", VRISING_THUMBNAIL)

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

    return embed

def set_status_color(embed, status):
    if status == "Running":
        embed.color=RUNNING
    elif status == "Stopped":
        embed.color=STOPPED

    return embed

def error(embed, error):
    embed.color=ERROR
    embed.add_field(name="Error", value=error, inline=False)

    return embed
