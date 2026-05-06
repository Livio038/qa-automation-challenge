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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_fluxo_compra_completo(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Tester")
    driver.find_element(By.ID, "last-name").send_keys("QA")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    assert "checkout-complete" in driver.current_url

def test_login_bloqueado(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("locked_out_user", "secret_sauce")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error

def test_login_senha_errada(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "senha_errada")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in error

def test_contador_carrinho_multiplo(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    buttons[0].click()
    buttons[1].click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"

def test_remover_item_carrinho(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    # Verifica se o badge do carrinho sumiu (vazio)
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

def test_ver_detalhes_produto(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    driver.find_element(By.ID, "item_4_title_link").click()
    assert "inventory-item" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "inventory_details_name").is_displayed()