from enum import Enum
from typing import List

class WebhookEvents(Enum):
    APPLICATION_STARTUP = "APPLICATION_STARTUP"
    QRCODE_UPDATED = "QRCODE_UPDATED"
    MESSAGES_SET = "MESSAGES_SET"
    MESSAGES_UPSERT = "MESSAGES_UPSERT"
    MESSAGES_UPDATE = "MESSAGES_UPDATE"
    MESSAGES_DELETE = "MESSAGES_DELETE"
    SEND_MESSAGE = "SEND_MESSAGE"
    CONTACTS_SET = "CONTACTS_SET"
    CONTACTS_UPSERT = "CONTACTS_UPSERT"
    CONTACTS_UPDATE = "CONTACTS_UPDATE"
    PRESENCE_UPDATE = "PRESENCE_UPDATE"
    CHATS_SET = "CHATS_SET"
    CHATS_UPSERT = "CHATS_UPSERT"
    CHATS_UPDATE = "CHATS_UPDATE"
    CHATS_DELETE = "CHATS_DELETE"
    GROUPS_UPSERT = "GROUPS_UPSERT"
    GROUPS_UPDATE = "GROUPS_UPDATE"
    GROUP_PARTICIPANTS_UPDATE = "GROUP_PARTICIPANTS_UPDATE"
    CONNECTION_UPDATE = "CONNECTION_UPDATE"
    CALL = "CALL"
    PRESENCE = "PRESENCE"
    TYPEBOT_START = "TYPEBOT_START"
    TYPEBOT_SEND_MESSAGE = "TYPEBOT_SEND_MESSAGE"


class WebhookConfig:
    def __init__(self, url: str, events: List[WebhookEvents], webhook_by_events: bool = None, webhook_base64: bool = None):
        self.url = url
        self.events = [event.value for event in events]
        if webhook_by_events is not None:
            self.webhook_by_events = webhook_by_events
        if webhook_base64 is not None:
            self.webhook_base64 = webhook_base64

