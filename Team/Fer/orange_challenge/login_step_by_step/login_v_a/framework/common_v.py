from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Team.Fer.orange_challenge.login_step_by_step.login_v_a.framework.utils import Utils, Using


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
