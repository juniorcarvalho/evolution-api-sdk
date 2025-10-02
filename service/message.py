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

class MessageService:
    def __init__(self, client):
        self.client = client

    def send_text(self, instance_name: str, data: TextMessage):
        return self.client.post(f'message/sendText/{instance_name}', data=data.__dict__)

    def send_media(self, instance_name: str, data: MediaMessage):
        return self.client.post(f'message/sendMedia/{instance_name}', data=data.__dict__)

    def send_whatsapp_audio(self, instance_name: str, data: MediaMessage):
        return self.client.post(f'message/sendWhatsAppAudio/{instance_name}', data=data.__dict__)

    def send_sticker(self, instance_name: str, data: MediaMessage):
        return self.client.post(f'message/sendSticker/{instance_name}', data=data.__dict__)

    def send_location(self, instance_name: str, data: LocationMessage):
        return self.client.post(f'message/sendLocation/{instance_name}', data=data.__dict__)

    def send_contact(self, instance_name: str, data: ContactMessage):
        return self.client.post(f'message/sendContact/{instance_name}', data=data.__dict__)

    def send_reaction(self, instance_name: str, data: ReactionMessage):
        return self.client.post(f'message/sendReaction/{instance_name}', data=data.__dict__)

    def send_poll(self, instance_name: str, data: PollMessage):
        return self.client.post(f'message/sendPoll/{instance_name}', data=data.__dict__)

    def send_list(self, instance_name: str, data: ListMessage):
        return self.client.post(f'message/sendList/{instance_name}', data=data.__dict__)

    def send_template(self, instance_name: str, data: TemplateMessage):
        return self.client.post(f'message/sendTemplate/{instance_name}', data=data.__dict__)
