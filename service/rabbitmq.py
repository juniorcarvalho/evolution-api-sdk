from models.rabbitmq import SetRabbitMQ

class RabbitMQService:
    def __init__(self, client):
        self.client = client

    def set_rabbitmq(self, instance_name: str, data: SetRabbitMQ):
        return self.client.post(f'rabbitmq/set/{instance_name}', data=data.__dict__)

    def find_rabbitmq(self, instance_name: str):
        return self.client.get(f'rabbitmq/find/{instance_name}')
