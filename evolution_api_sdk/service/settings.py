from evolution_api_sdk.models.settings import SettingsConfig

class SettingsService:
    def __init__(self, client):
        self.client = client

    def set_settings(self, instance_name: str, config: SettingsConfig):
        return self.client.post(
            f'settings/set/{instance_name}',
            data=config.__dict__,
        )

    def find_settings(self, instance_name: str):
        return self.client.get(f'settings/find/{instance_name}')

