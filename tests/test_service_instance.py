from unittest.mock import Mock

import pytest

from evolution_api_sdk.exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError
from evolution_api_sdk.service.instance import InstanceService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def instance_service(mock_client):
    return InstanceService(client=mock_client)


def test_fetch_instances_success(instance_service, mock_client):
    mock_client.get.return_value = [
        {"id": 1, "name": "Instance 1"},
        {"id": 2, "name": "Instance 2"}
    ]

    response = instance_service.fetch_instances()

    assert len(response) == 2
    assert response[0]["name"] == "Instance 1"
    assert response[1]["name"] == "Instance 2"

    mock_client.get.assert_called_once_with('instance/fetchInstances/', params=None)


def test_fetch_instances_authentication_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        instance_service.fetch_instances()


def test_fetch_instances_not_found_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        instance_service.fetch_instances()


def test_fetch_instances_api_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        instance_service.fetch_instances()



def test_restart_instance_success(instance_service, mock_client):
    mock_client.put.return_value = {"instance": {"state": "open"}}

    response = instance_service.restart_instance("test_instance")

    assert response["instance"]["state"] == "open"
    mock_client.put.assert_called_once_with('instance/restart/test_instance')


def test_fetch_instances_with_name(instance_service, mock_client):
    mock_client.get.return_value = {"id": 1, "name": "test_instance"}

    response = instance_service.fetch_instances("test_instance")

    assert response["name"] == "test_instance"
    mock_client.get.assert_called_once_with('instance/fetchInstances/', params={'instanceName': 'test_instance'})


def test_remove_instance_success(instance_service, mock_client):
    mock_client.delete.return_value = {"status": "removed"}

    response = instance_service.remove_instance("test_instance")

    assert response["status"] == "removed"
    mock_client.delete.assert_called_once_with('instance/delete/test_instance')


def test_create_instance_success(instance_service, mock_client):
    config = {"instanceName": "test_instance", "qrcode": True}
    mock_client.post.return_value = {"instance": {"instanceName": "test_instance"}}

    response = instance_service.create_instance(config)

    assert response["instance"]["instanceName"] == "test_instance"
    mock_client.post.assert_called_once_with('instance/create', data=config)


def test_connect_instance_success(instance_service, mock_client):
    mock_client.get.return_value = {"status": "connected"}

    response = instance_service.connect_instance("test_instance")

    assert response["status"] == "connected"
    mock_client.get.assert_called_once_with('instance/connect/test_instance')


def test_status_instance_success(instance_service, mock_client):
    mock_client.get.return_value = {"instance": {"state": "open"}}

    response = instance_service.status_instance("test_instance")

    assert response["instance"]["state"] == "open"
    mock_client.get.assert_called_once_with('instance/connectionState/test_instance')


def test_logout_instance_success(instance_service, mock_client):
    mock_client.delete.return_value = {"status": "logged_out"}

    response = instance_service.logout_instance("test_instance")

    assert response["status"] == "logged_out"
    mock_client.delete.assert_called_once_with('instance/logout/test_instance')


def test_set_presence_success(instance_service, mock_client):
    from evolution_api_sdk.models.instance import PresenceStatus, PresenceConfig
    mock_client.post.return_value = {"presence": "available"}

    response = instance_service.set_presence("test_instance", PresenceStatus.AVAILABLE)

    assert response["presence"] == "available"
    config = PresenceConfig(PresenceStatus.AVAILABLE)
    mock_client.post.assert_called_once_with('instance/setPresence/test_instance', data=config.__dict__)

