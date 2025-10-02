from unittest.mock import Mock

import pytest

from models.rabbitmq import SetRabbitMQ
from service.rabbitmq import RabbitMQService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def rabbitmq_service(mock_client):
    return RabbitMQService(client=mock_client)


def test_set_rabbitmq_success(rabbitmq_service, mock_client):
    data = SetRabbitMQ(
        uri="amqp://localhost",
        queue="evolution_queue"
    )
    mock_client.post.return_value = {"rabbitmq": {"enabled": True}}

    response = rabbitmq_service.set_rabbitmq("test_instance", data)

    assert response["rabbitmq"]["enabled"] is True
    mock_client.post.assert_called_once_with(
        'rabbitmq/set/test_instance',
        data=data.__dict__,
    )


def test_find_rabbitmq_success(rabbitmq_service, mock_client):
    mock_client.get.return_value = {
        "rabbitmq": {
            "enabled": True,
            "events": ["APPLICATION_STARTUP", "MESSAGES_UPSERT"]
        }
    }

    response = rabbitmq_service.find_rabbitmq("test_instance")

    assert response["rabbitmq"]["enabled"] is True
    assert len(response["rabbitmq"]["events"]) == 2
    mock_client.get.assert_called_once_with('rabbitmq/find/test_instance')
