import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")

    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1366,768")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver