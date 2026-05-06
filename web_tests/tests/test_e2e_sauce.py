import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from web_tests.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080") # Garante que os botões não fiquem escondidos
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15) # Aumentamos um pouco o tempo de espera
    
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    # Adicionar ao carrinho e navegar clicando (mais estável no CI)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    
    # Preenchimento de dados
    driver.find_element(By.ID, "first-name").send_keys("Tester")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # Finalização
    driver.find_element(By.ID, "finish").click()
    
    # Validação
    assert "checkout-complete" in driver.current_url