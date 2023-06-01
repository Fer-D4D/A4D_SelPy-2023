from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def do_login_external(page_obj, driver, *args):
    print(args)
    print(driver)
    print(page_obj)
    page_obj.fill_text_to_element(driver, args[0], args[1], args[2])
    page_obj.fill_text_to_element(driver, args[3], args[4], args[5])
    page_obj.do_click(driver, args[6], args[7])

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

    def do_login(self, driver, *args):
        print(args)
        self.fill_text_to_element(driver, args[0], args[1], args[2])
        self.fill_text_to_element(driver, args[3], args[4], args[5])
        self.do_click(driver, args[6], args[7])
0

