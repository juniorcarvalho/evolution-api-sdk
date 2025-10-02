<<<<<<< HEAD:service/chatwoot.py
from models.chatwoot import SetChatwoot
=======
from evolution_api_sdk.models.chatwoot import SetChatwoot
>>>>>>> main:evolution_api_sdk/service/chatwoot.py

class ChatwootService:
    def __init__(self, client):
        self.client = client

    def set_chatwoot(self, instance_name: str, data: SetChatwoot):
        return self.client.post(f'chatwoot/set/{instance_name}', data=data.__dict__)

    def find_chatwoot(self, instance_name: str):
        return self.client.get(f'chatwoot/find/{instance_name}')
<<<<<<< HEAD:service/chatwoot.py
=======

>>>>>>> main:evolution_api_sdk/service/chatwoot.py
