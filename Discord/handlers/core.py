async def help(message):
    await message.channel.send(
        "```"
        + "00R vrising start - Starts the V Rising Server\n"
        + "00R vrising stop - Stops the V Rising Server\n"
        + "00R vrising status - Gets the V Rising Server status\n"
        + "00R minecraft start - Starts the Minecraft Server\n"
        + "00R minecraft stop - Stops the Minecraft Server\n"
        + "00R minecraft status - Gets the Minecraft Server status\n"
        + "```"
    )
