import pytest

from web_tests.pages.login_page import LoginPage
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage


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
    inventory_page.add_backpack()
    assert inventory_page.cart_quantity() == "1"
    inventory_page.go_to_cart()

    cart_page.assert_loaded()
    cart_page.assert_products_quantity(1)
    cart_page.checkout()

    checkout_page.fill_customer_data("Livio", "Junior", "64000-000")
    checkout_page.finish_order()
    checkout_page.assert_order_completed()


@pytest.mark.web
def test_locked_user_cannot_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.error_message().lower()


@pytest.mark.web
def test_invalid_password_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "senha_errada")

    assert "username and password do not match" in login_page.error_message().lower()