from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Page:

    @staticmethod
    def set_driver():
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @staticmethod
    def launch_site(driver, base_url="https://www.saucedemo.com/", height=1440, width=1102):
        driver.get(base_url)
        driver.set_window_size(height, width)

    @staticmethod
    def delay_time(waiting_time_value=2):
        time.sleep(waiting_time_value)

    @staticmethod
    def find_text_to_element(driver, by_locator, locator):
        return driver.find_element(by_locator, locator)
    @staticmethod
    def fill_text_to_element(driver, by_locator, locator, text):
        return driver.find_element(by_locator, locator).send_keys(text)

    @staticmethod
    def do_click(driver, by_locator, locator):
        return driver.find_element(by_locator, locator).click()




