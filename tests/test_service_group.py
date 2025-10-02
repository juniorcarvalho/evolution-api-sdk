from unittest.mock import Mock, patch, mock_open

import pytest

from models.group import (
    CreateGroup,
    UpdateGroupSubject,
    UpdateGroupDescription,
    UpdateGroupMembers,
    UpdateGroupSetting,
)
from service.group import GroupService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def group_service(mock_client):
    return GroupService(client=mock_client)


def test_create_group_success(group_service, mock_client):
    data = CreateGroup(subject="Test Group", participants=["5511999999999"])
    mock_client.post.return_value = {"groupId": "123456@g.us"}

    response = group_service.create_group("test_instance", data)

    assert response["groupId"] == "123456@g.us"
    mock_client.post.assert_called_once_with(
        'group/createGroup/test_instance',
        data=data.__dict__,
    )


@patch("builtins.open", new_callable=mock_open, read_data=b"fake image data")
def test_update_group_picture_success(mock_file, group_service, mock_client):
    mock_client.put.return_value = {"status": "success"}

    response = group_service.update_group_picture("test_instance", "123456@g.us", "/path/to/image.jpg")

    assert response["status"] == "success"
    mock_file.assert_called_once_with("/path/to/image.jpg", 'rb')


def test_update_group_subject_success(group_service, mock_client):
    data = UpdateGroupSubject(group_id="123456@g.us", subject="New Subject")
    mock_client.put.return_value = {"updated": True}

    response = group_service.update_group_subject("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'group/updateGroupSubject/test_instance',
        data=data.__dict__,
    )


def test_update_group_description_success(group_service, mock_client):
    data = UpdateGroupDescription(group_id="123456@g.us", description="New Description")
    mock_client.put.return_value = {"updated": True}

    response = group_service.update_group_description("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'group/updateGroupDescription/test_instance',
        data=data.__dict__,
    )


def test_fetch_invite_code_success(group_service, mock_client):
    mock_client.get.return_value = {"inviteCode": "ABC123XYZ"}

    response = group_service.fetch_invite_code("test_instance", "123456@g.us")

    assert response["inviteCode"] == "ABC123XYZ"
    mock_client.get.assert_called_once_with(
        'group/fetchInviteCode/test_instance',
        params={'groupId': '123456@g.us'},
    )


def test_accept_invite_code_success(group_service, mock_client):
    mock_client.get.return_value = {"joined": True}

    response = group_service.accept_invite_code("test_instance", "ABC123XYZ")

    assert response["joined"] is True
    mock_client.get.assert_called_once_with(
        'group/acceptInviteCode/test_instance',
        params={'inviteCode': 'ABC123XYZ'},
    )


def test_revoke_invite_code_success(group_service, mock_client):
    mock_client.put.return_value = {"revoked": True}

    response = group_service.revoke_invite_code("test_instance", "123456@g.us")

    assert response["revoked"] is True
    mock_client.put.assert_called_once_with(
        'group/revokeInviteCode/test_instance',
        data={'groupId': '123456@g.us'},
    )


def test_send_group_invite_success(group_service, mock_client):
    mock_client.post.return_value = {"sent": True}

    response = group_service.send_group_invite("test_instance", "123456@g.us", "5511999999999")

    assert response["sent"] is True
    mock_client.post.assert_called_once_with(
        'group/sendGroupInvite/test_instance',
        data={'groupId': '123456@g.us', 'number': '5511999999999'},
    )


def test_find_group_by_invite_code_success(group_service, mock_client):
    mock_client.get.return_value = {"group": {"id": "123456@g.us", "subject": "Test Group"}}

    response = group_service.find_group_by_invite_code("test_instance", "ABC123XYZ")

    assert response["group"]["id"] == "123456@g.us"
    mock_client.get.assert_called_once_with(
        'group/findGroupByInviteCode/test_instance',
        params={'inviteCode': 'ABC123XYZ'},
    )


def test_find_group_by_jid_success(group_service, mock_client):
    mock_client.get.return_value = {"group": {"id": "123456@g.us"}}

    response = group_service.find_group_by_jid("test_instance", "123456@g.us")

    assert response["group"]["id"] == "123456@g.us"
    mock_client.get.assert_called_once_with(
        'group/findGroupByJid/test_instance',
        params={'jid': '123456@g.us'},
    )


def test_fetch_all_groups_success(group_service, mock_client):
    mock_client.get.return_value = {"groups": [{"id": "group1"}, {"id": "group2"}]}

    response = group_service.fetch_all_groups("test_instance")

    assert len(response["groups"]) == 2
    mock_client.get.assert_called_once_with('group/fetchAllGroups/test_instance')


def test_find_group_members_success(group_service, mock_client):
    mock_client.get.return_value = {"members": [{"id": "member1"}, {"id": "member2"}]}

    response = group_service.find_group_members("test_instance", "123456@g.us")

    assert len(response["members"]) == 2
    mock_client.get.assert_called_once_with(
        'group/findGroupMembers/test_instance',
        params={'groupId': '123456@g.us'},
    )


def test_update_group_members_success(group_service, mock_client):
    data = UpdateGroupMembers(group_id="123456@g.us", participants=["5511888888888"], action="add")
    mock_client.put.return_value = {"updated": True}

    response = group_service.update_group_members("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'group/updateGroupMembers/test_instance',
        data=data.__dict__,
    )


def test_update_group_setting_success(group_service, mock_client):
    data = UpdateGroupSetting(group_id="123456@g.us", setting="announcement", value=True)
    mock_client.put.return_value = {"updated": True}

    response = group_service.update_group_setting("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'group/updateGroupSetting/test_instance',
        data=data.__dict__,
    )


def test_toggle_ephemeral_success(group_service, mock_client):
    mock_client.put.return_value = {"ephemeral": True}

    response = group_service.toggle_ephemeral("test_instance", "123456@g.us", True)

    assert response["ephemeral"] is True
    mock_client.put.assert_called_once_with(
        'group/toggleEphemeral/test_instance',
        data={'groupId': '123456@g.us', 'isEphemeral': True},
    )


def test_leave_group_success(group_service, mock_client):
    mock_client.delete.return_value = {"left": True}

    response = group_service.leave_group("test_instance", "123456@g.us")

    assert response["left"] is True
    mock_client.delete.assert_called_once_with(
        'group/leaveGroup/test_instance',
        data={'groupId': '123456@g.us'},
    )
