from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class BasePage:

    def __init__(self):
        self.DRIVER = self.set_driver()

    @staticmethod
    def set_driver():
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_set_driver(self):
        return self.DRIVER

    def launch_site(self, base_url="https://www.saucedemo.com/", height=1440, width=1102):
        self.DRIVER.get(base_url)
        self.DRIVER.set_window_size(height, width)

    def gimme_element(self, by_locator, locator):
        return self.DRIVER.find_element(by_locator, locator)

    def fill_text_to_element(self, by_locator, locator, text):
        self.gimme_element(by_locator, locator).send_keys(text)

    def do_click(self, by_locator, locator):
        return self.gimme_element(by_locator, locator).click()

