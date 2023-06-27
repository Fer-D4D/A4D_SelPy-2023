from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import ElementClickInterceptedException
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
#ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException,TimeoutException, InvalidSelectorException,
import time

class Page:

    Driver = None

    # def __init__(self):
    #     self.Driver = self.set_driver()
    #     print("Driver created")
    def create_driver(self):
        self.Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    def create_edge_driver(self):
        self. Driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def create_firefox_driver(self):
        self. Driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

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
        self.Driver.find_element(by_locator, locator).send_keys(text)

    def do_click(self, by_locator, locator):
        try:
            self.Driver.find_element(by_locator, locator).click()
        except ElementClickInterceptedException:
            self.delay_time(1)
            self.do_click(by_locator, locator)

    def get_text_to_element(self, by_locator, locator):
        return self.Driver.find_element(by_locator, locator).text

    def back_to_page(self):
        self.Driver.back()

    def refresh_to_page(self):
        self.Driver.refresh()
    def is_selected(self, by_locator, locator):
        self.Driver.find_element(by_locator, locator).is_selected()

    def choose_dropdown_option(self, *args):
        self.do_click(args[0], args[1]),
        self.fill_text_to_element(args[2], args[3], args[4]),
        self.do_click(args[5], args[6])

    def set_timeout_page(self):
        self.Driver.set_page_load_timeout(.20)



    # def do_login(self, *args):
    #     print(args)
    #     self.fill_text_to_element(args[0], args[1], args[2])
    #     self.fill_text_to_element(args[3], args[4], args[5])
    #     self.do_click(args[6], args[7])