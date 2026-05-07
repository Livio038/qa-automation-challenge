import pytest
from selenium.webdriver.common.by import By
from web_tests.utils.driver_factory import create_driver
from web_tests.pages.login_page import LoginPage
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    browser = create_driver()
    yield browser
    browser.quit()


@pytest.mark.web
@pytest.mark.e2e
def test_user_can_complete_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.assert_loaded()
    inventory_page.add_two_products()
    assert inventory_page.cart_quantity() == "2"
    inventory_page.go_to_cart()

    cart_page.assert_loaded()
    cart_page.assert_products_quantity(2)
    cart_page.checkout()

    checkout_page.fill_customer_data("Livio", "Junior", "64000-000")
    checkout_page.finish_order()
    checkout_page.assert_order_completed()


@pytest.mark.web
def test_locked_user_cannot_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.error_message()


@pytest.mark.web
def test_invalid_password_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "senha_errada")

    assert "Username and password do not match" in login_page.error_message()


@pytest.mark.web
def test_add_and_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack()

    assert inventory_page.cart_quantity() == "1"

    inventory_page.remove_backpack()
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0


@pytest.mark.web
def test_user_can_open_product_details(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.open_backpack_details()

    assert "inventory-item.html" in driver.current_url
