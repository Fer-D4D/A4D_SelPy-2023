import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSelectorException
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


def get_by_string(locator_definition):
    if "CSS:" in locator_definition:
        return ["css selector", locator_definition.replace("CSS:", "")]
    if "ID:" in locator_definition:
        return ["css selector", locator_definition.replace("ID:", "#")]
    if "XPATH:" in locator_definition:
        return ["xpath", locator_definition.replace("XPATH:", "")]
    if "NAME:" in locator_definition:
        return ["xpath", locator_definition.replace("NAME:", "//*[@name='") + "']"]
    if "LINK_TEXT:" in locator_definition:
        return ["xpath", locator_definition.replace("LINK_TEXT:", "//a[contains(text(),'") + "']"]


class Common:
    driver = None
    PAGE_TIME_OUT = 15
    HIGHLIGHT_COLOR = "green"
    HIGHLIGHT_BORDER = 3
    HIGHLIGHT_DURATION = 1
    VIEWER_MODE = False
    VIEWER_MODE_TIME = 1
    HIGHLIGHT_MODE = False
    SELENIUM_WEBELEMENT_TYPE = 'selenium.webdriver.remote.webelement.WebElement'

    def __init__(self, browser='chrome', viewer_mode=False):
        self.browser = browser.lower()
        self.VIEWER_MODE = viewer_mode

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
        if self.VIEWER_MODE:
            waste_some_time(self.VIEWER_MODE_TIME)
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
        if "LINK_TEXT:" in locator_definition:
            return self.highlight(
                self.driver.find_element(By.XPATH, locator_definition.replace("LINK_TEXT:", "//a[contains(text(),'") +
                                         "')]"),
                self.HIGHLIGHT_DURATION,
                self.HIGHLIGHT_COLOR, self.HIGHLIGHT_BORDER)

    def get_element_ref(self, locator_definition):
        if self.VIEWER_MODE:
            waste_some_time(self.VIEWER_MODE_TIME)
        by_string = get_by_string(locator_definition)
        element = self.driver.find_element(by_string[0], by_string[1])
        return element

    def get_element_by_text(self, locator_definition, target_text):
        element_list = self.driver.find_elements(By.CSS_SELECTOR, locator_definition.replace("CSS:", ""))
        for element in element_list:
            print("<" + element.text + "> is not the target text. Trying next!")
            if element.text == target_text:
                print("<" + element.text + "> target text found.")
                return element

    def do_click_old(self, locator_type, locator_definition):
        self.get_element_old(locator_type, locator_definition).click()

    def do_click(self, locator_definition):
        ActionChains(self.driver).move_to_element(self.get_element(locator_definition)).click().perform()

    def do_click_from_options(self, locator_definitions):
        for option in locator_definitions:
            try:
                self.do_click(option)
                print("<" + option + "> Selector found")
                return True
            except NoSuchElementException:
                print("<" + option + "> Selector not found trying next")
            except InvalidSelectorException:
                print("<" + option + "> Selector is invalid please check it out.")

    def do_click_by_text(self, ambiguous_locator_definition, target_text):
        ActionChains(self.driver).move_to_element(self.get_element_by_text(ambiguous_locator_definition, target_text)). \
            click().perform()

    def fill_input_text_old(self, locator_type, locator_definition, text):
        self.get_element_old(locator_type, locator_definition).send_keys(text)

    def fill_input_text(self, locator_definition, text):
        element = self.get_element(locator_definition)
        element.clear()
        element.clear()
        element.send_keys(text)

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

    def page_back(self):
        if self.VIEWER_MODE:
            waste_some_time(self.VIEWER_MODE_TIME)
        self.driver.execute_script("window.history.go(-1)")

    def switch_browser_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        if self.VIEWER_MODE:
            waste_some_time(self.VIEWER_MODE_TIME)
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def get_current_tab(self):
        return self.driver.current_window_handle
