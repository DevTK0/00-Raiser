import pytest
from app.handlers import core
from app.status import GAMES


@pytest.mark.asyncio
async def test_start():
    result = await core.start(GAMES.V_RISING)
    assert result == {"status": "success"}

    result = await core.start(GAMES.MINECRAFT)
    assert result == {"status": "success"}

    result = await core.start(GAMES.CORE_KEEPER)
    assert result == {"status": "success"}


@pytest.mark.asyncio
async def test_stop():
    result = await core.stop(GAMES.V_RISING)
    assert result == {"status": "success"}

    result = await core.stop(GAMES.MINECRAFT)
    assert result == {"status": "success"}

    result = await core.stop(GAMES.CORE_KEEPER)
    assert result == {"status": "success"}
