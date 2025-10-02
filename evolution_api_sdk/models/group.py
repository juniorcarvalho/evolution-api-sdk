class CreateGroup:
    def __init__(self, subject: str, participants: list):
        self.subject = subject
        self.participants = participants

class UpdateGroupSubject:
    def __init__(self, group_id: str, subject: str):
        self.groupId = group_id
        self.subject = subject

class UpdateGroupDescription:
    def __init__(self, group_id: str, description: str):
        self.groupId = group_id
        self.description = description

class UpdateGroupMembers:
    def __init__(self, group_id: str, participants: list, action: str):
        self.groupId = group_id
        self.participants = participants
        self.action = action

class UpdateGroupSetting:
    def __init__(self, group_id: str, setting: str, value: bool):
        self.groupId = group_id
        self.setting = setting
        self.value = value
<<<<<<< HEAD:models/group.py
=======

>>>>>>> main:evolution_api_sdk/models/group.py
