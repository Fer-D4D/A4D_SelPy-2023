from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TinyCore:
    Driver = None

    def browsers(self):
        self.DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return self.DRIVER

    def set_page(self):
        self.DRIVER.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        return self.DRIVER


