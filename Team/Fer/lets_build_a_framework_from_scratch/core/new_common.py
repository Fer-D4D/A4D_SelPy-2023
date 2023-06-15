from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TinyCore:
    DRIVER = None

    def set_driver(self):
        self.DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return self.DRIVER

    def do_click(self, locator):
        self.DRIVER.find_element(By.ID, locator).click()
