import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_tests.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    # Mantemos a espera implícita como segurança extra
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    
    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    # Adicionar ao carrinho e Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    
    # Informações de envio
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Tester")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # O PONTO CRÍTICO: Esperar o botão 'finish' aparecer e ser clicável
    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()
    
    # Validação
    wait.until(EC.url_contains("checkout-complete"))
    assert "checkout-complete" in driver.current_url