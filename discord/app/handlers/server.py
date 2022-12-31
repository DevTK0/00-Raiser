import asyncio
import logging
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

def stop_handler(message, ec2, nametag):
    print("stop")


def start_handler(game):
    aws = AWS()
    
    try:    
        response = aws.start_server(aws, game)
    except Exception as ex:
        logging.error(ex)
        response = "Error starting server."

    aws.close()
    return response

def aws_start_handler(aws, game):

    server = aws.get_server_status(game)
    templateId = aws.get_launch_template_id(game)

    if (server["status"] == "running"):
        return "Server is already running with IP: {}:9876".format(server["ip"])

    if (server["status"] == "stopped" and server["ami_id"] is not None):
        server.start_server(ec2, templateId, server["ami_id"])
        return "Server is starting."

    if (server["status"] == "stopping"):
        server.start_server(ec2, templateId, server["ami_id"])
        return "Server is shutting down. Please wait a few minutes and try again."

    if (server["status"] == "archived"):
        print("Server is archived.")
        return "Server has been archived due to inactivity."
