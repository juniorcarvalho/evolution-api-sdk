from unittest.mock import Mock

import pytest

from models.settings import SettingsConfig
from service.settings import SettingsService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def settings_service(mock_client):
    return SettingsService(client=mock_client)


def test_set_settings_success(settings_service, mock_client):
    config = SettingsConfig(reject_call=True, groups_ignore=True, always_online=True, read_messages=True, read_status=True, sync_full_history=False)
    mock_client.post.return_value = {"settings": {"reject_call": True}}

    response = settings_service.set_settings("test_instance", config)

    assert response["settings"]["reject_call"] is True
    mock_client.post.assert_called_once_with(
        'settings/set/test_instance',
        data=config.__dict__,
    )

def test_find_settings_success(settings_service, mock_client):
    mock_client.get.return_value = {"reject_call": True}

    response = settings_service.find_settings("test_instance")

    assert response["reject_call"] is True
    mock_client.get.assert_called_once_with('settings/find/test_instance')

