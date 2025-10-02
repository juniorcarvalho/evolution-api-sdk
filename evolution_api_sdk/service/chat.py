<<<<<<< HEAD:service/chat.py
from models.chat import (
=======
from evolution_api_sdk.models.chat import (
>>>>>>> main:evolution_api_sdk/service/chat.py
    MarkAsRead,
    ArchiveChat,
    DeleteMessage,
    FindMessages,
    UpdateMessage,
)

class ChatService:
    def __init__(self, client):
        self.client = client

    def check_is_whatsapp(self, instance_name: str, number: str):
        return self.client.post(f'chat/checkIsWhatsApp/{instance_name}', data={'number': number})

    def mark_message_as_read(self, instance_name: str, data: MarkAsRead):
        return self.client.put(f'chat/markMessageAsRead/{instance_name}', data=data.__dict__)

    def archive_chat(self, instance_name: str, data: ArchiveChat):
        return self.client.put(f'chat/archiveChat/{instance_name}', data=data.__dict__)

    def delete_message_for_everyone(self, instance_name: str, data: DeleteMessage):
        return self.client.delete(f'chat/deleteMessageForEveryone/{instance_name}', data=data.__dict__)

    def send_presence(self, instance_name: str, number: str, presence: str):
        return self.client.post(f'chat/sendPresence/{instance_name}', data={'number': number, 'presence': presence})

    def fetch_profile_picture_url(self, instance_name: str, number: str):
        return self.client.post(f'chat/fetchProfilePictureUrl/{instance_name}', data={'number': number})

    def find_contacts(self, instance_name: str, number: str):
        return self.client.post(f'chat/findContacts/{instance_name}', data={'number': number})

    def find_messages(self, instance_name: str, data: FindMessages):
        return self.client.post(f'chat/findMessages/{instance_name}', data=data.__dict__)

    def find_status_message(self, instance_name: str, number: str):
        return self.client.post(f'chat/findStatusMessage/{instance_name}', data={'number': number})

    def update_message(self, instance_name: str, data: UpdateMessage):
        return self.client.put(f'chat/updateMessage/{instance_name}', data=data.__dict__)

    def find_chats(self, instance_name: str):
        return self.client.get(f'chat/findChats/{instance_name}')
<<<<<<< HEAD:service/chat.py
=======

>>>>>>> main:evolution_api_sdk/service/chat.py
