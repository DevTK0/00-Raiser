# settings.py
import os
from enum import Enum
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DISCORD_AUTH_TOKEN = os.environ.get("DISCORD_AUTH_TOKEN")

class Game(Enum):
    V_RISING = "V Rising"
    MINECRAFT = "Minecraft"
    CORE_KEEPER = "Core Keeper"

Configs = {
    Game.V_RISING: {
        "instance_type": "t2.micro",
        "volume_size": 30
    },
    Game.MINECRAFT: {
        "instance_type": "m1.small",
        "volume_size": 16
    },
    Game.CORE_KEEPER: {
        "instance_type": "t2.micro",
        "volume_size": 8
    }
}