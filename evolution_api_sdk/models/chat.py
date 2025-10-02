class MarkAsRead:
    def __init__(self, number: str, message_id: str):
        self.number = number
        self.messageId = message_id

class ArchiveChat:
    def __init__(self, number: str, archive: bool):
        self.number = number
        self.archive = archive

class DeleteMessage:
    def __init__(self, number: str, message_id: str):
        self.number = number
        self.messageId = message_id

class FindMessages:
    def __init__(self, number: str, count: int = 20):
        self.number = number
        self.count = count

class UpdateMessage:
    def __init__(self, number: str, message_id: str, text: str):
        self.number = number
        self.messageId = message_id
        self.text = text
<<<<<<< HEAD:models/chat.py
=======

>>>>>>> main:evolution_api_sdk/models/chat.py
