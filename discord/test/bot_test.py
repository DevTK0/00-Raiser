import pytest
from app.handlers import server
from app.settings import Game, Configs

@pytest
def test_vrising():

    # test start server
    response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    assert response == "Server is starting"

    # test starting a running server
    response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    assert response == "Server is already running"

    # test stop server
    response = stop_handler(GAME.V_RISING)
    assert response == "Server is shutting down"

    # test starting a stopping server
    response = start_handler(GAME.V_RISING, Configs[GAME.V_RISING])
    assert response == "Server is shutting down. Please wait a few minutes and try again." 

    # test stopping a stopped server
    response = stop_handler(GAME.V_RISING)
    assert response == "Server is already stopped" 

