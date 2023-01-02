import pytest
import asyncio
from app.handlers import server
from app.handlers.aws import AWS
from app.settings import Game, Configs

def test_vrising():
    # test start server
    response = server.start_handler(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
    assert response == "Server is starting."

    # test starting a running server
    response = server.start_handler(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
    assert "Server is already running."

    with AWS() as aws:
        aws.wait_for_server_ip(Game.CORE_KEEPER.value)

    # test stop server
    response = server.stop_handler(Game.CORE_KEEPER.value)
    assert response == "Server is shutting down."

    # test starting a stopping server
    response = server.start_handler(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
    assert response == "Server is shutting down. Please wait a few minutes and try again." 

    with AWS() as aws:
        aws.wait_for_server_to_stop(Game.CORE_KEEPER.value)

    # test stopping a stopped server
    response = server.stop_handler(Game.CORE_KEEPER.value)
    assert response == "Server is already stopped." 


@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_vrising_start():
    response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])
    assert response == "Server is starting."
    

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_vrising_stop():
    response = server.stop_handler(Game.V_RISING.value)
    assert response == "Server is shutting down."

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_minecraft_start():
    response = server.start_handler(Game.MINECRAFT.value, Configs[Game.MINECRAFT])
    assert response == "Server is starting."
    
@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_minecraft_stop():
    response = server.stop_handler(Game.MINECRAFT.value)
    assert response == "Server is shutting down."

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_corekeeper_start():
    response = server.start_handler(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
    assert response == "Server is starting."

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_corekeeper_stop():
    response = server.stop_handler(Game.CORE_KEEPER.value)
    assert response == "Server is shutting down."