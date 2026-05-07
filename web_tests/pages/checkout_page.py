from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_TITLE = (By.CLASS_NAME, "complete-header")

    def fill_customer_data(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    def finish_order(self):
        self.click(self.FINISH)

    def assert_order_completed(self):
        assert self.text_of(self.COMPLETE_TITLE) == "Thank you for your order!"
