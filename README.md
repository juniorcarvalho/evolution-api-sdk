# Evolution API SDK

SDK Python para integração com a Evolution API - WhatsApp Business API.

## Descrição

Este SDK facilita a integração com a Evolution API, permitindo o gerenciamento de instâncias do WhatsApp Business, configuração de webhooks, definição de configurações e muito mais através de uma interface Python simples e intuitiva.

## Instalação

### Requisitos

- Python 3.13+
- requests
- requests-toolbelt

### Instalação via pip

```bash
pip install evolution-api-sdk
```

### Instalação para desenvolvimento

```bash
git clone https://github.com/juniorcarvalho/evolution-api-sdk.git
cd evolution-api-sdk
pip install -e .
```

## Configuração

Para usar o SDK, você precisa ter uma instância da Evolution API rodando e obter sua chave de API.

```python
from client import EvolutionClient

# Inicializar o cliente
client = EvolutionClient(
    base_url="https://sua-evolution-api.com",
    api_token="sua-chave-de-api"
)
```

## Uso

### Informações da API

```python
# Obter informações sobre a API
info = client.get_info()
print(info)
```

### Gerenciamento de Instâncias

```python
# Buscar instâncias
instances = client.instance.fetch_instances()

# Buscar uma instância específica
instance = client.instance.fetch_instances("nome-da-instancia")

# Criar uma nova instância
from models.instance import InstanceConfig

config = InstanceConfig(
    instanceName="minha-instancia",
    qrcode=True,
    number="5511999999999"
)
result = client.instance.create_instance(config.__dict__)

# Conectar uma instância
client.instance.connect_instance("nome-da-instancia")

# Verificar status da conexão
status = client.instance.status_instance("nome-da-instancia")

# Reiniciar uma instância
client.instance.restart_instance("nome-da-instancia")

# Fazer logout de uma instância
client.instance.logout_instance("nome-da-instancia")

# Remover uma instância
client.instance.remove_instance("nome-da-instancia")

# Definir presença
from models.instance import PresenceStatus

client.instance.set_presence("nome-da-instancia", PresenceStatus.AVAILABLE)
```

### Configuração de Webhooks

```python
from models.webhook import WebhookConfig, WebhookEvents

# Configurar webhook
webhook_config = WebhookConfig(
    url="https://seu-webhook.com/endpoint",
    events=[
        WebhookEvents.MESSAGES_UPSERT,
        WebhookEvents.CONNECTION_UPDATE,
        WebhookEvents.QRCODE_UPDATED
    ],
    webhook_by_events=True,
    webhook_base64=False
)

result = client.webhook.set_webhook("nome-da-instancia", webhook_config)

# Buscar configuração de webhook
webhook_info = client.webhook.find_webhook("nome-da-instancia")
```

### Configurações da Instância

```python
from models.settings import SettingsConfig

# Definir configurações
settings_config = SettingsConfig(
    reject_call=True,
    groups_ignore=False,
    always_online=True,
    read_messages=True,
    read_status=True,
    sync_full_history=False,
    msg_call="Chamadas não são aceitas neste número."
)

result = client.settings.set_settings("nome-da-instancia", settings_config)

# Buscar configurações
settings_info = client.settings.find_settings("nome-da-instancia")
```

## Eventos de Webhook Disponíveis

O SDK suporta os seguintes eventos de webhook:

- `APPLICATION_STARTUP` - Inicialização da aplicação
- `QRCODE_UPDATED` - QR Code atualizado
- `MESSAGES_SET` - Mensagens definidas
- `MESSAGES_UPSERT` - Mensagens inseridas/atualizadas
- `MESSAGES_UPDATE` - Mensagens atualizadas
- `MESSAGES_DELETE` - Mensagens deletadas
- `SEND_MESSAGE` - Mensagem enviada
- `CONTACTS_SET` - Contatos definidos
- `CONTACTS_UPSERT` - Contatos inseridos/atualizados
- `CONTACTS_UPDATE` - Contatos atualizados
- `PRESENCE_UPDATE` - Atualização de presença
- `CHATS_SET` - Chats definidos
- `CHATS_UPSERT` - Chats inseridos/atualizados
- `CHATS_UPDATE` - Chats atualizados
- `CHATS_DELETE` - Chats deletados
- `GROUPS_UPSERT` - Grupos inseridos/atualizados
- `GROUPS_UPDATE` - Grupos atualizados
- `GROUP_PARTICIPANTS_UPDATE` - Participantes do grupo atualizados
- `CONNECTION_UPDATE` - Atualização de conexão
- `CALL` - Chamada
- `PRESENCE` - Presença
- `TYPEBOT_START` - Início do Typebot
- `TYPEBOT_SEND_MESSAGE` - Mensagem do Typebot

## Tratamento de Erros

O SDK inclui tratamento de erros específicos:

```python
from exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError

try:
    result = client.instance.fetch_instances()
except EvolutionAuthenticationError:
    print("Erro de autenticação - verifique sua chave de API")
except EvolutionNotFoundError:
    print("Recurso não encontrado")
except EvolutionAPIError as e:
    print(f"Erro na API: {e}")
```

## Exemplos Práticos

### Exemplo 1: Criar e Configurar uma Instância Completa

```python
from client import EvolutionClient
from models.instance import InstanceConfig
from models.webhook import WebhookConfig, WebhookEvents
from models.settings import SettingsConfig

# Inicializar cliente
client = EvolutionClient("https://sua-api.com", "sua-chave")

# Criar instância
instance_config = InstanceConfig(
    instanceName="bot-vendas",
    qrcode=True,
    number="5511999999999"
)
client.instance.create_instance(instance_config.__dict__)

# Configurar webhook
webhook_config = WebhookConfig(
    url="https://seu-sistema.com/webhook",
    events=[WebhookEvents.MESSAGES_UPSERT, WebhookEvents.CONNECTION_UPDATE],
    webhook_by_events=True
)
client.webhook.set_webhook("bot-vendas", webhook_config)

# Configurar settings
settings_config = SettingsConfig(
    reject_call=True,
    groups_ignore=False,
    always_online=True,
    read_messages=True,
    read_status=True,
    sync_full_history=False
)
client.settings.set_settings("bot-vendas", settings_config)

print("Instância configurada com sucesso!")
```

### Exemplo 2: Monitorar Status de Múltiplas Instâncias

```python
# Buscar todas as instâncias
instances = client.instance.fetch_instances()

for instance in instances:
    instance_name = instance.get('instance', {}).get('instanceName')
    if instance_name:
        status = client.instance.status_instance(instance_name)
        print(f"Instância: {instance_name} - Status: {status.get('instance', {}).get('state')}")
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Suporte

Para suporte e dúvidas:

- Abra uma issue no GitHub
- Consulte a [documentação oficial da Evolution API](https://doc.evolution-api.com)

## Changelog

### v0.1.0
- Implementação inicial do SDK
- Suporte para gerenciamento de instâncias
- Configuração de webhooks
- Configuração de settings da instância
- Método para obter informações da API
- Método para reiniciar instâncias
