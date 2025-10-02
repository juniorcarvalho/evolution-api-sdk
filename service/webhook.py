from models.webhook import WebhookConfig

class WebhookService:
    def __init__(self, client):
        self.client = client

    def set_webhook(self, instance_name: str, config: WebhookConfig):
        return self.client.post(
            f"webhook/set/{instance_name}",
            data=config.__dict__,
        )

    def find_webhook(self, instance_name: str):
        return self.client.get(f"webhook/find/{instance_name}")

