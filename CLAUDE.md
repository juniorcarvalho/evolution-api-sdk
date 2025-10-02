# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python SDK for Evolution API - a WhatsApp Business API integration library. The SDK provides a clean interface for managing WhatsApp instances, webhooks, and settings through the Evolution API.

## Development Commands

### Testing
```bash
pytest                           # Run all tests
pytest tests/test_client.py      # Run specific test file
pytest -k test_get_success       # Run specific test by name
```

### Package Management
```bash
pip install -e .                 # Install in development mode
uv sync                          # Sync dependencies with uv
```

## Architecture

### Core Client (client.py:10)
The `EvolutionClient` class is the main entry point. It:
- Handles HTTP communication with the Evolution API (GET, POST, PUT, DELETE)
- Manages authentication via API tokens in headers
- Provides centralized error handling and response processing
- Initializes three service modules: `instance`, `webhook`, and `settings`

### Service Layer Pattern
The SDK uses a service-oriented architecture where each service handles a specific domain:

**InstanceService** (service/instance.py): Manages WhatsApp instances lifecycle
- Create, connect, restart, logout, remove instances
- Check connection status and fetch instance information
- Set presence status (available/unavailable)

**WebhookService** (service/webhook.py): Configures webhook endpoints
- Set webhook URLs and event subscriptions
- Retrieve current webhook configuration

**SettingsService** (service/settings.py): Manages instance behavior settings
- Configure call rejection, message reading, online status
- Control group behavior and history synchronization

### Models Layer
Each service has corresponding model classes in `models/`:
- **instance.py**: `InstanceConfig` for instance creation, `PresenceStatus` enum, `PresenceConfig`
- **webhook.py**: `WebhookConfig` for webhook setup, `WebhookEvents` enum (27 event types)
- **settings.py**: `SettingsConfig` for instance behavior configuration

Models use `__dict__` serialization to convert Python objects to JSON payloads.

### Exception Hierarchy (exception.py)
```
EvolutionAPIError (base)
├── EvolutionAuthenticationError (401 responses)
└── EvolutionNotFoundError (404 responses)
```

### Import Patterns
- Services import from `models/` for configuration classes
- Client imports from `service/` to initialize service modules
- The package uses `evolution_api_sdk` as the root module name internally
- External usage imports from top-level: `from client import EvolutionClient`

### HTTP Communication
- All requests include `apikey` header for authentication
- POST requests handle both JSON data and multipart file uploads
- Response handling centralizes status code checking and error raising
- SSL verification is disabled (`verify=False` in GET requests)

## Testing Strategy
Tests use pytest with mocking (`unittest.mock`):
- Mock HTTP responses to test client behavior without API calls
- Test both success cases and error handling
- Fixtures provide reusable client instances
