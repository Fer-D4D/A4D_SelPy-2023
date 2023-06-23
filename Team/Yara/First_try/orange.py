import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
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

    def login_success(self,locator,user,locator_pass,password,locator_button):
        try:
            self.DRIVER.find_element(By.NAME,locator).send_keys(user)
            self.DRIVER.find_element(By.NAME,locator_pass).send_keys(password)
            self.DRIVER.find_element(By.CSS_SELECTOR,locator_button).click()

        except ElementClickInterceptedException:

            print("Re-clicking")

    def oneSec(func):
        def wrapper(*args, **kwargs):
            time.sleep(1)
            result = func(*args, **kwargs)
            return result

        return wrapper














