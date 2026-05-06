import os

# Dicionário contendo os caminhos dos arquivos e seus respectivos conteúdos
arquivos_do_projeto = {
    "api_tests/tests/test_petstore.py": """
import requests

BASE_URL = "https://petstore.swagger.io/v2"

class TestPetStore:
    def test_create_user(self):
        payload = {"id": 101, "username": "tester_gemini", "firstName": "Test", "lastName": "User"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        assert response.status_code == 200

    def test_add_new_pet(self):
        payload = {"id": 999, "name": "Snoopy", "status": "available"}
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()['name'] == "Snoopy"

    def test_place_order(self):
        payload = {"id": 1, "petId": 999, "quantity": 1, "status": "placed"}
        response = requests.post(f"{BASE_URL}/store/order", json=payload)
        assert response.status_code == 200
""",

    "web_tests/pages/login_page.py": """
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_field = (By.ID, "user-name")
        self.pass_field = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, user, password):
        self.driver.find_element(*self.user_field).send_keys(user)
        self.driver.find_element(*self.pass_field).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
""",

    "web_tests/tests/test_e2e_sauce.py": """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web_tests.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless") # Essencial para rodar no GitHub Actions
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.get("https://www.saucedemo.com/cart.html")
    driver.find_element("id", "checkout").click()
    
    driver.find_element("id", "first-name").send_keys("Tester")
    driver.find_element("id", "last-name").send_keys("Silva")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "finish").click()
    
    assert "thank-you" in driver.current_url
""",

    ".github/workflows/main.yml": """
name: QA Automation Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install requests pytest selenium webdriver-manager

      - name: Run API Tests
        run: pytest api_tests/tests/

      - name: Run Web Tests
        run: pytest web_tests/tests/
""",

    "requirements.txt": """
pytest
requests
selenium
webdriver-manager
""",

    "README.md": """
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
"""
}

# Lógica para criar as pastas e salvar os arquivos
for caminho_arquivo, conteudo in arquivos_do_projeto.items():
    # Cria os diretórios necessários, se não existirem
    diretorio = os.path.dirname(caminho_arquivo)
    if diretorio:
        os.makedirs(diretorio, exist_ok=True)
    
    # Escreve o conteúdo no arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo.strip() + "\n")

print("✅ Estrutura do projeto gerada com sucesso! Você já pode instalar os requirements e rodar os testes.")