# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python SDK for Evolution API - a WhatsApp Business API integration library. The SDK provides a clean interface for managing WhatsApp instances, webhooks, settings, messages, and more through the Evolution API.

## Development Commands

### Testing
```bash
uv run pytest -v                 # Run all tests with verbose output
uv run pytest tests/test_client.py      # Run specific test file
uv run pytest -k test_get_success       # Run specific test by name
```

### Package Management
```bash
uv pip install -e .              # Install package in editable mode
uv sync                          # Sync dependencies with uv
```

## Project Structure (Flat Layout)

The project uses a **flat layout** structure (not a src/ layout):

```
evolution_api_sdk/
├── client.py           # Core EvolutionClient class
├── exception.py        # Custom exceptions
├── __init__.py         # Package entry point
├── models/             # Data models for requests/responses
│   ├── __init__.py
│   ├── instance.py
│   ├── webhook.py
│   ├── settings.py
│   ├── message.py
│   ├── chat.py
│   ├── profile.py
│   ├── group.py
│   ├── typebot.py
│   ├── chatwoot.py
│   ├── rabbitmq.py
│   └── websocket.py
├── service/            # Service layer (11 services)
│   ├── __init__.py
│   ├── instance.py     # InstanceService
│   ├── webhook.py      # WebhookService
│   ├── settings.py     # SettingsService
│   ├── message.py      # MessageService
│   ├── chat.py         # ChatService
│   ├── profile.py      # ProfileService
│   ├── group.py        # GroupService
│   ├── typebot.py      # TypebotService
│   ├── chatwoot.py     # ChatwootService
│   ├── rabbitmq.py     # RabbitMQService
│   └── websocket.py    # WebSocketService
├── tests/              # Test suite
│   ├── test_client.py
│   ├── test_service_instance.py
│   ├── test_service_settings.py
│   └── test_service_webhook.py
├── pyproject.toml      # Project metadata and dependencies
└── pytest.ini          # Pytest configuration (includes pythonpath = .)
```

## Architecture

### Core Client (client.py:18)
The `EvolutionClient` class is the main entry point. It:
- Handles HTTP communication with the Evolution API (GET, POST, PUT, DELETE)
- Manages authentication via API tokens in headers
- Provides centralized error handling and response processing
- Initializes 11 service modules: `instance`, `webhook`, `settings`, `message`, `chat`, `profile`, `group`, `typebot`, `chatwoot`, `rabbitmq`, `websocket`

### Service Layer Pattern
The SDK uses a service-oriented architecture where each service handles a specific domain:

**InstanceService** (service/instance.py): Manages WhatsApp instances lifecycle
- Create, connect, restart, logout, remove instances
- Check connection status and fetch instance information
- Set presence status (available/unavailable)

**MessageService** (service/message.py): Send messages
- Text, media, location, contact, reaction, poll, list, template messages

**ChatService** (service/chat.py): Chat operations
- Mark as read, archive, delete messages, find messages/chats

**ProfileService** (service/profile.py): Profile management
- Update name, status, picture, privacy settings

**GroupService** (service/group.py): Group management
- Create, update, manage members, settings, ephemeral messages

**WebhookService** (service/webhook.py): Webhook configuration
- Set webhook URLs and event subscriptions
- Retrieve current webhook configuration

**SettingsService** (service/settings.py): Instance behavior settings
- Configure call rejection, message reading, online status
- Control group behavior and history synchronization

**TypebotService**, **ChatwootService**, **RabbitMQService**, **WebSocketService**: Integration services

### Models Layer
Each service has corresponding model classes in `models/`:
- **instance.py**: `InstanceConfig`, `PresenceStatus` enum, `PresenceConfig`
- **webhook.py**: `WebhookConfig`, `WebhookEvents` enum (27 event types)
- **settings.py**: `SettingsConfig`
- **message.py**: `TextMessage`, `MediaMessage`, `LocationMessage`, etc.
- **chat.py**: `MarkAsRead`, `ArchiveChat`, `DeleteMessage`, etc.
- **profile.py**: `UpdateProfileName`, `UpdateProfileStatus`, `UpdatePrivacySettings`
- **group.py**: `CreateGroup`, `UpdateGroupSubject`, `UpdateGroupMembers`, etc.

Models use `__dict__` serialization to convert Python objects to JSON payloads.

### Exception Hierarchy (exception.py)
```
EvolutionAPIError (base)
├── EvolutionAuthenticationError (401 responses)
└── EvolutionNotFoundError (404 responses)
```

### Import Patterns (CRITICAL)

The project uses **absolute imports** due to flat layout:

**In client.py:**
```python
from exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError
from service.instance import InstanceService
from service.webhook import WebhookService
```

**In service/*.py:**
```python
from models.webhook import WebhookConfig
from models.settings import SettingsConfig
```

**In tests/*.py:**
```python
from client import EvolutionClient
from exception import EvolutionAuthenticationError
from models.webhook import WebhookConfig, WebhookEvents
from service.instance import InstanceService
```

**In test mocks (@patch decorators):**
```python
@patch('client.requests.get')  # NOT 'evolution_api_sdk.client.requests.get'
```

**NEVER use relative imports** (`.`, `..`) in this project - they will break the flat layout structure.

### pytest Configuration
The `pytest.ini` file includes `pythonpath = .` which adds the project root to Python's path, enabling absolute imports to work correctly.

### HTTP Communication
- All requests include `apikey` header for authentication
- POST requests handle both JSON data and multipart file uploads
- Response handling centralizes status code checking and error raising
- SSL verification is disabled (`verify=False` in GET requests)

## Testing Strategy
Tests use pytest with mocking (`unittest.mock`):
- Mock HTTP responses to test client behavior without API calls
- Test both success cases and error handling (401, 404, 400, 500)
- Fixtures provide reusable client instances
- 27 tests covering client methods and service operations
- All `@patch` decorators use module-level paths (e.g., `@patch('client.requests.get')`)
