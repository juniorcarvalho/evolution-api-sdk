from unittest.mock import Mock

import pytest

from models.webhook import WebhookConfig, WebhookEvents
from service.webhook import WebhookService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def webhook_service(mock_client):
    return WebhookService(client=mock_client)


def test_set_webhook_success(webhook_service, mock_client):
    config = WebhookConfig(url="http://test.com", events=[WebhookEvents.APPLICATION_STARTUP])
    mock_client.post.return_value = {"webhook": {"enabled": True}}

    response = webhook_service.set_webhook("test_instance", config)

    assert response["webhook"]["enabled"] is True
    mock_client.post.assert_called_once_with(
        'webhook/set/test_instance',
        data=config.__dict__,
    )

def test_find_webhook_success(webhook_service, mock_client):
    mock_client.get.return_value = {"enabled": True, "url": "http://test.com"}

    response = webhook_service.find_webhook("test_instance")

    assert response["enabled"] is True
    assert response["url"] == "http://test.com"
    mock_client.get.assert_called_once_with('webhook/find/test_instance')

