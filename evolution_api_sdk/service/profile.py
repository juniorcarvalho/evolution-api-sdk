<<<<<<< HEAD:service/profile.py
from models.profile import (
=======
from evolution_api_sdk.models.profile import (
>>>>>>> main:evolution_api_sdk/service/profile.py
    UpdateProfileName,
    UpdateProfileStatus,
    UpdatePrivacySettings,
)

class ProfileService:
    def __init__(self, client):
        self.client = client

    def fetch_business_profile(self, instance_name: str, number: str):
        return self.client.post(f'profile/fetchBusinessProfile/{instance_name}', data={'number': number})

    def fetch_profile(self, instance_name: str, number: str):
        return self.client.post(f'profile/fetchProfile/{instance_name}', data={'number': number})

    def update_profile_name(self, instance_name: str, data: UpdateProfileName):
        return self.client.post(f'profile/updateProfileName/{instance_name}', data=data.__dict__)

    def update_profile_status(self, instance_name: str, data: UpdateProfileStatus):
        return self.client.post(f'profile/updateProfileStatus/{instance_name}', data=data.__dict__)

    def update_profile_picture(self, instance_name: str, file_path: str):
        with open(file_path, 'rb') as f:
            return self.client.put(f'profile/updateProfilePicture/{instance_name}', files={'file': ('image.jpeg', f, 'image/jpeg')})

    def remove_profile_picture(self, instance_name: str):
        return self.client.put(f'profile/removeProfilePicture/{instance_name}')

    def fetch_privacy_settings(self, instance_name: str):
        return self.client.get(f'profile/fetchPrivacySettings/{instance_name}')

    def update_privacy_settings(self, instance_name: str, data: UpdatePrivacySettings):
        return self.client.put(f'profile/updatePrivacySettings/{instance_name}', data=data.__dict__)
<<<<<<< HEAD:service/profile.py
=======

>>>>>>> main:evolution_api_sdk/service/profile.py
