class SetTypebot:
    def __init__(self, name: str, url: str, token: str):
        self.name = name
        self.url = url
        self.token = token

class StartTypebot:
    def __init__(self, number: str, start: dict):
        self.number = number
        self.start = start

class ChangeTypebotStatus:
    def __init__(self, number: str, status: str):
        self.number = number
        self.status = status
