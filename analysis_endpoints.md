# Análise dos Endpoints da Evolution API

## Endpoints já implementados no SDK atual:
- GET / (Get Information)
- POST /instance (Create Instance Basic)
- GET /instance/fetchInstances (Fetch Instances)
- GET /instance/connect/{instance} (Instance Connect)
- PUT /instance/restart/{instance} (Restart Instance)
- GET /instance/connectionState/{instance} (Connection State)
- DELETE /instance/logout/{instance} (Logout Instance)
- DELETE /instance/delete/{instance} (Delete Instance)
- POST /instance/setPresence/{instance} (Set Presence)
- POST /webhook/set/{instance} (Set Webhook)
- GET /webhook/find/{instance} (Find Webhook)
- POST /settings/set/{instance} (Set Settings)
- GET /settings/find/{instance} (Find Settings)

## Endpoints encontrados que precisam ser implementados:

### Send Message (Message Controller)
1. **POST /message/sendTemplate/{instance}** - Send Template
   - Envia mensagem template usando WhatsApp API oficial
   - Parâmetros: number, templateMessage (name, language, components)

## Próximos passos:
- Continuar navegando pela documentação para encontrar outros endpoints de Send Message
- Analisar Chat Controller, Profile Settings, Group Controller, Typebot, Chatwoot, RabbitMQ, WebSocket


### Send Message - Endpoints completos encontrados:
1. **POST /message/sendTemplate/{instance}** - Send Template
2. **POST /message/sendText/{instance}** - Send Plain Text  
3. **POST /message/sendStatus/{instance}** - Send Status
4. **POST /message/sendMedia/{instance}** - Send Media
5. **POST /message/sendWhatsAppAudio/{instance}** - Send WhatsApp Audio
6. **POST /message/sendSticker/{instance}** - Send Sticker
7. **POST /message/sendLocation/{instance}** - Send Location
8. **POST /message/sendContact/{instance}** - Send Contact
9. **POST /message/sendReaction/{instance}** - Send Reaction
10. **POST /message/sendPoll/{instance}** - Send Poll
11. **POST /message/sendList/{instance}** - Send List

### Chat Controller - Endpoints encontrados:
1. **POST /chat/checkIsWhatsApp/{instance}** - Check is WhatsApp
2. **PUT /chat/markMessageAsRead/{instance}** - Mark Message As Read
3. **PUT /chat/archiveChat/{instance}** - Archive Chat
4. **DELETE /chat/deleteMessageForEveryone/{instance}** - Delete Message for Everyone
5. **POST /chat/sendPresence/{instance}** - Send Presence
6. **POST /chat/fetchProfilePictureUrl/{instance}** - Fetch Profile Picture URL
7. **POST /chat/findContacts/{instance}** - Find Contacts
8. **POST /chat/findMessages/{instance}** - Find Messages

### Chat Controller - Endpoints adicionais:
9. **POST /chat/findStatusMessage/{instance}** - Find Status Message
10. **PUT /chat/updateMessage/{instance}** - Update Message
11. **GET /chat/findChats/{instance}** - Find Chats

### Profile Settings - Endpoints encontrados:
1. **POST /profile/fetchBusinessProfile/{instance}** - Fetch Business Profile
2. **POST /profile/fetchProfile/{instance}** - Fetch Profile
3. **POST /profile/updateProfileName/{instance}** - Update Profile Name
4. **POST /profile/updateProfileStatus/{instance}** - Update Profile Status
5. **PUT /profile/updateProfilePicture/{instance}** - Update Profile Picture
6. **PUT /profile/removeProfilePicture/{instance}** - Remove Profile Picture
7. **GET /profile/fetchPrivacySettings/{instance}** - Fetch Privacy Settings
8. **PUT /profile/updatePrivacySettings/{instance}** - Update Privacy Settings

### Group Controller - Endpoints encontrados:
1. **POST /group/createGroup/{instance}** - Create Group
2. **PUT /group/updateGroupPicture/{instance}** - Update Group Picture
3. **PUT /group/updateGroupSubject/{instance}** - Update Group Subject
4. **PUT /group/updateGroupDescription/{instance}** - Update Group Description

### Group Controller - Endpoints adicionais:
5. **GET /group/fetchInviteCode/{instance}** - Fetch Invite Code
6. **GET /group/acceptInviteCode/{instance}** - Accept Invite Code
7. **PUT /group/revokeInviteCode/{instance}** - Revoke Invite Code
8. **POST /group/sendGroupInvite/{instance}** - Send Group Invite
9. **GET /group/findGroupByInviteCode/{instance}** - Find Group by Invite Code
10. **GET /group/findGroupByJid/{instance}** - Find Group by JID
11. **GET /group/fetchAllGroups/{instance}** - Fetch All Groups
12. **GET /group/findGroupMembers/{instance}** - Find Group Members
13. **PUT /group/updateGroupMembers/{instance}** - Update Group Members
14. **PUT /group/updateGroupSetting/{instance}** - Update Group Setting
15. **PUT /group/toggleEphemeral/{instance}** - Toggle Ephemeral
16. **DELETE /group/leaveGroup/{instance}** - Leave Group

### Typebot - Endpoints encontrados:
1. **POST /typebot/set/{instance}** - Set Typebot
2. **POST /typebot/start/{instance}** - Start Typebot
3. **GET /typebot/find/{instance}** - Find Typebot
4. **POST /typebot/changeStatus/{instance}** - Change Typebot Status

### Chatwoot - Endpoints encontrados:
1. **POST /chatwoot/set/{instance}** - Set Chatwoot

### Chatwoot - Endpoints completos:
1. **POST /chatwoot/set/{instance}** - Set Chatwoot
2. **GET /chatwoot/find/{instance}** - Find Chatwoot

### SQS - Endpoints encontrados:
1. **POST /sqs/set/{instance}** - Set SQS
2. **GET /sqs/find/{instance}** - Find SQS

### RabbitMQ - Endpoints encontrados:
1. **POST /rabbitmq/set/{instance}** - Set RabbitMQ
2. **GET /rabbitmq/find/{instance}** - Find RabbitMQ

### WebSocket - Endpoints encontrados:
1. **GET /websocket/find/{instance}** - Find Chatwoot (parece ser um endpoint duplicado)
2. **POST /websocket/set/{instance}** - Set Chatwoot (parece ser um endpoint duplicado)

## Resumo dos endpoints a implementar:
- **Send Message**: 11 endpoints
- **Chat Controller**: 11 endpoints  
- **Profile Settings**: 8 endpoints
- **Group Controller**: 16 endpoints
- **Typebot**: 4 endpoints
- **Chatwoot**: 2 endpoints
- **SQS**: 2 endpoints
- **RabbitMQ**: 2 endpoints
- **WebSocket**: 2 endpoints (possivelmente duplicados)

**Total**: ~58 novos endpoints para implementar
