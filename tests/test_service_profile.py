from unittest.mock import Mock, patch, mock_open

import pytest

from models.profile import (
    UpdateProfileName,
    UpdateProfileStatus,
    UpdatePrivacySettings,
)
from service.profile import ProfileService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def profile_service(mock_client):
    return ProfileService(client=mock_client)


def test_fetch_business_profile_success(profile_service, mock_client):
    mock_client.post.return_value = {"name": "My Business", "description": "Business description"}

    response = profile_service.fetch_business_profile("test_instance", "5511999999999")

    assert response["name"] == "My Business"
    mock_client.post.assert_called_once_with(
        'profile/fetchBusinessProfile/test_instance',
        data={'number': '5511999999999'},
    )


def test_fetch_profile_success(profile_service, mock_client):
    mock_client.post.return_value = {"name": "John Doe", "status": "Hey there!"}

    response = profile_service.fetch_profile("test_instance", "5511999999999")

    assert response["name"] == "John Doe"
    mock_client.post.assert_called_once_with(
        'profile/fetchProfile/test_instance',
        data={'number': '5511999999999'},
    )


def test_update_profile_name_success(profile_service, mock_client):
    data = UpdateProfileName(name="New Name")
    mock_client.post.return_value = {"status": "success"}

    response = profile_service.update_profile_name("test_instance", data)

    assert response["status"] == "success"
    mock_client.post.assert_called_once_with(
        'profile/updateProfileName/test_instance',
        data=data.__dict__,
    )


def test_update_profile_status_success(profile_service, mock_client):
    data = UpdateProfileStatus(status="Available now")
    mock_client.post.return_value = {"status": "success"}

    response = profile_service.update_profile_status("test_instance", data)

    assert response["status"] == "success"
    mock_client.post.assert_called_once_with(
        'profile/updateProfileStatus/test_instance',
        data=data.__dict__,
    )


@patch("builtins.open", new_callable=mock_open, read_data=b"fake image data")
def test_update_profile_picture_success(mock_file, profile_service, mock_client):
    mock_client.put.return_value = {"status": "success"}

    response = profile_service.update_profile_picture("test_instance", "/path/to/image.jpg")

    assert response["status"] == "success"
    mock_file.assert_called_once_with("/path/to/image.jpg", 'rb')
    mock_client.put.assert_called_once()


def test_remove_profile_picture_success(profile_service, mock_client):
    mock_client.put.return_value = {"removed": True}

    response = profile_service.remove_profile_picture("test_instance")

    assert response["removed"] is True
    mock_client.put.assert_called_once_with('profile/removeProfilePicture/test_instance')


def test_fetch_privacy_settings_success(profile_service, mock_client):
    mock_client.get.return_value = {"readReceipts": "all", "profilePicture": "contacts"}

    response = profile_service.fetch_privacy_settings("test_instance")

    assert response["readReceipts"] == "all"
    mock_client.get.assert_called_once_with('profile/fetchPrivacySettings/test_instance')


def test_update_privacy_settings_success(profile_service, mock_client):
    data = UpdatePrivacySettings(setting="readReceipts", value="contacts")
    mock_client.put.return_value = {"updated": True}

    response = profile_service.update_privacy_settings("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'profile/updatePrivacySettings/test_instance',
        data=data.__dict__,
    )
