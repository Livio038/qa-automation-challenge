# Desafio de Automação de Testes - Swagger Petstore e SauceDemo

Repositório único com automação de API e Web, usando Pytest, Requests, Selenium, Page Object Model e GitHub Actions.

## Tecnologias utilizadas

- Python
- Pytest
- Requests
- Selenium WebDriver
- WebDriver Manager
- Pytest HTML
- GitHub Actions
- Page Object Model

## Estrutura do projeto

```text
qa-automation-final/
├── .github/workflows/main.yml
├── api_tests/
│   ├── tests/
│   └── utils/
├── web_tests/
│   ├── pages/
│   ├── tests/
│   └── utils/
├── docs/prints/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Automação de API

Base URL:

```text
https://petstore.swagger.io/v2
```

Cobertura implementada:

### User

- Criar usuário
- Buscar usuário
- Atualizar usuário
- Deletar usuário
- Login
- Logout

### Pet

- Criar pet
- Buscar pet por ID
- Atualizar pet
- Buscar pet por status
- Deletar pet

### Store

- Criar pedido
- Buscar pedido
- Deletar pedido
- Consultar inventário

## Automação Web

URL:

```text
https://www.saucedemo.com/
```

Fluxos implementados:

- Login com usuário válido
- Compra ponta a ponta
- Login com usuário bloqueado
- Login com senha inválida
- Adicionar e remover item do carrinho
- Acessar detalhes de produto

## Boas práticas aplicadas

- Separação entre testes, páginas e utilitários
- Page Object Model na automação Web
- Dados dinâmicos nos testes de API
- Asserções claras
- Pipeline separada para API e Web
- Relatórios HTML gerados na execução

## Como executar localmente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente virtual no Windows

```bash
.\.venv\Scripts\Activate.ps1
```

Se preferir executar sem ativar:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar todos os testes

```bash
pytest
```

### 5. Rodar somente API

```bash
pytest api_tests/tests -m api
```

### 6. Rodar somente Web

```bash
pytest web_tests/tests -m web
```

## Pipeline CI/CD

A pipeline está em:

```text
.github/workflows/main.yml
```

Ela executa automaticamente em:

- Push
- Pull Request
- Execução manual pelo GitHub Actions

Jobs configurados:

- API Tests - Swagger Petstore
- Web Tests - SauceDemo

## Evidências de execução

Adicione os prints na pasta `docs/prints`.

Sugestão de arquivos:

```text
docs/prints/execucao-local.png
docs/prints/pipeline-github-actions.png
docs/prints/relatorio-testes.png
docs/prints/estrutura-vscode.png
```

## Roteiro de apresentação

1. Mostrar o objetivo do projeto
2. Explicar a estrutura de pastas
3. Mostrar os testes de API
4. Mostrar o uso de Page Objects
5. Explicar o fluxo E2E do SauceDemo
6. Mostrar os testes rodando localmente
7. Mostrar a pipeline no GitHub Actions
8. Mostrar as evidências de execução
