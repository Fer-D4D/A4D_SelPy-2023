from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class Page:

    Driver = None

    # def __init__(self):
    #     self.Driver = self.set_driver()
    #     print("Driver created")
    def create_driver(self):
        self.Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def set_driver(self, InDriver):
        self.Driver = InDriver

    def get_driver(self):
        return self.Driver

    def launch_site(self, base_url="https://www.saucedemo.com/", height=1440, width=1102):
        self.Driver.get(base_url)
        self.Driver.set_window_size(height, width)

    @staticmethod
    def delay_time(waiting_time_value=2):
        time.sleep(waiting_time_value)

    def find_text_to_element(self, by_locator, locator):
        return self.Driver.find_element(by_locator, locator)

    def fill_text_to_element(self, by_locator, locator, text):
        return self.Driver.find_element(by_locator, locator).send_keys(text)

    def do_click(self, by_locator, locator):
        return self.Driver.find_element(by_locator, locator).click()

    def get_text_to_element(self, by_locator, locator):
       return self.Driver.find_element(by_locator, locator).text

    # def do_login(self, *args):
    #     print(args)
    #     self.fill_text_to_element(args[0], args[1], args[2])
    #     self.fill_text_to_element(args[3], args[4], args[5])
    #     self.do_click(args[6], args[7])
0

