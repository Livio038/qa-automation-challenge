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
    
    assert "checkout-complete" in driver.current_url
