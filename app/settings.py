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

class Instance(Enum):
    # For Testing
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    # GPU
    G4DN_XLARGE = "g4dn.xlarge"
    # Budget 
    M5A_LARGE = "m5a.large"
    M5A_XLARGE = "m5a.xlarge"
    C5A_LARGE = "c5a.large"
    C5A_XLARGE = "c5a.xlarge"
    # Normal
    M5N_LARGE = "m5n.large"
    M5N_XLARGE = "m5n.xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"
    # Performance
    M5ZN_LARGE = "m5zn.large"
    M5ZN_XLARGE = "m5zn.xlarge"
    C5N_LARGE = "c5n.large"
    C5N_XLARGE = "c5n.xlarge"

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
        "instance_type": Instance.T2_SMALL.value,
        "volume_size": 8
    }
}