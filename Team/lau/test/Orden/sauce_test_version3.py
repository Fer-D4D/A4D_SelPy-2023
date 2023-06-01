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

    def __init__(self):
        self.DRIVER = self.set_driver()
        print("Genere una clase y un driver")

    @staticmethod
    def set_driver():
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_set_driver(self):
        return self.DRIVER

    def launch_site(self, base_url="https://www.saucedemo.com/", height=1440, width=1102):
        self.DRIVER.get(base_url)
        self.DRIVER.set_window_size(height, width)

    @staticmethod
    def delay_time(waiting_time_value=2):
        time.sleep(waiting_time_value)

    def find_text_to_element(self, by_locator, locator):
        return self.DRIVER.find_element(by_locator, locator)

    def fill_text_to_element(self, by_locator, locator, text):
        self.DRIVER.find_element(by_locator, locator).send_keys(text)

    def do_click(self, by_locator, locator):
        return self.DRIVER.find_element(by_locator, locator).click()

    def do_login(self, *args):
        print(args)
        self.fill_text_to_element(self.DRIVER, args[0], args[1],)
        self.fill_text_to_element(self.DRIVER, args[2], args[3],)
        self.do_click(self.DRIVER, args[4])


0
