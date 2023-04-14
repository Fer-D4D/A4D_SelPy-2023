import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def fill_input_by_xpath(driver, locator, text):
    driver.find_element(By.XPATH, locator).send_keys(text)
    print(driver.title)


def do_click_by_xpath(driver, locator):
    driver.find_element(By.XPATH, locator).click()
    print(driver.title)


def get_text_from_element_by_xpath(driver, locator):
    return driver.find_element(By.XPATH, locator).text


def waste_some_time(waiting_time=5):
    time.sleep(waiting_time)


class Common:

    def __init__(self, browser='chrome'):
        self.browser = browser.lower()

    def set_webdriver(self):
        if self.browser == "edge":
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        if self.browser == "firefox":
            return webdriver.Firefox(GeckoDriverManager().install())
        return webdriver.Chrome(ChromeDriverManager().install())

    def go_url(self, base_url):
        driver = self.set_webdriver()
        driver.get(base_url)
        driver.maximize_window()
        return driver
