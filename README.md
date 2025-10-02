# Evolution API SDK

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

SDK Python completo para integração com a [Evolution API](https://doc.evolution-api.com) - Solução robusta para automação do WhatsApp Business.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Recursos](#recursos)
- [Instalação](#instalação)
- [Início Rápido](#início-rápido)
- [Documentação Completa](#documentação-completa)
  - [Gerenciamento de Instâncias](#gerenciamento-de-instâncias)
  - [Envio de Mensagens](#envio-de-mensagens)
  - [Gerenciamento de Chats](#gerenciamento-de-chats)
  - [Gerenciamento de Perfil](#gerenciamento-de-perfil)
  - [Gerenciamento de Grupos](#gerenciamento-de-grupos)
  - [Webhooks](#webhooks)
  - [Configurações](#configurações)
  - [Integrações](#integrações)
- [Tratamento de Erros](#tratamento-de-erros)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Suporte](#suporte)

## 🚀 Sobre o Projeto

O **Evolution API SDK** é uma biblioteca Python completa que facilita a integração com a Evolution API, oferecendo uma interface intuitiva e type-safe para todas as funcionalidades da API do WhatsApp Business.

## 🎯 Recursos

### Serviços Disponíveis

| Serviço | Descrição | Principais Funcionalidades |
|---------|-----------|---------------------------|
| **Instance** | Gerenciamento de instâncias WhatsApp | Criar, conectar, desconectar, reiniciar, status |
| **Message** | Envio de mensagens | Texto, mídia, áudio, localização, contatos, enquetes, listas |
| **Chat** | Gerenciamento de conversas | Marcar como lido, arquivar, deletar, buscar mensagens |
| **Profile** | Gerenciamento de perfil | Atualizar nome, status, foto, configurações de privacidade |
| **Group** | Gerenciamento de grupos | Criar, atualizar, gerenciar membros, configurações |
| **Webhook** | Configuração de webhooks | Definir URLs e eventos de notificação |
| **Settings** | Configurações da instância | Rejeitar chamadas, modo sempre online, leitura automática |
| **Typebot** | Integração com Typebot | Configurar e gerenciar bots conversacionais |
| **Chatwoot** | Integração com Chatwoot | Conectar com plataforma de atendimento |
| **RabbitMQ** | Integração com RabbitMQ | Configurar fila de mensagens |
| **WebSocket** | Conexão WebSocket | Estabelecer conexão em tempo real |

## 📦 Instalação

### Requisitos

- Python 3.13 ou superior
- pip ou uv (gerenciador de pacotes)

### Via pip (recomendado)

```bash
pip install evolution-api-sdk
```

### Via uv (mais rápido)

```bash
uv pip install evolution-api-sdk
```

### Instalação para Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
cd evolution-api-sdk

# Instale em modo editável
pip install -e .

# Ou com uv
uv pip install -e .
```

## ⚡ Início Rápido

```python
from client import EvolutionClient
from models.instance import InstanceConfig
from models.message import TextMessage

# 1. Inicialize o cliente
client = EvolutionClient(
    base_url="https://sua-evolution-api.com",
    api_token="sua-chave-de-api"
)

# 2. Crie uma instância
config = InstanceConfig(
    instanceName="minha-instancia",
    qrcode=True
)
client.instance.create_instance(config.__dict__)

# 3. Envie uma mensagem
message = TextMessage(
    number="5511999999999",
    text="Olá! Esta é uma mensagem enviada via Evolution API SDK 🚀"
)
client.message.send_text("minha-instancia", message)

print("✅ Mensagem enviada com sucesso!")
```

## 📚 Documentação Completa

### Gerenciamento de Instâncias

O `InstanceService` gerencia o ciclo de vida completo das instâncias do WhatsApp.

#### Criar Instância

```python
from client import EvolutionClient
from models.instance import InstanceConfig

client = EvolutionClient(base_url="https://api.com", api_token="token")

# Criar instância com QR Code
config = InstanceConfig(
    instanceName="vendas-bot",
    qrcode=True,
    number="5511999999999"
)
result = client.instance.create_instance(config.__dict__)
print(f"Instância criada: {result}")
```

#### Conectar e Gerenciar Instância

```python
# Conectar instância
client.instance.connect_instance("vendas-bot")

# Verificar status da conexão
status = client.instance.status_instance("vendas-bot")
print(f"Status: {status['instance']['state']}")

# Buscar todas as instâncias
instances = client.instance.fetch_instances()

# Buscar instância específica
instance = client.instance.fetch_instances("vendas-bot")

# Reiniciar instância
client.instance.restart_instance("vendas-bot")

# Fazer logout
client.instance.logout_instance("vendas-bot")

# Remover instância
client.instance.remove_instance("vendas-bot")
```

#### Definir Presença

```python
from models.instance import PresenceStatus

# Definir como disponível
client.instance.set_presence("vendas-bot", PresenceStatus.AVAILABLE)

# Definir como indisponível
client.instance.set_presence("vendas-bot", PresenceStatus.UNAVAILABLE)
```

---

### Envio de Mensagens

O `MessageService` oferece métodos para enviar diversos tipos de mensagens.

#### Mensagem de Texto

```python
from models.message import TextMessage

message = TextMessage(
    number="5511999999999",
    text="Olá! Como posso ajudar você hoje?"
)
client.message.send_text("vendas-bot", message)
```

#### Mensagem com Mídia

```python
from models.message import MediaMessage

# Enviar imagem
media = MediaMessage(
    number="5511999999999",
    url="https://example.com/imagem.jpg",
    caption="Confira nossa promoção!"
)
client.message.send_media("vendas-bot", media)

# Enviar áudio do WhatsApp
audio = MediaMessage(
    number="5511999999999",
    url="https://example.com/audio.mp3"
)
client.message.send_whatsapp_audio("vendas-bot", audio)

# Enviar sticker
sticker = MediaMessage(
    number="5511999999999",
    url="https://example.com/sticker.webp"
)
client.message.send_sticker("vendas-bot", sticker)
```

#### Mensagem de Localização

```python
from models.message import LocationMessage

location = LocationMessage(
    number="5511999999999",
    latitude=-23.550520,
    longitude=-46.633308,
    name="Avenida Paulista",
    address="São Paulo, SP"
)
client.message.send_location("vendas-bot", location)
```

#### Enviar Contato

```python
from models.message import ContactMessage

contact = ContactMessage(
    number="5511999999999",
    contact_name="João Silva",
    contact_number="5511888888888"
)
client.message.send_contact("vendas-bot", contact)
```

#### Enviar Reação

```python
from models.message import ReactionMessage

reaction = ReactionMessage(
    number="5511999999999",
    message_id="MESSAGE_ID_HERE",
    reaction="👍"
)
client.message.send_reaction("vendas-bot", reaction)
```

#### Criar Enquete

```python
from models.message import PollMessage

poll = PollMessage(
    number="5511999999999",
    poll_name="Qual sua preferência?",
    poll_options=["Opção 1", "Opção 2", "Opção 3"]
)
client.message.send_poll("vendas-bot", poll)
```

#### Enviar Lista Interativa

```python
from models.message import ListMessage

list_msg = ListMessage(
    number="5511999999999",
    title="Menu Principal",
    button_text="Ver Opções",
    description="Escolha uma opção do menu",
    sections=[
        {
            "title": "Produtos",
            "rows": [
                {"title": "Produto 1", "description": "Descrição do produto 1"},
                {"title": "Produto 2", "description": "Descrição do produto 2"}
            ]
        }
    ]
)
client.message.send_list("vendas-bot", list_msg)
```

#### Enviar Template

```python
from models.message import TemplateMessage

template = TemplateMessage(
    number="5511999999999",
    template_name="hello_world",
    language="pt_BR",
    components=[
        {
            "type": "body",
            "parameters": [
                {"type": "text", "text": "João"}
            ]
        }
    ]
)
client.message.send_template("vendas-bot", template)
```

---

### Gerenciamento de Chats

O `ChatService` gerencia conversas e mensagens.

#### Verificar se é WhatsApp

```python
result = client.chat.check_is_whatsapp("vendas-bot", "5511999999999")
print(f"É WhatsApp: {result['exists']}")
```

#### Marcar Mensagem como Lida

```python
from models.chat import MarkAsRead

mark = MarkAsRead(
    number="5511999999999",
    message_id="MESSAGE_ID_HERE"
)
client.chat.mark_message_as_read("vendas-bot", mark)
```

#### Arquivar Conversa

```python
from models.chat import ArchiveChat

archive = ArchiveChat(
    number="5511999999999",
    archive=True  # False para desarquivar
)
client.chat.archive_chat("vendas-bot", archive)
```

#### Deletar Mensagem para Todos

```python
from models.chat import DeleteMessage

delete = DeleteMessage(
    number="5511999999999",
    message_id="MESSAGE_ID_HERE"
)
client.chat.delete_message_for_everyone("vendas-bot", delete)
```

#### Enviar Presença

```python
# Mostrar "digitando..."
client.chat.send_presence("vendas-bot", "5511999999999", "composing")

# Mostrar "gravando áudio..."
client.chat.send_presence("vendas-bot", "5511999999999", "recording")

# Disponível
client.chat.send_presence("vendas-bot", "5511999999999", "available")
```

#### Buscar Foto de Perfil

```python
result = client.chat.fetch_profile_picture_url("vendas-bot", "5511999999999")
print(f"URL da foto: {result['profilePictureUrl']}")
```

#### Buscar Contatos

```python
contacts = client.chat.find_contacts("vendas-bot", "5511999999999")
print(f"Contatos encontrados: {contacts}")
```

#### Buscar Mensagens

```python
from models.chat import FindMessages

search = FindMessages(
    number="5511999999999",
    count=20  # Número de mensagens
)
messages = client.chat.find_messages("vendas-bot", search)
```

#### Atualizar Mensagem

```python
from models.chat import UpdateMessage

update = UpdateMessage(
    number="5511999999999",
    message_id="MESSAGE_ID_HERE",
    text="Texto atualizado"
)
client.chat.update_message("vendas-bot", update)
```

#### Listar Todas as Conversas

```python
chats = client.chat.find_chats("vendas-bot")
for chat in chats['chats']:
    print(f"Chat: {chat['id']}")
```

---

### Gerenciamento de Perfil

O `ProfileService` gerencia informações do perfil WhatsApp.

#### Buscar Perfil Comercial

```python
profile = client.profile.fetch_business_profile("vendas-bot", "5511999999999")
print(f"Nome comercial: {profile['name']}")
```

#### Buscar Perfil

```python
profile = client.profile.fetch_profile("vendas-bot", "5511999999999")
print(f"Nome: {profile['name']}")
print(f"Status: {profile['status']}")
```

#### Atualizar Nome do Perfil

```python
from models.profile import UpdateProfileName

update = UpdateProfileName(name="Meu Novo Nome")
client.profile.update_profile_name("vendas-bot", update)
```

#### Atualizar Status

```python
from models.profile import UpdateProfileStatus

status = UpdateProfileStatus(status="Disponível para atendimento!")
client.profile.update_profile_status("vendas-bot", status)
```

#### Atualizar Foto de Perfil

```python
# A foto deve ser um arquivo local
client.profile.update_profile_picture("vendas-bot", "/caminho/para/foto.jpg")
```

#### Remover Foto de Perfil

```python
client.profile.remove_profile_picture("vendas-bot")
```

#### Buscar Configurações de Privacidade

```python
settings = client.profile.fetch_privacy_settings("vendas-bot")
print(f"Configurações: {settings}")
```

#### Atualizar Configurações de Privacidade

```python
from models.profile import UpdatePrivacySettings

privacy = UpdatePrivacySettings(
    setting="readReceipts",  # ou "profilePicture", "status", "online"
    value="contacts"  # ou "all", "nobody"
)
client.profile.update_privacy_settings("vendas-bot", privacy)
```

---

### Gerenciamento de Grupos

O `GroupService` oferece funcionalidades completas para grupos.

#### Criar Grupo

```python
from models.group import CreateGroup

group = CreateGroup(
    subject="Meu Grupo",
    participants=["5511999999999", "5511888888888"]
)
result = client.group.create_group("vendas-bot", group)
print(f"Grupo criado: {result['groupId']}")
```

#### Atualizar Foto do Grupo

```python
client.group.update_group_picture(
    "vendas-bot",
    "123456@g.us",
    "/caminho/para/foto.jpg"
)
```

#### Atualizar Assunto do Grupo

```python
from models.group import UpdateGroupSubject

update = UpdateGroupSubject(
    group_id="123456@g.us",
    subject="Novo Assunto do Grupo"
)
client.group.update_group_subject("vendas-bot", update)
```

#### Atualizar Descrição do Grupo

```python
from models.group import UpdateGroupDescription

update = UpdateGroupDescription(
    group_id="123456@g.us",
    description="Nova descrição do grupo"
)
client.group.update_group_description("vendas-bot", update)
```

#### Buscar Link de Convite

```python
invite = client.group.fetch_invite_code("vendas-bot", "123456@g.us")
print(f"Código de convite: {invite['inviteCode']}")
```

#### Aceitar Convite

```python
result = client.group.accept_invite_code("vendas-bot", "CODIGO_CONVITE")
```

#### Revogar Link de Convite

```python
client.group.revoke_invite_code("vendas-bot", "123456@g.us")
```

#### Enviar Convite para Número

```python
client.group.send_group_invite("vendas-bot", "123456@g.us", "5511999999999")
```

#### Buscar Informações do Grupo

```python
# Por código de convite
group = client.group.find_group_by_invite_code("vendas-bot", "CODIGO")

# Por JID
group = client.group.find_group_by_jid("vendas-bot", "123456@g.us")
```

#### Listar Todos os Grupos

```python
groups = client.group.fetch_all_groups("vendas-bot")
for group in groups['groups']:
    print(f"Grupo: {group['subject']}")
```

#### Buscar Membros do Grupo

```python
members = client.group.find_group_members("vendas-bot", "123456@g.us")
for member in members['members']:
    print(f"Membro: {member['id']}")
```

#### Atualizar Membros do Grupo

```python
from models.group import UpdateGroupMembers

# Adicionar membros
update = UpdateGroupMembers(
    group_id="123456@g.us",
    participants=["5511999999999"],
    action="add"  # ou "remove", "promote", "demote"
)
client.group.update_group_members("vendas-bot", update)
```

#### Atualizar Configurações do Grupo

```python
from models.group import UpdateGroupSetting

# Permitir apenas admins enviarem mensagens
setting = UpdateGroupSetting(
    group_id="123456@g.us",
    setting="announcement",
    value=True
)
client.group.update_group_setting("vendas-bot", setting)
```

#### Ativar/Desativar Mensagens Temporárias

```python
client.group.toggle_ephemeral("vendas-bot", "123456@g.us", is_ephemeral=True)
```

#### Sair do Grupo

```python
client.group.leave_group("vendas-bot", "123456@g.us")
```

---

### Webhooks

O `WebhookService` configura endpoints para receber notificações de eventos.

#### Configurar Webhook

```python
from models.webhook import WebhookConfig, WebhookEvents

config = WebhookConfig(
    url="https://seu-servidor.com/webhook",
    events=[
        WebhookEvents.MESSAGES_UPSERT,
        WebhookEvents.CONNECTION_UPDATE,
        WebhookEvents.QRCODE_UPDATED,
        WebhookEvents.CALL,
        WebhookEvents.GROUPS_UPSERT
    ],
    webhook_by_events=True,
    webhook_base64=False
)

client.webhook.set_webhook("vendas-bot", config)
```

#### Buscar Configuração de Webhook

```python
webhook = client.webhook.find_webhook("vendas-bot")
print(f"URL do webhook: {webhook['url']}")
print(f"Eventos: {webhook['events']}")
```

#### Eventos de Webhook Disponíveis

```python
from models.webhook import WebhookEvents

# Eventos de aplicação
WebhookEvents.APPLICATION_STARTUP

# Eventos de QR Code
WebhookEvents.QRCODE_UPDATED

# Eventos de mensagens
WebhookEvents.MESSAGES_SET
WebhookEvents.MESSAGES_UPSERT
WebhookEvents.MESSAGES_UPDATE
WebhookEvents.MESSAGES_DELETE
WebhookEvents.SEND_MESSAGE

# Eventos de contatos
WebhookEvents.CONTACTS_SET
WebhookEvents.CONTACTS_UPSERT
WebhookEvents.CONTACTS_UPDATE

# Eventos de chats
WebhookEvents.CHATS_SET
WebhookEvents.CHATS_UPSERT
WebhookEvents.CHATS_UPDATE
WebhookEvents.CHATS_DELETE

# Eventos de grupos
WebhookEvents.GROUPS_UPSERT
WebhookEvents.GROUPS_UPDATE
WebhookEvents.GROUP_PARTICIPANTS_UPDATE

# Eventos de conexão
WebhookEvents.CONNECTION_UPDATE
WebhookEvents.PRESENCE_UPDATE
WebhookEvents.PRESENCE

# Eventos de chamadas
WebhookEvents.CALL

# Eventos de Typebot
WebhookEvents.TYPEBOT_START
WebhookEvents.TYPEBOT_SEND_MESSAGE
```

---

### Configurações

O `SettingsService` gerencia configurações da instância.

#### Definir Configurações

```python
from models.settings import SettingsConfig

config = SettingsConfig(
    reject_call=True,                # Rejeitar chamadas automaticamente
    groups_ignore=False,             # Ignorar mensagens de grupos
    always_online=True,              # Aparecer sempre online
    read_messages=True,              # Marcar mensagens como lidas
    read_status=True,                # Marcar status como lidos
    sync_full_history=False,         # Sincronizar histórico completo
    msg_call="Não aceito chamadas"   # Mensagem ao rejeitar chamada
)

client.settings.set_settings("vendas-bot", config)
```

#### Buscar Configurações

```python
settings = client.settings.find_settings("vendas-bot")
print(f"Rejeitar chamadas: {settings['reject_call']}")
print(f"Sempre online: {settings['always_online']}")
```

---

### Integrações

#### Typebot (Chatbot)

```python
from models.typebot import SetTypebot, StartTypebot, ChangeTypebotStatus

# Configurar Typebot
typebot = SetTypebot(
    name="Meu Bot",
    url="https://typebot.io/my-bot",
    token="SEU_TOKEN_TYPEBOT"
)
client.typebot.set_typebot("vendas-bot", typebot)

# Iniciar sessão com Typebot
start = StartTypebot(
    number="5511999999999",
    start={"flow": "welcome"}
)
client.typebot.start_typebot("vendas-bot", start)

# Buscar Typebot configurado
typebot_info = client.typebot.find_typebot("vendas-bot", "5511999999999")

# Alterar status do Typebot
status = ChangeTypebotStatus(
    number="5511999999999",
    status="paused"  # ou "active"
)
client.typebot.change_typebot_status("vendas-bot", status)
```

#### Chatwoot (Atendimento)

```python
from models.chatwoot import SetChatwoot

# Configurar Chatwoot
chatwoot = SetChatwoot(
    url="https://app.chatwoot.com",
    token="SEU_TOKEN_CHATWOOT"
)
client.chatwoot.set_chatwoot("vendas-bot", chatwoot)

# Buscar configuração do Chatwoot
chatwoot_info = client.chatwoot.find_chatwoot("vendas-bot")
```

#### RabbitMQ (Fila de Mensagens)

```python
from models.rabbitmq import SetRabbitMQ

# Configurar RabbitMQ
rabbitmq = SetRabbitMQ(
    uri="amqp://user:password@localhost:5672",
    queue="evolution_queue"
)
client.rabbitmq.set_rabbitmq("vendas-bot", rabbitmq)

# Buscar configuração do RabbitMQ
rabbitmq_info = client.rabbitmq.find_rabbitmq("vendas-bot")
```

#### WebSocket (Conexão em Tempo Real)

```python
from models.websocket import SetWebSocket

# Habilitar WebSocket
websocket = SetWebSocket(enabled=True)
client.websocket.set_websocket("vendas-bot", websocket)

# Buscar configuração do WebSocket
websocket_info = client.websocket.find_websocket("vendas-bot")
```

---

## 🛡️ Tratamento de Erros

O SDK oferece exceções específicas para diferentes cenários:

```python
from exception import (
    EvolutionAPIError,           # Erro genérico da API
    EvolutionAuthenticationError, # Erro de autenticação (401)
    EvolutionNotFoundError        # Recurso não encontrado (404)
)

try:
    # Suas operações aqui
    client.instance.fetch_instances()

except EvolutionAuthenticationError as e:
    print(f"❌ Erro de autenticação: {e}")
    print("Verifique se sua API key está correta")

except EvolutionNotFoundError as e:
    print(f"❌ Recurso não encontrado: {e}")
    print("Verifique se a instância existe")

except EvolutionAPIError as e:
    print(f"❌ Erro na API: {e}")
    print("Ocorreu um erro inesperado")
```

## 🧪 Testes

O SDK possui uma suíte completa de testes automatizados.

### Executar Todos os Testes

```bash
# Com pytest
pytest -v

# Com uv
uv run pytest -v
```

### Executar Testes Específicos

```bash
# Testar apenas o client
pytest tests/test_client.py -v

# Testar apenas um serviço específico
pytest tests/test_service_message.py -v

# Executar teste específico
pytest tests/test_client.py::test_get_success -v
```


## 🤝 Contribuição

Contribuições são muito bem-vindas! Siga os passos abaixo:

### Como Contribuir

1. **Fork o projeto**
   ```bash
   git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
   ```

2. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/minha-nova-feature
   ```

3. **Faça suas alterações e adicione testes**
   ```bash
   # Faça suas modificações
   # Adicione testes para suas mudanças
   pytest -v
   ```

4. **Commit suas mudanças**
   ```bash
   git commit -am 'feat: Adiciona nova funcionalidade X'
   ```

5. **Push para a branch**
   ```bash
   git push origin feature/minha-nova-feature
   ```

6. **Abra um Pull Request**
   - Descreva suas mudanças detalhadamente
   - Referencie issues relacionadas
   - Aguarde review

### Diretrizes de Contribuição

- ✅ Escreva testes para novas funcionalidades
- ✅ Mantenha a cobertura de testes acima de 90%
- ✅ Siga o estilo de código do projeto
- ✅ Documente novas funcionalidades
- ✅ Use commits semânticos (feat, fix, docs, etc.)

## 📄 Licença

Este projeto está licenciado sob a **Licença Apache 2.0**.

```
Copyright 2025 Júnior Carvalho

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 💬 Suporte

### Precisa de Ajuda?

- 📖 **Documentação:** [Evolution API Docs](https://doc.evolution-api.com)
- 🐛 **Issues:** [Reportar um problema](https://github.com/juniorcarvalho/evolution-api-sdk/issues)
- 💡 **Discussões:** [GitHub Discussions](https://github.com/juniorcarvalho/evolution-api-sdk/discussions)
- 📧 **Email:** joseadolfojr@gmail.com

### Links Úteis

- [Evolution API](https://evolution-api.com)
- [Documentação Oficial](https://doc.evolution-api.com)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)

---

<div align="center">

**Desenvolvido com ❤️ por [Júnior Carvalho](https://github.com/juniorcarvalho)**

[![GitHub](https://img.shields.io/badge/GitHub-juniorcarvalho-181717?logo=github)](https://github.com/juniorcarvalho)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

⭐ Se este projeto foi útil para você, considere dar uma estrela!

</div>
