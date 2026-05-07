# Desafio de Automação de Testes - Swagger Petstore e SauceDemo

Repositório único criado para o trabalho de automação de testes, contendo:

- Automação de API usando Swagger Petstore
- Automação Web usando Selenium no SauceDemo
- Pipeline de CI/CD com GitHub Actions
- Organização com boas práticas, separação de responsabilidades e Page Object Model

## Objetivo

Avaliar a capacidade técnica no desenvolvimento de automação de testes robusta, seguindo boas práticas de desenvolvimento, organização de código, reusabilidade e integração contínua.

## Tecnologias utilizadas

- Python
- Pytest
- Requests
- Selenium WebDriver
- WebDriver Manager
- GitHub Actions
- Page Object Model

## Estrutura do projeto

```text
qa-automation-challenge/
├── .github/
│   └── workflows/
│       └── main.yml
├── api_tests/
│   ├── tests/
│   └── utils/
├── web_tests/
│   ├── pages/
│   ├── tests/
│   └── utils/
├── docs/
│   └── prints/
├── requirements.txt
└── README.md
```

## Automação de API

Base URL:

```text
https://petstore.swagger.io/v2
```

A automação de API cobre os principais recursos da Swagger Petstore:

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

Fluxo E2E implementado:

1. Acessar o SauceDemo
2. Realizar login com usuário válido
3. Adicionar produtos ao carrinho
4. Validar produtos no carrinho
5. Preencher dados do checkout
6. Finalizar a compra
7. Validar mensagem de sucesso

## Boas práticas aplicadas

- Separação entre testes, páginas e utilitários
- Uso de Page Object Model na automação Web
- Dados dinâmicos nos testes de API
- Asserções claras em cada cenário
- Organização do projeto em um único repositório
- Pipeline executando API e Web automaticamente

## Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Livio038/qa-automation-challenge.git
cd qa-automation-challenge
```

### 2. Criar ambiente virtual

Windows PowerShell:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar todos os testes

```bash
pytest
```

### 5. Executar somente API

```bash
pytest api_tests/tests/
```

### 6. Executar somente Web

```bash
pytest web_tests/tests/
```

## Pipeline CI/CD

O projeto possui integração contínua com GitHub Actions.

Arquivo da pipeline:

```text
.github/workflows/main.yml
```

A pipeline é executada automaticamente em:

- Push
- Pull Request
- Execução manual pelo GitHub Actions

Ela possui dois jobs:

- API Tests - Swagger Petstore
- Web Tests - SauceDemo

## Evidências de execução

Adicione os prints na pasta:

```text
docs/prints/
```

### Execução local

![Execução local](docs/prints/execucao-local.png)

### Pipeline GitHub Actions

![Pipeline GitHub Actions](docs/prints/pipeline-github-actions.png)

### Relatório ou resultado dos testes

![Relatório dos testes](docs/prints/relatorio-testes.png)

### Estrutura no VS Code

![Estrutura VS Code](docs/prints/estrutura-vscode.png)

## Roteiro de apresentação

1. Apresentar o objetivo do projeto
2. Mostrar a estrutura de pastas
3. Explicar os testes de API
4. Explicar o fluxo E2E Web
5. Mostrar o uso do Page Object Model
6. Executar os testes localmente
7. Mostrar a pipeline no GitHub Actions
8. Mostrar as evidências de execução

## Resumo da solução

Este projeto automatiza cenários de API e Web em um único repositório.

Na API, foram cobertos endpoints principais da Swagger Petstore, incluindo User, Pet e Store.

Na Web, foi implementado um fluxo ponta a ponta no SauceDemo usando Selenium.

A execução automatizada foi configurada no GitHub Actions para garantir validação contínua a cada alteração enviada ao repositório.
