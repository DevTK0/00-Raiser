import pytest
from app.handlers import server
from app.settings import Game, Configs

def test_vrising():
    print ("test_vrising")
    assert Game.V_RISING.value == "V Rising"
    # # test start server
    # response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    # assert response == "Server is starting"

    # # test starting a running server
    # response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    # assert response == "Server is already running"

    # # test stop server
    # response = stop_handler(GAME.V_RISING)
    # assert response == "Server is shutting down"

    # # test starting a stopping server
    # response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    # assert response == "Server is shutting down. Please wait a few minutes and try again." 

    # # test stopping a stopped server
    # response = stop_handler(GAME.V_RISING)
    # assert response == "Server is already stopped" 


def test_vrising_start():
    response = server.start_handler(Game.V_RISING.value, Configs[Game.V_RISING])
    assert response == "Server is starting."
    

def test_vrising_stop():
    response = server.stop_handler(Game.V_RISING.value)
    assert response == "Server is shutting down."

