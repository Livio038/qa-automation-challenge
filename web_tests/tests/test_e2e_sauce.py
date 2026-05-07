import pytest
import time
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
    # Desativa qualquer interferência de pop-ups ou automação
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_fluxo_compra_completo(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    btn_add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.execute_script("arguments[0].click();", btn_add)
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Tester")
    driver.find_element(By.ID, "last-name").send_keys("QA")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    btn_cont = driver.find_element(By.ID, "continue")
    driver.execute_script("arguments[0].click();", btn_cont)
    wait.until(EC.url_contains("checkout-step-two.html"))
    btn_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    driver.execute_script("arguments[0].click();", btn_finish)
    wait.until(EC.url_contains("checkout-complete"))
    assert "checkout-complete" in driver.current_url

def test_adicionar_e_remover_item(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    
    # Adiciona
    btn_add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.execute_script("arguments[0].click();", btn_add)
    
    # Espera o badge aparecer
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    
    # Remove
    btn_rem = wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
    driver.execute_script("arguments[0].click();", btn_rem)
    
    # Retry logic manual para o badge sumir
    for _ in range(5):
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        if len(badges) == 0:
            break
        time.sleep(1)
    
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

def test_login_usuario_bloqueado(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("locked_out_user", "secret_sauce")
    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))).text
    assert "locked out" in error

def test_login_senha_invalida(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "senha_errada")
    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))).text
    assert "Username and password do not match" in error

def test_validar_contador_carrinho_multiplo(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]")))
    driver.execute_script("arguments[0].click();", btn1)
    time.sleep(0.5)
    btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]")))
    driver.execute_script("arguments[0].click();", btn2)
    badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "2"

def test_navegacao_detalhes_produto(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    link = driver.find_element(By.ID, "item_4_title_link")
    driver.execute_script("arguments[0].click();", link)
    assert "inventory-item.html" in driver.current_url