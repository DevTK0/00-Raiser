from app.handlers.aws import AWS
import logging

def stop_handler(game):
    
    with AWS() as aws:
        server = aws.get_server_status(game)

        if (server["status"] == "stopping"):
            raise Exception("Server is already shutting down.")
        elif (server["status"] == "stopped" or server["status"] == "archived"):
            raise Exception("Server is already stopped.")
        elif (server["status"] == "running"):
            aws.stop_server(game)
        else:
            logging.error(f"Unknown state found for {game}. {server}")
            raise Exception("Unknown state.")

def start_handler(game, configs):

    with AWS() as aws:
        server = aws.get_server_status(game)
        
        if (server["status"] == "running"):
            raise Exception("Server is already running.")
        elif (server["status"] == "stopping"):
            raise Exception("Server is shutting down. Please wait a few minutes and try again.")
        elif (server["status"] == "archived"):
            raise Exception("Server has been archived due to inactivity.")
        elif (server["status"] == "stopped" and server["ami_id"] is not None):
            aws.start_server(game, configs)
        else:
            logging.error(f"Unknown state found for {game} with configs: {configs}. {server}")
            raise Exception("Unknown state.")

def status_handler(game):

    with AWS() as aws:
        server = aws.get_server_status(game)

        if (server["status"] == "running"):
            server["description"] = "Server is running."
            
        if (server["status"] == "stopped"):
            server["description"] = "Server is stopped."

        if (server["status"] == "stopping"):
            server["description"] = "Server is shutting down."

        if (server["status"] == "archived"):
            server["description"] = "Server has been archived due to inactivity."

    return server

def get_server_details(game):
    with AWS() as aws:
        server = aws.get_server_status(game)

        if "ip_address" in server:
            return server

        return None

def get_stop_server_status(game):
    with AWS() as aws:
        server = aws.get_server_status(game)

        if (server["status"] == "stopped"):
            return True

        return False
        