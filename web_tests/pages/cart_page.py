from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CHECKOUT = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def assert_loaded(self):
        assert self.text_of(self.TITLE) == "Your Cart"

    def assert_products_quantity(self, expected_quantity):
        products = self.driver.find_elements(*self.CART_ITEMS)
        assert len(products) == expected_quantity

    def checkout(self):
        self.click(self.CHECKOUT)
