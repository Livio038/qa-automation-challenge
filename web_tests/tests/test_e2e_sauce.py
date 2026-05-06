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
    """Cenário 1: Fluxo de compra de ponta a ponta (Happy Path)"""
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    # Adicionando ao carrinho
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    
    # Navegação para o carrinho
    shopping_cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    shopping_cart.click()
    
    # Clicar no Checkout - Usando espera explícita para garantir a transição
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()
    
    # Formulário de checkout - Agora com garantia de que a página mudou
    first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    first_name_field.send_keys("Tester")
    
    driver.find_element(By.ID, "last-name").send_keys("QA")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # Finalização
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    
    # Validação final
    wait.until(EC.url_contains("checkout-complete"))
    assert "checkout-complete" in driver.current_url

def test_login_usuario_bloqueado(driver):
    """Cenário 2: Validação de erro para usuário bloqueado"""
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("locked_out_user", "secret_sauce")
    
    error_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error_text

def test_login_senha_invalida(driver):
    """Cenário 3: Validação de erro para credenciais incorretas"""
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "senha_errada")
    
    error_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in error_text

def test_adicionar_e_remover_item(driver):
    """Cenário 4: Validação de adição e remoção dinâmica de itens"""
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    
    # Adiciona e depois remove
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # Verifica se o contador do carrinho desapareceu
    badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badge) == 0

def test_validar_contador_carrinho_multiplo(driver):
    """Cenário 5: Verifica se o contador acumula itens corretamente"""
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    
    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    buttons[0].click()
    buttons[1].click()
    
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"

def test_navegacao_detalhes_produto(driver):
    """Cenário 6: Valida se a página de detalhes do produto carrega"""
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    
    driver.find_element(By.ID, "item_4_title_link").click()
    assert "inventory-item.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "inventory_details_name").is_displayed()