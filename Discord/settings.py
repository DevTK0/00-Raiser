# settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DISCORD_AUTH_TOKEN = os.environ.get("DISCORD_AUTH_TOKEN")
GAMING_INSTANCE_NAME = os.environ.get("GAMING_INSTANCE_NAME")
LAUNCH_TEMPLATE = os.environ.get("LAUNCH_TEMPLATE")
