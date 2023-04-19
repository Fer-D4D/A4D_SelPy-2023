import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def waste_some_time(waiting_time=5):
    time.sleep(waiting_time)


class Common:
    driver = None
    PAGE_TIME_OUT = 15
    HIGHLIGHT_COLOR = "green"
    HIGHLIGHT_BORDER = 3
    HIGHLIGHT_DURATION = 1

    def __init__(self, browser='chrome'):
        self.browser = browser.lower()

    def page_loaded(self, anchor_locator_definition):
        try:
            if "CSS:" in anchor_locator_definition:
                WebDriverWait(self.driver, self.PAGE_TIME_OUT).until(ec.presence_of_element_located(
                    (By.CSS_SELECTOR, anchor_locator_definition.replace("CSS:", ""))))
            if "ID:" in anchor_locator_definition:
                WebDriverWait(self.driver, self.PAGE_TIME_OUT).until(ec.presence_of_element_located(
                    (By.CSS_SELECTOR, anchor_locator_definition.replace("ID:", "#"))))
            if "XPATH:" in anchor_locator_definition:
                WebDriverWait(self.driver, self.PAGE_TIME_OUT).until(ec.presence_of_element_located(
                    (By.XPATH, anchor_locator_definition.replace("XPATH:", ""))))
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")

    def set_webdriver(self):
        if self.browser == "edge":
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        if self.browser == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        return self.driver

    def launch_site_old(self, base_url):
        self.driver = self.set_webdriver()
        self.driver.get(base_url)
        self.driver.maximize_window()

    def launch_site(self, base_url, anchor_locator_definition="//body"):
        self.driver = self.set_webdriver()
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.page_loaded(anchor_locator_definition)
        return self.driver

    def get_element_old(self, locator_type, locator_definition):
        if locator_type.lower() == "css":
            return self.driver.find_element(By.CSS_SELECTOR, locator_definition)
        return self.driver.find_element(By.XPATH, locator_definition)

    def get_element(self, locator_definition):
        if "CSS:" in locator_definition:
            return self.highlight(self.driver.find_element(By.CSS_SELECTOR, locator_definition.replace("CSS:", "")),
                                  self.HIGHLIGHT_DURATION,
                                  self.HIGHLIGHT_COLOR, self.HIGHLIGHT_BORDER)
        if "ID:" in locator_definition:
            return self.highlight(self.driver.find_element(By.CSS_SELECTOR, locator_definition.replace("ID:", "#")),
                                  self.HIGHLIGHT_DURATION,
                                  self.HIGHLIGHT_COLOR, self.HIGHLIGHT_BORDER)
        if "XPATH:" in locator_definition:
            return self.highlight(self.driver.find_element(By.XPATH, locator_definition.replace("XPATH:", "")),
                                  self.HIGHLIGHT_DURATION,
                                  self.HIGHLIGHT_COLOR, self.HIGHLIGHT_BORDER)
        if "NAME:" in locator_definition:
            return self.highlight(
                self.driver.find_element(By.XPATH, locator_definition.replace("NAME:", "//*[@name='") +
                                         "']"),
                self.HIGHLIGHT_DURATION,
                self.HIGHLIGHT_COLOR, self.HIGHLIGHT_BORDER)

    def do_click_old(self, locator_type, locator_definition):
        self.get_element_old(locator_type, locator_definition).click()

    def do_click(self, locator_definition):
        ActionChains(self.driver).move_to_element(self.get_element(locator_definition)).click().perform()

    def fill_input_text_old(self, locator_type, locator_definition, text):
        self.get_element_old(locator_type, locator_definition).send_keys(text)

    def fill_input_text(self, locator_definition, text):
        self.get_element(locator_definition).send_keys(text)

    def get_text_from_element(self, locator_definition):
        try:
            return self.get_element(locator_definition).text
        except NoSuchElementException:
            pass

    def highlight(self, element, effect_time, color, border):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)
        return element

    def select_dropdown_option(self, locator_definition, text_value):
        Select(self.get_element(locator_definition)).select_by_visible_text(text_value)
