# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [0.1.0] - 2025-10-02

### Adicionado

#### Core
- Cliente principal `EvolutionClient` para interação com a Evolution API
- Sistema de tratamento de erros com exceções personalizadas:
  - `EvolutionAPIError` - Erro genérico da API
  - `EvolutionAuthenticationError` - Erro de autenticação (401)
  - `EvolutionNotFoundError` - Recurso não encontrado (404)

#### Serviços
- **InstanceService**: Gerenciamento completo de instâncias WhatsApp
  - Criar, conectar, desconectar, reiniciar instâncias
  - Verificar status de conexão
  - Gerenciar QR Code
  - Definir presença (disponível/indisponível)
  - Fazer logout e remover instâncias

- **MessageService**: Envio de diversos tipos de mensagens
  - Mensagens de texto
  - Mídia (imagem, vídeo, documento)
  - Áudio do WhatsApp
  - Stickers
  - Localização
  - Contatos
  - Reações
  - Enquetes (polls)
  - Listas interativas
  - Templates

- **ChatService**: Gerenciamento de conversas
  - Verificar se número é WhatsApp
  - Marcar mensagens como lidas
  - Arquivar/desarquivar conversas
  - Deletar mensagens para todos
  - Enviar presença (digitando, gravando áudio)
  - Buscar foto de perfil
  - Buscar contatos e mensagens
  - Atualizar mensagens
  - Listar todas as conversas

- **ProfileService**: Gerenciamento de perfil
  - Buscar perfil comercial e pessoal
  - Atualizar nome do perfil
  - Atualizar status
  - Atualizar foto de perfil
  - Remover foto de perfil
  - Gerenciar configurações de privacidade

- **GroupService**: Gerenciamento completo de grupos
  - Criar grupos
  - Atualizar foto, assunto e descrição
  - Gerenciar código de convite
  - Adicionar/remover/promover/rebaixar membros
  - Configurações do grupo (somente admins, mensagens temporárias)
  - Buscar informações e membros
  - Sair do grupo

- **WebhookService**: Configuração de webhooks
  - Definir URL e eventos de notificação
  - 23 eventos diferentes suportados (mensagens, contatos, grupos, chamadas, etc.)
  - Buscar configuração atual

- **SettingsService**: Configurações da instância
  - Rejeitar chamadas automaticamente
  - Ignorar mensagens de grupos
  - Modo sempre online
  - Leitura automática de mensagens e status
  - Sincronização de histórico
  - Mensagem personalizada ao rejeitar chamada

- **TypebotService**: Integração com Typebot
  - Configurar bot conversacional
  - Iniciar sessões com usuários
  - Alterar status do bot

- **ChatwootService**: Integração com Chatwoot
  - Configurar plataforma de atendimento
  - Buscar configuração atual

- **RabbitMQService**: Integração com RabbitMQ
  - Configurar fila de mensagens
  - Buscar configuração atual

- **WebSocketService**: Conexão WebSocket
  - Habilitar/desabilitar conexão em tempo real
  - Buscar configuração atual

#### Modelos de Dados
- Modelos completos para todos os tipos de requisições
- Type hints para melhor experiência de desenvolvimento
- Validação de dados via modelos

#### Testes
- 82 testes automatizados (100% de sucesso)
- Cobertura completa de todos os serviços
- Testes usando mocks para isolamento
- Configuração pytest com suporte ao flat layout

#### Documentação
- README.md completo em português com exemplos de uso
- Documentação de todos os 11 serviços
- Guia de instalação (pip e uv)
- Exemplos de código para todas as funcionalidades
- Tratamento de erros documentado
- Guia de contribuição
- CLAUDE.md para contexto de desenvolvimento
- PUBLISHING.md com instruções de publicação

#### Infraestrutura
- Licença Apache 2.0
- pyproject.toml configurado para publicação no PyPI
- Suporte para Python 3.8+
- Estrutura flat layout
- Configuração de build com setuptools
- Git ignore apropriado
- Pytest configurado

### Características Técnicas
- Compatível com Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- Dependências mínimas (requests, requests-toolbelt)
- Type hints para melhor IDE support
- Arquitetura orientada a serviços
- Cliente HTTP reutilizável
- Tratamento robusto de erros

### Notas
- Primeira versão beta do SDK
- API estável mas pode receber melhorias
- Feedback e contribuições são bem-vindas

[0.1.0]: https://github.com/juniorcarvalho/evolution-api-sdk/releases/tag/v0.1.0
