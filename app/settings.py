# settings.py
import os
from enum import Enum
from dotenv import load_dotenv, find_dotenv

import logging.config
logging.config.fileConfig("app/logging.conf")

load_dotenv(find_dotenv())

DISCORD_AUTH_TOKEN = os.environ.get("DISCORD_AUTH_TOKEN")

class Game(Enum):
    V_RISING = "V Rising"
    MINECRAFT = "Minecraft"
    CORE_KEEPER = "Core Keeper"
    PALWORLD = "Palworld"

# Note that the CPU needs to be x86 for games to work
class Instance(Enum):
    # For Testing
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    # GPU
    G4DN_XLARGE = "g4dn.xlarge"

    # Budget 
    C5A_LARGE = "c5a.large" # +CPU
    R5A_LARGE = "r5a.large" # -CPU +RAM
    R6A_LARGE = "r6a.large" # +RAM
    
    # Normal 
    C5A_XLARGE = "c5a.xlarge"
    R5A_XLARGE = "r5a.xlarge"
    R6A_XLARGE = "r6a.xlarge" 

    # Performance 
    C5A_2XLARGE = "c5a.2xlarge"
    R5A_2XLARGE = "r5a.2xlarge"
    R6A_2XLARGE= "r6a.2xlarge" 

Configs = {
    Game.V_RISING: {
        "instance_type": Instance.T2_SMALL.value,
        "volume_size": 30
    },
    Game.MINECRAFT: {
        "instance_type": Instance.C5A_LARGE.value,
        "volume_size": 16
    },
    Game.CORE_KEEPER: {
        "instance_type": Instance.C5A_LARGE.value,
        "volume_size": 8
    },
    Game.PALWORLD: {
        "instance_type": Instance.C5A_XLARGE.value,
        "volume_size": 16
    }
}
