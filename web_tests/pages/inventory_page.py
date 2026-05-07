from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT_ADD = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BACKPACK_REMOVE = (By.ID, "remove-sauce-labs-backpack")
    BACKPACK_DETAIL = (By.ID, "item_4_title_link")

    def assert_loaded(self):
        assert self.text_of(self.TITLE) == "Products"

    def add_backpack(self):
        self.click(self.BACKPACK_ADD)

    def add_two_products(self):
        self.click(self.BACKPACK_ADD)
        self.click(self.BIKE_LIGHT_ADD)

    def remove_backpack(self):
        self.click(self.BACKPACK_REMOVE)

    def cart_quantity(self):
        return self.text_of(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART)

    def open_backpack_details(self):
        self.click(self.BACKPACK_DETAIL)
