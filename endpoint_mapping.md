# Mapeamento de Endpoints - Evolution API SDK

## Endpoints já implementados no SDK atual:

### InstanceService (service/instance.py)
- ✅ GET /instance/fetchInstances - `fetch_instances()`
- ✅ DELETE /instance/delete/{instance} - `remove_instance()`
- ✅ POST /instance/create - `create_instance()`
- ✅ GET /instance/connect/{instance} - `connect_instance()`
- ✅ GET /instance/connectionState/{instance} - `status_instance()`
- ✅ DELETE /instance/logout/{instance} - `logout_instance()`
- ✅ POST /instance/setPresence/{instance} - `set_presence()`
- ✅ PUT /instance/restart/{instance} - `restart_instance()`

### WebhookService (service/webhook.py)
- ✅ POST /webhook/set/{instance} - `set_webhook()`
- ✅ GET /webhook/find/{instance} - `find_webhook()`

### SettingsService (service/settings.py)
- ✅ POST /settings/set/{instance} - `set_settings()`
- ✅ GET /settings/find/{instance} - `find_settings()`

### EvolutionClient (client.py)
- ✅ GET / - `get_info()`

## Endpoints que precisam ser implementados:

### 🔄 MessageService (NOVO) - 11 endpoints
- ❌ POST /message/sendTemplate/{instance}
- ❌ POST /message/sendText/{instance}
- ❌ POST /message/sendStatus/{instance}
- ❌ POST /message/sendMedia/{instance}
- ❌ POST /message/sendWhatsAppAudio/{instance}
- ❌ POST /message/sendSticker/{instance}
- ❌ POST /message/sendLocation/{instance}
- ❌ POST /message/sendContact/{instance}
- ❌ POST /message/sendReaction/{instance}
- ❌ POST /message/sendPoll/{instance}
- ❌ POST /message/sendList/{instance}

### 🔄 ChatService (NOVO) - 11 endpoints
- ❌ POST /chat/checkIsWhatsApp/{instance}
- ❌ PUT /chat/markMessageAsRead/{instance}
- ❌ PUT /chat/archiveChat/{instance}
- ❌ DELETE /chat/deleteMessageForEveryone/{instance}
- ❌ POST /chat/sendPresence/{instance}
- ❌ POST /chat/fetchProfilePictureUrl/{instance}
- ❌ POST /chat/findContacts/{instance}
- ❌ POST /chat/findMessages/{instance}
- ❌ POST /chat/findStatusMessage/{instance}
- ❌ PUT /chat/updateMessage/{instance}
- ❌ GET /chat/findChats/{instance}

### 🔄 ProfileService (NOVO) - 8 endpoints
- ❌ POST /profile/fetchBusinessProfile/{instance}
- ❌ POST /profile/fetchProfile/{instance}
- ❌ POST /profile/updateProfileName/{instance}
- ❌ POST /profile/updateProfileStatus/{instance}
- ❌ PUT /profile/updateProfilePicture/{instance}
- ❌ PUT /profile/removeProfilePicture/{instance}
- ❌ GET /profile/fetchPrivacySettings/{instance}
- ❌ PUT /profile/updatePrivacySettings/{instance}

### 🔄 GroupService (NOVO) - 16 endpoints
- ❌ POST /group/createGroup/{instance}
- ❌ PUT /group/updateGroupPicture/{instance}
- ❌ PUT /group/updateGroupSubject/{instance}
- ❌ PUT /group/updateGroupDescription/{instance}
- ❌ GET /group/fetchInviteCode/{instance}
- ❌ GET /group/acceptInviteCode/{instance}
- ❌ PUT /group/revokeInviteCode/{instance}
- ❌ POST /group/sendGroupInvite/{instance}
- ❌ GET /group/findGroupByInviteCode/{instance}
- ❌ GET /group/findGroupByJid/{instance}
- ❌ GET /group/fetchAllGroups/{instance}
- ❌ GET /group/findGroupMembers/{instance}
- ❌ PUT /group/updateGroupMembers/{instance}
- ❌ PUT /group/updateGroupSetting/{instance}
- ❌ PUT /group/toggleEphemeral/{instance}
- ❌ DELETE /group/leaveGroup/{instance}

### 🔄 TypebotService (NOVO) - 4 endpoints
- ❌ POST /typebot/set/{instance}
- ❌ POST /typebot/start/{instance}
- ❌ GET /typebot/find/{instance}
- ❌ POST /typebot/changeStatus/{instance}

### 🔄 ChatwootService (NOVO) - 2 endpoints
- ❌ POST /chatwoot/set/{instance}
- ❌ GET /chatwoot/find/{instance}

### 🔄 SqsService (NOVO) - 2 endpoints
- ❌ POST /sqs/set/{instance}
- ❌ GET /sqs/find/{instance}

### 🔄 RabbitmqService (NOVO) - 2 endpoints
- ❌ POST /rabbitmq/set/{instance}
- ❌ GET /rabbitmq/find/{instance}

## Resumo:
- **Implementados**: 13 endpoints
- **A implementar**: 56 endpoints
- **Novos serviços**: 8 serviços
- **Novos modelos**: ~15-20 classes de modelo estimadas

## Padrão identificado:
1. Cada serviço herda o cliente no `__init__(self, client)`
2. Métodos seguem padrão snake_case
3. Parâmetros de instância sempre como `instance_name: str`
4. Uso de modelos para configurações complexas com `.__dict__` para serialização
5. Retorno direto do `self.client.{method}()`
