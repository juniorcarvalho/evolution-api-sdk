from unittest.mock import Mock

import pytest

from models.typebot import (
    SetTypebot,
    StartTypebot,
    ChangeTypebotStatus,
)
from service.typebot import TypebotService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def typebot_service(mock_client):
    return TypebotService(client=mock_client)


def test_set_typebot_success(typebot_service, mock_client):
    data = SetTypebot(name="My Bot", url="https://typebot.io/bot123", token="my_token")
    mock_client.post.return_value = {"typebot": {"enabled": True}}

    response = typebot_service.set_typebot("test_instance", data)

    assert response["typebot"]["enabled"] is True
    mock_client.post.assert_called_once_with(
        'typebot/set/test_instance',
        data=data.__dict__,
    )


def test_start_typebot_success(typebot_service, mock_client):
    data = StartTypebot(number="5511999999999", start={"flow": "welcome"})
    mock_client.post.return_value = {"status": "started"}

    response = typebot_service.start_typebot("test_instance", data)

    assert response["status"] == "started"
    mock_client.post.assert_called_once_with(
        'typebot/start/test_instance',
        data=data.__dict__,
    )


def test_find_typebot_success(typebot_service, mock_client):
    mock_client.get.return_value = {"typebot": {"url": "https://typebot.io/bot123"}}

    response = typebot_service.find_typebot("test_instance", "5511999999999")

    assert response["typebot"]["url"] == "https://typebot.io/bot123"
    mock_client.get.assert_called_once_with(
        'typebot/find/test_instance',
        params={'number': '5511999999999'},
    )


def test_change_typebot_status_success(typebot_service, mock_client):
    data = ChangeTypebotStatus(number="5511999999999", status="paused")
    mock_client.post.return_value = {"status": "paused"}

    response = typebot_service.change_typebot_status("test_instance", data)

    assert response["status"] == "paused"
    mock_client.post.assert_called_once_with(
        'typebot/changeStatus/test_instance',
        data=data.__dict__,
    )
