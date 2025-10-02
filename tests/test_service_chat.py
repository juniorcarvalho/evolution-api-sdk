from unittest.mock import Mock

import pytest

from models.chat import (
    MarkAsRead,
    ArchiveChat,
    DeleteMessage,
    FindMessages,
    UpdateMessage,
)
from service.chat import ChatService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def chat_service(mock_client):
    return ChatService(client=mock_client)


def test_check_is_whatsapp_success(chat_service, mock_client):
    mock_client.post.return_value = {"exists": True}

    response = chat_service.check_is_whatsapp("test_instance", "5511999999999")

    assert response["exists"] is True
    mock_client.post.assert_called_once_with(
        'chat/checkIsWhatsApp/test_instance',
        data={'number': '5511999999999'},
    )


def test_mark_message_as_read_success(chat_service, mock_client):
    data = MarkAsRead(number="5511999999999", message_id="msg_123")
    mock_client.put.return_value = {"status": "success"}

    response = chat_service.mark_message_as_read("test_instance", data)

    assert response["status"] == "success"
    mock_client.put.assert_called_once_with(
        'chat/markMessageAsRead/test_instance',
        data=data.__dict__,
    )


def test_archive_chat_success(chat_service, mock_client):
    data = ArchiveChat(number="5511999999999", archive=True)
    mock_client.put.return_value = {"archived": True}

    response = chat_service.archive_chat("test_instance", data)

    assert response["archived"] is True
    mock_client.put.assert_called_once_with(
        'chat/archiveChat/test_instance',
        data=data.__dict__,
    )


def test_delete_message_for_everyone_success(chat_service, mock_client):
    data = DeleteMessage(number="5511999999999", message_id="msg_123")
    mock_client.delete.return_value = {"deleted": True}

    response = chat_service.delete_message_for_everyone("test_instance", data)

    assert response["deleted"] is True
    mock_client.delete.assert_called_once_with(
        'chat/deleteMessageForEveryone/test_instance',
        data=data.__dict__,
    )


def test_send_presence_success(chat_service, mock_client):
    mock_client.post.return_value = {"status": "success"}

    response = chat_service.send_presence("test_instance", "5511999999999", "available")

    assert response["status"] == "success"
    mock_client.post.assert_called_once_with(
        'chat/sendPresence/test_instance',
        data={'number': '5511999999999', 'presence': 'available'},
    )


def test_fetch_profile_picture_url_success(chat_service, mock_client):
    mock_client.post.return_value = {"profilePictureUrl": "https://example.com/pic.jpg"}

    response = chat_service.fetch_profile_picture_url("test_instance", "5511999999999")

    assert response["profilePictureUrl"] == "https://example.com/pic.jpg"
    mock_client.post.assert_called_once_with(
        'chat/fetchProfilePictureUrl/test_instance',
        data={'number': '5511999999999'},
    )


def test_find_contacts_success(chat_service, mock_client):
    mock_client.post.return_value = {"contacts": [{"name": "John Doe"}]}

    response = chat_service.find_contacts("test_instance", "5511999999999")

    assert len(response["contacts"]) == 1
    mock_client.post.assert_called_once_with(
        'chat/findContacts/test_instance',
        data={'number': '5511999999999'},
    )


def test_find_messages_success(chat_service, mock_client):
    data = FindMessages(number="5511999999999", count=10)
    mock_client.post.return_value = {"messages": []}

    response = chat_service.find_messages("test_instance", data)

    assert "messages" in response
    mock_client.post.assert_called_once_with(
        'chat/findMessages/test_instance',
        data=data.__dict__,
    )


def test_find_status_message_success(chat_service, mock_client):
    mock_client.post.return_value = {"status": "active"}

    response = chat_service.find_status_message("test_instance", "5511999999999")

    assert response["status"] == "active"
    mock_client.post.assert_called_once_with(
        'chat/findStatusMessage/test_instance',
        data={'number': '5511999999999'},
    )


def test_update_message_success(chat_service, mock_client):
    data = UpdateMessage(number="5511999999999", message_id="msg_123", text="Updated text")
    mock_client.put.return_value = {"updated": True}

    response = chat_service.update_message("test_instance", data)

    assert response["updated"] is True
    mock_client.put.assert_called_once_with(
        'chat/updateMessage/test_instance',
        data=data.__dict__,
    )


def test_find_chats_success(chat_service, mock_client):
    mock_client.get.return_value = {"chats": [{"id": "chat_1"}, {"id": "chat_2"}]}

    response = chat_service.find_chats("test_instance")

    assert len(response["chats"]) == 2
    mock_client.get.assert_called_once_with('chat/findChats/test_instance')
