from unittest.mock import Mock

import pytest

from models.websocket import SetWebSocket
from service.websocket import WebSocketService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def websocket_service(mock_client):
    return WebSocketService(client=mock_client)


def test_set_websocket_success(websocket_service, mock_client):
    data = SetWebSocket(enabled=True)
    mock_client.post.return_value = {"websocket": {"enabled": True}}

    response = websocket_service.set_websocket("test_instance", data)

    assert response["websocket"]["enabled"] is True
    mock_client.post.assert_called_once_with(
        'websocket/set/test_instance',
        data=data.__dict__,
    )


def test_find_websocket_success(websocket_service, mock_client):
    mock_client.get.return_value = {
        "websocket": {
            "enabled": True,
            "events": ["APPLICATION_STARTUP", "MESSAGES_UPSERT"]
        }
    }

    response = websocket_service.find_websocket("test_instance")

    assert response["websocket"]["enabled"] is True
    assert len(response["websocket"]["events"]) == 2
    mock_client.get.assert_called_once_with('websocket/find/test_instance')
