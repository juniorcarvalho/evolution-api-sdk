from models.websocket import SetWebSocket

class WebSocketService:
    def __init__(self, client):
        self.client = client

    def set_websocket(self, instance_name: str, data: SetWebSocket):
        return self.client.post(f'websocket/set/{instance_name}', data=data.__dict__)

    def find_websocket(self, instance_name: str):
        return self.client.get(f'websocket/find/{instance_name}')
