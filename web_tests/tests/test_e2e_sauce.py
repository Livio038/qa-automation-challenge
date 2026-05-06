import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web_tests.pages.login_page import LoginPage

@pytest.fixture
def driver():
    # Configurações para rodar no GitHub Actions (Linux) e Local (Windows)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    # Espera implícita para evitar erros de carregamento lento (Race Conditions)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    # Acessar o site
    driver.get("https://www.saucedemo.com/")
    
    # Realizar Login usando Page Objects
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    # Fluxo de compra
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.get("https://www.saucedemo.com/cart.html")
    driver.find_element("id", "checkout").click()
    
    # Preenchimento de dados de entrega
    driver.find_element("id", "first-name").send_keys("Tester")
    driver.find_element("id", "last-name").send_keys("Silva")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    
    # Finalização
    driver.find_element("id", "finish").click()
    
    # Validação final (URL de sucesso)
    assert "checkout-complete" in driver.current_url