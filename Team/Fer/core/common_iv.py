import time

from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    InvalidSelectorException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Team.Fer.core.utils import Utils, Using, timer, oneSec


class TinyCore(Utils):
    MAIN_DRIVER = None
    DEFAULT_WAITING_TIME = 5
    DEFAULT_REFRESH_TIME = .33

    def init_web_driver(self, browser=Using.Chrome):
        self.MAIN_DRIVER = self.define_webdriver(browser)

    def get_web_driver(self):
        return self.MAIN_DRIVER

    def launch_site(self, target_url):
        self.MAIN_DRIVER.get(target_url)
        self.MAIN_DRIVER.maximize_window()

    def find_element_by_tiny(self, locator_definition, dynamic_selector_subtext=""):
        byString = self.build_byString(locator_definition, dynamic_selector_subtext)
        if self.validate_object(byString):
            try:
                return self.get_fluent_wait().until(ec.element_to_be_clickable((byString["By"],
                                                                                byString["custom_selector"])))
            except (NoSuchElementException, InvalidSelectorException, TimeoutException):
                print(f"Locator: {byString['custom_selector']} @type {byString['By']} failed")
                return None

    def find_elements_by_tiny(self, locator_definition, dynamic_selector_subtext=""):
        byString = self.build_byString(locator_definition, dynamic_selector_subtext)
        print(f"Custom Locator: {byString['custom_selector']} @type {byString['By']}")
        if self.validate_object(byString):
            try:
                return self.MAIN_DRIVER.find_elements(byString["By"], byString["custom_selector"])
            except (NoSuchElementException, InvalidSelectorException):
                print(f"Locator: {byString['custom_selector']} @type {byString['By']} failed")
                return None

    def set_fake_dropdown_value(self, target_locator, value):
        wElemList = self.find_elements_by_tiny(target_locator)
        for wElem in wElemList:
            re = wElem.text
            if re == value:
                wElem.click()
                print(re)
                break

    def set_orange_fake_dropdown_value(self, gen_target_locator, dropdown_name, dropdown_value):
        wElemList = self.find_elements_by_tiny(gen_target_locator, dropdown_name)
        for wElem in wElemList:
            if wElem.text == dropdown_value:
                wElem.click()

    @oneSec
    def do_click(self, target_locator, generic_component=""):
        try:
            wElement = self.find_element_by_tiny(target_locator, generic_component)
            if self.validate_object(wElement):
                wElement.click()
        except ElementClickInterceptedException:
            time.sleep(.5)
            self.do_click(target_locator, generic_component)
            print("Click Intercepted - re-trying")

    @oneSec
    def fast_fill_field(self, target_locator, fill_text):
        wElement = self.find_element_by_tiny(target_locator)
        if self.validate_object(wElement):
            self.MAIN_DRIVER.execute_script("arguments[0].value='" + fill_text + "';", wElement)

    @oneSec
    def fill_field(self, target_locator, fill_text, generic_component=""):
        wElement = self.find_element_by_tiny(target_locator, generic_component)
        if self.validate_object(wElement):
            wElement.clear()
            wElement.send_keys(fill_text)

    def do_click_and_check(self, target_locator, what_to_check):
        self.do_click(target_locator)
        return self.check_for_element_readiness(what_to_check)

    def check_for_page_readiness(self, trusted_element):
        return self.check_for_element_readiness(trusted_element)

    def check_for_element_readiness(self, trusted_element):
        return self.validate_object(self.find_element_by_tiny(trusted_element))

    def get_fluent_wait(self, waiting_time=DEFAULT_WAITING_TIME, refresh_frequency=DEFAULT_REFRESH_TIME):
        if self.validate_object(self.MAIN_DRIVER):
            return WebDriverWait(self.MAIN_DRIVER, waiting_time, poll_frequency=refresh_frequency,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def tear_down(self):
        self.MAIN_DRIVER.quit()
