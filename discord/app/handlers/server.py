import asyncio
from app.handlers.aws import AWS

def stop_handler(game):
    
    with AWS() as aws:
        server = aws.get_server_status(game)

        if (server["status"] == "running" or server["status"] == "stopping"):
            aws.stop_server(game)
            return "Server is shutting down."

        if (server["status"] == "stopped" or server["status"] == "archived"):
            return "Server is already stopped."

def start_handler(game, configs):

    with AWS() as aws:
        server = aws.get_server_status(game)
        
        if (server["status"] == "running"):
            return "Server is already running."

        if (server["status"] == "stopped" and server["ami_id"] is not None):
            aws.start_server(game, configs)
            return "Server is starting."

        if (server["status"] == "stopping"):
            return "Server is shutting down. Please wait a few minutes and try again."

        if (server["status"] == "archived"):
            return "Server has been archived due to inactivity."


def get_ip_address(game):
    with AWS() as aws:
        server = aws.get_server_status(game)

        if "ip_address" in server:
            return server["ip_address"]

        return None