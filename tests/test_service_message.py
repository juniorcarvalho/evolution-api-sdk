from unittest.mock import Mock

import pytest

from models.message import (
    TextMessage,
    MediaMessage,
    LocationMessage,
    ContactMessage,
    ReactionMessage,
    PollMessage,
    ListMessage,
    TemplateMessage,
)
from service.message import MessageService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def message_service(mock_client):
    return MessageService(client=mock_client)


def test_send_text_success(message_service, mock_client):
    data = TextMessage(number="5511999999999", text="Hello World")
    mock_client.post.return_value = {"key": {"id": "123"}}

    response = message_service.send_text("test_instance", data)

    assert response["key"]["id"] == "123"
    mock_client.post.assert_called_once_with(
        'message/sendText/test_instance',
        data=data.__dict__,
    )


def test_send_media_success(message_service, mock_client):
    data = MediaMessage(number="5511999999999", url="https://example.com/image.jpg")
    mock_client.post.return_value = {"key": {"id": "456"}}

    response = message_service.send_media("test_instance", data)

    assert response["key"]["id"] == "456"
    mock_client.post.assert_called_once_with(
        'message/sendMedia/test_instance',
        data=data.__dict__,
    )


def test_send_whatsapp_audio_success(message_service, mock_client):
    data = MediaMessage(number="5511999999999", url="https://example.com/audio.mp3")
    mock_client.post.return_value = {"key": {"id": "789"}}

    response = message_service.send_whatsapp_audio("test_instance", data)

    assert response["key"]["id"] == "789"
    mock_client.post.assert_called_once_with(
        'message/sendWhatsAppAudio/test_instance',
        data=data.__dict__,
    )


def test_send_sticker_success(message_service, mock_client):
    data = MediaMessage(number="5511999999999", url="https://example.com/sticker.webp")
    mock_client.post.return_value = {"key": {"id": "321"}}

    response = message_service.send_sticker("test_instance", data)

    assert response["key"]["id"] == "321"
    mock_client.post.assert_called_once_with(
        'message/sendSticker/test_instance',
        data=data.__dict__,
    )


def test_send_location_success(message_service, mock_client):
    data = LocationMessage(number="5511999999999", latitude=-23.5505, longitude=-46.6333)
    mock_client.post.return_value = {"key": {"id": "654"}}

    response = message_service.send_location("test_instance", data)

    assert response["key"]["id"] == "654"
    mock_client.post.assert_called_once_with(
        'message/sendLocation/test_instance',
        data=data.__dict__,
    )


def test_send_contact_success(message_service, mock_client):
    data = ContactMessage(number="5511999999999", contact_name="John Doe", contact_number="5511888888888")
    mock_client.post.return_value = {"key": {"id": "987"}}

    response = message_service.send_contact("test_instance", data)

    assert response["key"]["id"] == "987"
    mock_client.post.assert_called_once_with(
        'message/sendContact/test_instance',
        data=data.__dict__,
    )


def test_send_reaction_success(message_service, mock_client):
    data = ReactionMessage(number="5511999999999", message_id="message_key_123", reaction="👍")
    mock_client.post.return_value = {"status": "success"}

    response = message_service.send_reaction("test_instance", data)

    assert response["status"] == "success"
    mock_client.post.assert_called_once_with(
        'message/sendReaction/test_instance',
        data=data.__dict__,
    )


def test_send_poll_success(message_service, mock_client):
    data = PollMessage(number="5511999999999", poll_name="Test Poll", poll_options=["Option 1", "Option 2"])
    mock_client.post.return_value = {"key": {"id": "111"}}

    response = message_service.send_poll("test_instance", data)

    assert response["key"]["id"] == "111"
    mock_client.post.assert_called_once_with(
        'message/sendPoll/test_instance',
        data=data.__dict__,
    )


def test_send_list_success(message_service, mock_client):
    data = ListMessage(number="5511999999999", title="Menu", button_text="Select", description="Choose an option", sections=[])
    mock_client.post.return_value = {"key": {"id": "222"}}

    response = message_service.send_list("test_instance", data)

    assert response["key"]["id"] == "222"
    mock_client.post.assert_called_once_with(
        'message/sendList/test_instance',
        data=data.__dict__,
    )


def test_send_template_success(message_service, mock_client):
    data = TemplateMessage(number="5511999999999", template_name="hello_world", language="en", components=[])
    mock_client.post.return_value = {"key": {"id": "333"}}

    response = message_service.send_template("test_instance", data)

    assert response["key"]["id"] == "333"
    mock_client.post.assert_called_once_with(
        'message/sendTemplate/test_instance',
        data=data.__dict__,
    )
