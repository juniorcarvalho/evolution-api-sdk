from models.chatwoot import SetChatwoot

class ChatwootService:
    def __init__(self, client):
        self.client = client

    def set_chatwoot(self, instance_name: str, data: SetChatwoot):
        return self.client.post(f'chatwoot/set/{instance_name}', data=data.__dict__)

    def find_chatwoot(self, instance_name: str):
        return self.client.get(f'chatwoot/find/{instance_name}')
