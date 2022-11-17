from ..status import Game, GAMES

games = {
    GAMES.V_RISING: Game(GAMES.V_RISING),
    GAMES.MINECRAFT: Game(GAMES.MINECRAFT),
    GAMES.CORE_KEEPER: Game(GAMES.CORE_KEEPER),
}


async def start(name=""):
    game = games[name]
    if game.expired():
        game.launch()
        return {"status": "success"}
    else:
        return {"status": "failure", "message": "Game is already running"}


async def stop(name=""):
    game = games[name]
    if game.expired():
        return {"status": "failure", "message": "Game is not running"}
    else:
        game.terminate()
        return {"status": "success"}
