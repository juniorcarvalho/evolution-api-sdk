# Guia de Publicação no PyPI

Este guia descreve como publicar o Evolution API SDK no PyPI (Python Package Index).

## Pré-requisitos

Antes de publicar, você precisa:

1. **Conta no PyPI**:
   - Criar conta em: https://pypi.org/account/register/
   - Criar conta no TestPyPI (para testes): https://test.pypi.org/account/register/

2. **Configurar autenticação**:
   - Gerar API Token no PyPI: https://pypi.org/manage/account/token/
   - Gerar API Token no TestPyPI: https://test.pypi.org/manage/account/token/

3. **Instalar ferramentas necessárias**:
   ```bash
   # Com uv
   uv pip install build twine

   # Ou com pip
   pip install build twine
   ```

## Passo a Passo para Publicação

### 1. Verificar e Atualizar Versão

Edite a versão no `pyproject.toml`:

```toml
[project]
version = "0.1.0"  # Atualize conforme necessário
```

Siga o [Versionamento Semântico](https://semver.org/):
- **MAJOR**: Mudanças incompatíveis na API (ex: 1.0.0 → 2.0.0)
- **MINOR**: Novas funcionalidades compatíveis (ex: 0.1.0 → 0.2.0)
- **PATCH**: Correções de bugs (ex: 0.1.0 → 0.1.1)

### 2. Executar Testes

```bash
# Executar todos os testes
pytest -v

# Verificar que todos os 82 testes passam
pytest tests/ -v
```

### 3. Limpar builds anteriores

```bash
# Remover builds antigos
rm -rf dist/ build/ *.egg-info
```

### 4. Build do Pacote

```bash
# Usando uv (recomendado)
uv build

# Ou usando python -m build
python -m build
```

Isso irá gerar:
- `dist/evolution_api_sdk-VERSION.tar.gz` (source distribution)
- `dist/evolution_api_sdk-VERSION-py3-none-any.whl` (wheel distribution)

### 5. Verificar o Pacote

```bash
# Verificar se o pacote está correto
twine check dist/*
```

### 6. Publicar no TestPyPI (Recomendado Primeiro)

```bash
# Upload para TestPyPI
twine upload --repository testpypi dist/*

# Será solicitado:
# Username: __token__
# Password: seu-token-do-testpypi
```

Após upload bem-sucedido, teste a instalação:

```bash
# Criar ambiente virtual para teste
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# ou
test_env\Scripts\activate  # Windows

# Instalar do TestPyPI
pip install --index-url https://test.pypi.org/simple/ evolution-api-sdk

# Testar importação
python -c "from client import EvolutionClient; print('OK')"

# Desativar ambiente
deactivate
```

### 7. Publicar no PyPI (Produção)

Após confirmar que tudo funciona no TestPyPI:

```bash
# Upload para PyPI oficial
twine upload dist/*

# Será solicitado:
# Username: __token__
# Password: seu-token-do-pypi
```

### 8. Verificar Publicação

Acesse a página do projeto:
- PyPI: https://pypi.org/project/evolution-api-sdk/
- TestPyPI: https://test.pypi.org/project/evolution-api-sdk/

Teste a instalação:

```bash
pip install evolution-api-sdk
```

## Usando Arquivo de Configuração (.pypirc)

Para evitar digitar tokens toda vez, crie `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-SEU_TOKEN_AQUI

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-SEU_TOKEN_TESTPYPI_AQUI
```

Com isso, pode usar:

```bash
# Upload para TestPyPI
twine upload --repository testpypi dist/*

# Upload para PyPI
twine upload dist/*
```

## Automatização com GitHub Actions (Opcional)

Crie `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

Adicione o token como secret no GitHub:
- Settings → Secrets and variables → Actions → New repository secret
- Nome: `PYPI_API_TOKEN`
- Valor: seu token do PyPI

## Checklist de Publicação

Antes de publicar, verifique:

- [ ] Todos os testes passam (`pytest -v`)
- [ ] Versão atualizada em `pyproject.toml`
- [ ] README.md está atualizado
- [ ] CHANGELOG.md atualizado com mudanças da versão
- [ ] Licença está correta (Apache-2.0)
- [ ] Build funciona sem erros (`uv build`)
- [ ] Pacote verificado (`twine check dist/*`)
- [ ] Testado no TestPyPI
- [ ] Git tag criada para a versão
- [ ] Commit e push realizados

## Criar Tag de Versão no Git

```bash
# Criar tag
git tag -a v0.1.0 -m "Release version 0.1.0"

# Enviar tag para o GitHub
git push origin v0.1.0

# Ou enviar todas as tags
git push --tags
```

## Solução de Problemas

### Erro: "File already exists"

O PyPI não permite reenviar a mesma versão. Soluções:
1. Incrementar a versão em `pyproject.toml`
2. Rebuild e enviar novamente

### Erro: "Invalid distribution filename"

Certifique-se de que o nome do pacote segue o padrão:
- Letras minúsculas
- Hífens ao invés de underscores
- Sem espaços ou caracteres especiais

### Erro: "Insufficient permission"

Verifique se o token de API:
- Está correto e não expirou
- Tem permissões de escrita
- Foi copiado completamente (incluindo o prefixo `pypi-`)

## Recursos Úteis

- [PyPI Documentation](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
- [Python Packaging User Guide](https://packaging.python.org/)

## Manutenção

Após cada release:

1. Criar uma GitHub Release com as mudanças
2. Atualizar a branch `main` com a versão mais recente
3. Documentar as mudanças no CHANGELOG.md
4. Anunciar a nova versão (se aplicável)
