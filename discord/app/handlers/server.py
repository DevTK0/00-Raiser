import asyncio

from aws import AWS

async def help_handler(ctx):
    await ctx.send(
        "You must provide a subcommand, available commands: "
        + "```"
        + "00R vrising start\n"
        + "00R vrising stop\n"
        + "00R vrising status\n"
        + "```"
    )


async def status_handler(message, ec2, nametag):
    print("status")

async def stop_handler(message, ec2, nametag):
    print("stop")


async def start_handler(message, ec2, aws, game):

    server = aws.get_server_status(ec2, game)
    templateId = aws.get_launch_template_id(aws, game)

    if (server["status"] == "running"):
        await message.channel.send("Server is already running with IP: {}:9876".format(server["ip"]))
        return

    if (server["status"] == "stopped" and server["ami_id"] is not None):
        server.start_server(ec2, templateId, server["ami_id"])
        await message.channel.send("Server is starting.")
        return

    if (server["status"] == "stopping"):
        server.start_server(ec2, templateId, server["ami_id"])
        await message.channel.send("Server is shutting down. Please wait a few minutes and try again.")
        return

    if (server["status"] == "archived"):
        print("Server is archived.")
        await message.channel.send("Server has been archived due to inactivity.")
        return
