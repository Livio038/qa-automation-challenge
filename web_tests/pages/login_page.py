from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_field = (By.ID, "user-name")
        self.pass_field = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, user, password):
        self.driver.find_element(*self.user_field).send_keys(user)
        self.driver.find_element(*self.pass_field).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
