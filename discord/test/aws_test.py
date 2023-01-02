import pytest
import asyncio
from app.handlers.aws import AWS
from app.settings import Game, Configs, Instance

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_aws_start_server():
    with AWS() as aws:
        response = aws.start_server(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
        print(response)
        assert len(response) == 1

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_aws_stop_server():
    with AWS() as aws:
        response = aws.stop_server(Game.CORE_KEEPER.value)
        print(response)
        assert len(response["TerminatingInstances"]) == 1

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_aws_wait_for_server_ip():
    with AWS() as aws:
        response = aws.start_server(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])
        print(response)
        aws.wait_for_server_ip(Game.CORE_KEEPER.value)
        
        server = aws.get_server_status(Game.CORE_KEEPER.value)
        print(server)
        assert server["ip_address"] is not None

@pytest.mark.skip(reason="Only run this test in insolation, do not run with other tests.")
def test_aws_wait_for_server_to_stop():
    with AWS() as aws:
        response = aws.start_server(Game.CORE_KEEPER.value, Configs[Game.CORE_KEEPER])

        aws.wait_for_server_ip(Game.CORE_KEEPER.value)

        response = aws.stop_server(Game.CORE_KEEPER.value)

        aws.wait_for_server_to_stop(Game.CORE_KEEPER.value)
        
        server = aws.get_server_status(Game.CORE_KEEPER.value)
        print(server)
        assert server["status"] == "stopped"