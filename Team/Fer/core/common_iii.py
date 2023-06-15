from Team.Fer.core.utils import Utils, timer
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException, TimeoutException, \
    ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support import expected_conditions as ec


class TinyCore(Utils):
    DRIVER = None
    BROWSER = 'chrome'
    TEST_URL = ""

    VIEWER_MODE = False
    VERBOSE_MODE = False
    HIGHLIGHT_MODE = False
    FLOW_CONTROL_FLAG = True

    DEFAULT_TRUSTED_KEY_SELECTOR = "XPATH://body"

    PAGE_TIME_OUT = 15
    FLUENT_WAIT_TIMEOUT = 5
    FLUENT_WAIT_FREQ = .1

    def __init__(self, test_url,
                 browser='chrome',
                 viewer_mode="Viewer-Mode-OFF",
                 verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        self.TEST_URL = test_url
        self.BROWSER = browser.lower()
        self.VIEWER_MODE = self.translate_to_boolean(viewer_mode)
        self.VERBOSE_MODE = self.translate_to_boolean(verbose_mode)
        self.HIGHLIGHT_MODE = self.translate_to_boolean(highlight_mode)

    def define_browser(self, browser='chrome'):
        self.BROWSER = browser.lower()

    def set_viewer_mode(self, viewer_mode="Viewer-Mode-OFF"):
        self.VIEWER_MODE = self.translate_to_boolean(viewer_mode)

    def set_verbose_mode(self, verbose_mode="Verbose-Mode-OFF"):
        self.VERBOSE_MODE = self.translate_to_boolean(verbose_mode)

    def set_highlight_mode(self, highlight_mode="Verbose-Mode-OFF"):
        self.HIGHLIGHT_MODE = self.translate_to_boolean(highlight_mode)

    def update_flow_control_flag(self, new_state):
        self.FLOW_CONTROL_FLAG = new_state

    def define_webdriver(self):
        if self.BROWSER == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        if self.BROWSER == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        if self.BROWSER == "brave":
            return webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def start_driver(self):
        self.DRIVER = self.define_webdriver()

    def get_driver(self):
        return self.DRIVER

    def launch_site(self, base_url, trusted_key_selector=DEFAULT_TRUSTED_KEY_SELECTOR, dynamic_selector_text=""):
        if self.validate_object(self.DRIVER):
            self.DRIVER.get(base_url)
            self.DRIVER.maximize_window()
            return self.is_page_ready(trusted_key_selector, dynamic_selector_text)

    def get_element(self, selector_definition, dynamic_selector_text="", waiting_time=FLUENT_WAIT_TIMEOUT):
        wait = WebDriverWait(self.DRIVER, waiting_time, poll_frequency=self.FLUENT_WAIT_FREQ,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        by_string = self.make_required_byString(selector_definition, dynamic_selector_text)
        print(by_string)
        try:
            element = wait.until(ec.element_to_be_clickable((by_string["By"], by_string["custom_selector"])))
            return element
        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            return None

    def get_list_of_elements(self, selector_definition, dynamic_selector_text=""):
        by_string = self.make_required_byString(selector_definition, dynamic_selector_text)
        return self.DRIVER.find_elements(by_string["By"], by_string["custom_selector"])

    def is_page_ready(self, trusted_key_selector=DEFAULT_TRUSTED_KEY_SELECTOR, dynamic_selector_text=""):
        self.update_flow_control_flag(self.validate_object(self.DRIVER) and self.validate_object(
            self.get_element(trusted_key_selector, dynamic_selector_text)))
        return self.FLOW_CONTROL_FLAG

    def do_click(self, selector_definition, dynamic_selector_text=""):
        element = self.get_element(selector_definition, dynamic_selector_text)
        if self.validate_object(element):
            element.click()
            return element

    def do_click_and_check(self, action_selector_definition,
                           target_selector_definition,
                           dynamic_action_selector_text="",
                           dynamic_target_selector_text=""):
        self.update_flow_control_flag(self.FLOW_CONTROL_FLAG
                                      and self.validate_object(self.do_click(action_selector_definition,
                                                                             dynamic_action_selector_text))
                                      and self.validate_object(self.get_element(target_selector_definition,
                                                                                dynamic_target_selector_text)))
        return self.FLOW_CONTROL_FLAG

    def get_text_from_element(self, selector_definition, dynamic_selector_text=""):
        element = self.get_element(selector_definition, dynamic_selector_text)
        if self.validate_object(element):
            return element.text

    def get_text_from_input_form(self, selector_definition, dynamic_selector_text=""):
        element = self.get_element(selector_definition, dynamic_selector_text)
        if self.validate_object(element):
            return element.get_attribute("value")

    def fill_form_element(self, selector_definition, text_to_enter, dynamic_selector_text=""):
        element = self.get_element(selector_definition, dynamic_selector_text)
        if self.validate_object(element):
            element.click()
            element.clear()
            element.send_keys(text_to_enter)
            return element

    def fill_form_element_and_check(self,
                                    selector_definition,
                                    text_to_enter,
                                    dynamic_selector_text=""):
        self.update_flow_control_flag(self.FLOW_CONTROL_FLAG
                                      and self.validate_object(self.fill_form_element(selector_definition,
                                                                                      text_to_enter,
                                                                                      dynamic_selector_text))
                                      and self.compare_two_texts(text_to_enter,
                                                                 self.get_text_from_input_form(selector_definition,
                                                                                               dynamic_selector_text)))
        # print(f"Text -> { self.get_text_from_input_form(selector_definition,dynamic_selector_text)}")
        return self.FLOW_CONTROL_FLAG
