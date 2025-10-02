# -*- coding: utf-8 -*-
from enum import Enum

class Message:
    def __init__(self, number: str):
        self.number = number

class TextMessage(Message):
    def __init__(self, number: str, text: str):
        super().__init__(number)
        self.text = text

class MediaMessage(Message):
    def __init__(self, number: str, url: str, caption: str = None):
        super().__init__(number)
        self.url = url
        self.caption = caption

class LocationMessage(Message):
    def __init__(self, number: str, latitude: float, longitude: float, name: str = None, address: str = None):
        super().__init__(number)
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.address = address

class ContactMessage(Message):
    def __init__(self, number: str, contact_name: str, contact_number: str):
        super().__init__(number)
        self.contactName = contact_name
        self.contactNumber = contact_number

class ReactionMessage(Message):
    def __init__(self, number: str, message_id: str, reaction: str):
        super().__init__(number)
        self.messageId = message_id
        self.reaction = reaction

class PollMessage(Message):
    def __init__(self, number: str, poll_name: str, poll_options: list):
        super().__init__(number)
        self.pollName = poll_name
        self.pollOptions = poll_options

class ListMessage(Message):
    def __init__(self, number: str, title: str, button_text: str, description: str, sections: list):
        super().__init__(number)
        self.title = title
        self.buttonText = button_text
        self.description = description
        self.sections = sections

class TemplateMessage(Message):
    def __init__(self, number: str, template_name: str, language: str, components: list):
        super().__init__(number)
        self.templateName = template_name
        self.language = language
        self.components = components

