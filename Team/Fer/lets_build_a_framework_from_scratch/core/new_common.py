from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    TimeoutException, InvalidSelectorException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as ec

from Team.Fer.lets_build_a_framework_from_scratch.core.utils import Utils, timer


class TinyCore(Utils):
    DRIVER = None

    def set_chrome_driver(self):
        self.DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def set_edge_driver(self):
        self.DRIVER = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def set_firefox_driver(self):
        self.DRIVER = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def launch_site(self, target_url):
        self.DRIVER.get(target_url)
        self.DRIVER.maximize_window()

    def set_implicit_wait(self, waiting_time):
        self.DRIVER.implicitly_wait(waiting_time)

    def do_click(self, locator):
        self.DRIVER.find_element(By.XPATH, locator).click()

    def efficient_wait_n_do_click(self, locator):
        self.efficient_wait(10, .1).until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def explicit_wait_n_do_click(self, locator):
        WebDriverWait(self.DRIVER, timeout=5).until(ec.element_to_be_clickable((By.XPATH, locator)))
        self.DRIVER.find_element(By.XPATH, locator).click()

    def force_text_value(self, locator, text_to_type):
        self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';", self.DRIVER.find_element(By.XPATH,
                                                                                                          locator))

    def efficient_wait_n_force_text_value(self, locator, text_to_type):
        self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';",
                                   self.efficient_wait(10, .1).until(ec.element_to_be_clickable((By.XPATH, locator))))

    def explicit_wait_n_force_text_value(self, locator, text_to_type):
        WebDriverWait(self.DRIVER, timeout=3).until(ec.element_to_be_clickable((By.XPATH, locator)))
        self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';", self.DRIVER.find_element(By.XPATH,
                                                                                                          locator))

    def type_in_text_field(self, locator, text_to_type):
        self.DRIVER.find_element(By.XPATH, locator).send_keys(text_to_type)

    def efficient_wait_n_type_in_text_field(self, locator, text_to_type):
        self.efficient_wait(10, .1).until(ec.element_to_be_clickable((By.XPATH, locator))).send_keys(text_to_type)

    def explicit_wait_n_type_in_text_field(self, locator, text_to_type):
        WebDriverWait(self.DRIVER, timeout=3).until(ec.element_to_be_clickable((By.XPATH, locator)))
        self.DRIVER.find_element(By.XPATH, locator).send_keys(text_to_type)

    def efficient_wait(self, waiting_time, refresh_frequency):
        return WebDriverWait(self.DRIVER, waiting_time, poll_frequency=refresh_frequency,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def tear_down(self):
        self.DRIVER.quit()


class ImprovedTinyCore(Utils):
    DRIVER = None

    def set_chrome_driver(self):
        self.DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def set_edge_driver(self):
        self.DRIVER = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def set_firefox_driver(self):
        self.DRIVER = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def launch_site(self, target_url):
        self.DRIVER.get(target_url)
        self.DRIVER.maximize_window()

    def set_implicit_wait(self, waiting_time):
        self.DRIVER.implicitly_wait(waiting_time)

    def do_click(self, locator):
        try:
            self.DRIVER.find_element(By.XPATH, locator).click()
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            print("Not able to find an element")

    def fluent_wait_n_do_click(self, locator):
        self.fluent_wait_find_element_by_xpath(locator).click()

    def explicit_wait_n_do_click(self, locator):
        self.explicit_wait_find_element_by_xpath(locator).click()

    def force_text_value(self, locator, text_to_type):
        try:
            self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';", self.DRIVER.find_element(By.XPATH,
                                                                                                              locator))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            print("Not able to find an element")

    def fluent_wait_n_force_text_value(self, locator, text_to_type):
        el = self.fluent_wait_find_element_by_xpath(locator)
        if el is not None:
            self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';", el)

    def explicit_wait_n_force_text_value(self, locator, text_to_type):
        el = self.explicit_wait_find_element_by_xpath(locator)
        if el is not None:
            self.DRIVER.execute_script("arguments[0].value='" + text_to_type + "';", el)

    def type_in_text_field(self, locator, text_to_type):
        try:
            self.DRIVER.find_element(By.XPATH, locator).send_keys(text_to_type)
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            print("Not able to find an element")

    def fluent_wait_n_type_in_text_field(self, locator, text_to_type):
        el = self.fluent_wait_find_element_by_xpath(locator)
        if el is not None:
            el.send_keys(text_to_type)

    def explicit_wait_n_type_in_text_field(self, locator, text_to_type):
        el = self.explicit_wait_find_element_by_xpath(locator)
        if el is not None:
            el.send_keys(text_to_type)

    def fluent_wait(self, waiting_time, refresh_frequency):
        return WebDriverWait(self.DRIVER, waiting_time, poll_frequency=refresh_frequency,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def explicit_wait_find_element_by_xpath(self, locator):
        try:
            return WebDriverWait(self.DRIVER, timeout=3).until(ec.element_to_be_clickable((By.XPATH, locator)))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            return None

    def fluent_wait_find_element_by_xpath(self, locator):
        try:
            return self.fluent_wait(10, .1).until(ec.element_to_be_clickable((By.XPATH, locator)))
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            return None

    def tear_down(self):
        self.DRIVER.quit()
