from evolution_api_sdk.models.typebot import (
    SetTypebot,
    StartTypebot,
    ChangeTypebotStatus,
)

class TypebotService:
    def __init__(self, client):
        self.client = client

    def set_typebot(self, instance_name: str, data: SetTypebot):
        return self.client.post(f'typebot/set/{instance_name}', data=data.__dict__)

    def start_typebot(self, instance_name: str, data: StartTypebot):
        return self.client.post(f'typebot/start/{instance_name}', data=data.__dict__)

    def find_typebot(self, instance_name: str, number: str):
        return self.client.get(f'typebot/find/{instance_name}', params={'number': number})

    def change_typebot_status(self, instance_name: str, data: ChangeTypebotStatus):
        return self.client.post(f'typebot/changeStatus/{instance_name}', data=data.__dict__)

