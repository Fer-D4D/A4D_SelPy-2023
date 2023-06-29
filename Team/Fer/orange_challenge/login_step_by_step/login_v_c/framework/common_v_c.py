from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Team.Fer.orange_challenge.login_step_by_step.login_v_c.framework.utils import Utils, Using


class TinyCore(Utils):
    MAIN_DRIVER = None
    DEFAULT_WAITING_TIME = 5
    DEFAULT_REFRESH_TIME = .1

    def init_web_driver(self, browser=Using.Chrome):
        self.MAIN_DRIVER = self.define_webdriver(browser)

    def get_web_driver(self):
        return self.MAIN_DRIVER

    def launch_site(self, target_url):
        self.MAIN_DRIVER.get(target_url)
        self.MAIN_DRIVER.maximize_window()

    def wait_for_page_readiness(self, xpath_trusted_locator):
        self.get_fluent_wait().until(expected_conditions.element_to_be_clickable
                                     ((By.XPATH, xpath_trusted_locator)))

    def tear_down(self):
        self.snore(2)
        self.MAIN_DRIVER.quit()

    def get_fluent_wait(self, waiting_time=DEFAULT_WAITING_TIME, refresh_frequency=DEFAULT_REFRESH_TIME):
        return WebDriverWait(self.MAIN_DRIVER, waiting_time, poll_frequency=refresh_frequency,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def custom_find_element_1st_approach(self, custom_locator):
        if "CSS:" in custom_locator:
            return self.MAIN_DRIVER.find_element("css selector", custom_locator.replace("CSS:", ""))
        if "ID:" in custom_locator:
            return self.MAIN_DRIVER.find_element("css selector", custom_locator.replace("ID:", "#"))
        if "XPATH:" in custom_locator:
            return self.MAIN_DRIVER.find_element("xpath", custom_locator.replace("XPATH:", ""))
        if "NAME:" in custom_locator:
            return self.MAIN_DRIVER.find_element("xpath", custom_locator.replace("NAME:", "//*[@name='") + "']")
        if "LINK_TEXT:" in custom_locator:
            return self.MAIN_DRIVER.find_element("xpath", custom_locator.replace("LINK_TEXT:",
                                                                                 "//a[contains(text(),'") + "']")
