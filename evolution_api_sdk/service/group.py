from evolution_api_sdk.models.group import (
    CreateGroup,
    UpdateGroupSubject,
    UpdateGroupDescription,
    UpdateGroupMembers,
    UpdateGroupSetting,
)

class GroupService:
    def __init__(self, client):
        self.client = client

    def create_group(self, instance_name: str, data: CreateGroup):
        return self.client.post(f'group/createGroup/{instance_name}', data=data.__dict__)

    def update_group_picture(self, instance_name: str, group_id: str, file_path: str):
        with open(file_path, 'rb') as f:
            return self.client.put(f'group/updateGroupPicture/{instance_name}', data={'groupId': group_id}, files={'file': ('image.jpeg', f, 'image/jpeg')})

    def update_group_subject(self, instance_name: str, data: UpdateGroupSubject):
        return self.client.put(f'group/updateGroupSubject/{instance_name}', data=data.__dict__)

    def update_group_description(self, instance_name: str, data: UpdateGroupDescription):
        return self.client.put(f'group/updateGroupDescription/{instance_name}', data=data.__dict__)

    def fetch_invite_code(self, instance_name: str, group_id: str):
        return self.client.get(f'group/fetchInviteCode/{instance_name}', params={'groupId': group_id})

    def accept_invite_code(self, instance_name: str, invite_code: str):
        return self.client.get(f'group/acceptInviteCode/{instance_name}', params={'inviteCode': invite_code})

    def revoke_invite_code(self, instance_name: str, group_id: str):
        return self.client.put(f'group/revokeInviteCode/{instance_name}', data={'groupId': group_id})

    def send_group_invite(self, instance_name: str, group_id: str, number: str):
        return self.client.post(f'group/sendGroupInvite/{instance_name}', data={'groupId': group_id, 'number': number})

    def find_group_by_invite_code(self, instance_name: str, invite_code: str):
        return self.client.get(f'group/findGroupByInviteCode/{instance_name}', params={'inviteCode': invite_code})

    def find_group_by_jid(self, instance_name: str, jid: str):
        return self.client.get(f'group/findGroupByJid/{instance_name}', params={'jid': jid})

    def fetch_all_groups(self, instance_name: str):
        return self.client.get(f'group/fetchAllGroups/{instance_name}')

    def find_group_members(self, instance_name: str, group_id: str):
        return self.client.get(f'group/findGroupMembers/{instance_name}', params={'groupId': group_id})

    def update_group_members(self, instance_name: str, data: UpdateGroupMembers):
        return self.client.put(f'group/updateGroupMembers/{instance_name}', data=data.__dict__)

    def update_group_setting(self, instance_name: str, data: UpdateGroupSetting):
        return self.client.put(f'group/updateGroupSetting/{instance_name}', data=data.__dict__)

    def toggle_ephemeral(self, instance_name: str, group_id: str, is_ephemeral: bool):
        return self.client.put(f'group/toggleEphemeral/{instance_name}', data={'groupId': group_id, 'isEphemeral': is_ephemeral})

    def leave_group(self, instance_name: str, group_id: str):
        return self.client.delete(f'group/leaveGroup/{instance_name}', data={'groupId': group_id})

