from unittest.mock import Mock

import pytest

from models.chatwoot import SetChatwoot
from service.chatwoot import ChatwootService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def chatwoot_service(mock_client):
    return ChatwootService(client=mock_client)


def test_set_chatwoot_success(chatwoot_service, mock_client):
    data = SetChatwoot(
        url="https://app.chatwoot.com",
        token="chatwoot_token_abc"
    )
    mock_client.post.return_value = {"chatwoot": {"enabled": True}}

    response = chatwoot_service.set_chatwoot("test_instance", data)

    assert response["chatwoot"]["enabled"] is True
    mock_client.post.assert_called_once_with(
        'chatwoot/set/test_instance',
        data=data.__dict__,
    )


def test_find_chatwoot_success(chatwoot_service, mock_client):
    mock_client.get.return_value = {
        "chatwoot": {
            "accountId": "123456",
            "url": "https://app.chatwoot.com",
            "enabled": True
        }
    }

    response = chatwoot_service.find_chatwoot("test_instance")

    assert response["chatwoot"]["enabled"] is True
    assert response["chatwoot"]["accountId"] == "123456"
    mock_client.get.assert_called_once_with('chatwoot/find/test_instance')
