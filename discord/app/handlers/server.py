import asyncio
from aws import AWS

logging.basicConfig(filename="server.log" , level=logging.INFO)

def help_handler(ctx):
    return "You must provide a subcommand, available commands: "
            + "```"
            + "00R vrising start\n"
            + "00R vrising stop\n"
            + "00R vrising status\n"
            + "```"


def status_handler(message, ec2, nametag):
    print("status")

def stop_handler(game):
    
    with AWS() as aws:
        server = aws.get_server_status(game)

        if (server["status"] == "running" or server["status"] == "stopping"):
            server.stop_server(ec2, templateId)
            return "Server is shutting down."

        if (server["status"] == "stopped"):
            return "Server is already stopped."

def start_handler(game):

    with AWS() as aws:
        server = aws.get_server_status(game)
        templateId = aws.get_launch_template_id(game)

        if (server["status"] == "running"):
            return "Server is already running with IP: {}".format(server["ip"])

        if (server["status"] == "stopped" and server["ami_id"] is not None):
            server.start_server(ec2, templateId, server["ami_id"])
            return "Server is starting."

        if (server["status"] == "stopping"):
            server.start_server(ec2, templateId, server["ami_id"])
            return "Server is shutting down. Please wait a few minutes and try again."

        if (server["status"] == "archived"):
            print("Server is archived.")
            return "Server has been archived due to inactivity."
