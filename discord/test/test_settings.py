import pytest
from app.settings import Game, Configs

def test_vrising_configs():
    assert Configs[Game.V_RISING]["instance_type"] == "t2.micro"
    assert Configs[Game.V_RISING]["volume_size"] == 30

def test_minecraft_configs():
    assert Configs[Game.MINECRAFT]["instance_type"] == "m1.small"
    assert Configs[Game.MINECRAFT]["volume_size"] == 16

def test_corekeeper_configs():
    assert Configs[Game.CORE_KEEPER]["instance_type"] == "t2.micro"
    assert Configs[Game.CORE_KEEPER]["volume_size"] == 8