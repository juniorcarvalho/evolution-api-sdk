class SettingsConfig:
    def __init__(self, reject_call: bool, groups_ignore: bool, always_online: bool, read_messages: bool, read_status: bool, sync_full_history: bool, msg_call: str = None):
        self.reject_call = reject_call
        self.groups_ignore = groups_ignore
        self.always_online = always_online
        self.read_messages = read_messages
        self.read_status = read_status
        self.sync_full_history = sync_full_history
        if msg_call is not None:
            self.msg_call = msg_call

