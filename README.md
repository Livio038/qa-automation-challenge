# Desafio de Automação de Testes - Swagger & SauceDemo

## 🚀 Tecnologias
- **Linguagem:** Python 3.9
- **Framework de Teste:** Pytest
- **Web:** Selenium WebDriver
- **API:** Requests
- **CI/CD:** GitHub Actions

## 🏗️ Padrões Utilizados
- **Page Object Model (POM):** Aplicado na automação Web para facilitar manutenção.
- **Assertions:** Validações de Status Code (API) e URL/Elementos (Web).

## 🔧 Como Executar
1. Clone o repositório.
2. Instale as dependências executando: `pip install -r requirements.txt`
3. Execute os testes:
   - API: `pytest api_tests/`
   - Web: `pytest web_tests/`

## 📈 Pipeline (CI)
O projeto conta com integração contínua via GitHub Actions, executando todos os testes automaticamente a cada push feito no repositório.
