import time
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support import expected_conditions as ec


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


class TinyCore:
    driver = None
    PAGE_TIME_OUT = 15
    HIGHLIGHT_COLOR = "green"
    HIGHLIGHT_BORDER = 3
    HIGHLIGHT_DURATION = 1
    VIEWER_MODE = "OFF"
    VIEWER_MODE_TIME = 1
    VERBOSE_MODE = "OFF"
    HIGHLIGHT_MODE = "OFF"
    DEFAULT_TRUSTED_KEY_ELEMENT = "XPATH://body"

    def __init__(self, browser='chrome', viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        self.browser = browser.lower()
        self.VIEWER_MODE = viewer_mode
        self.VERBOSE_MODE = verbose_mode
        self.HIGHLIGHT_MODE = highlight_mode

    def viewer_mode(self):
        if "on" in self.VIEWER_MODE.lower():
            waste_some_time(self.VIEWER_MODE_TIME)

    def verbose_mode(self, verbose_msg):
        if "on" in self.VERBOSE_MODE.lower():
            print(verbose_msg)

    def highlight_mode(self, element):
        if "on" in self.HIGHLIGHT_MODE.lower():
            original_style = element.get_attribute('style')
            self.apply_style(element, "border: {0}px solid {1};".format(self.HIGHLIGHT_BORDER, self.HIGHLIGHT_COLOR))
            time.sleep(self.HIGHLIGHT_DURATION)
            self.apply_style(element, original_style)

    def apply_style(self, element, style):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)

    def get_element(self, locator_definition):
        self.viewer_mode()
        by_string = get_by_string(locator_definition)
        try:
            element = self.driver.find_element(by_string[0], by_string[1])
            self.highlight_mode(element)
            self.verbose_mode("<" + locator_definition + "> Selector found!")
            return element
        except NoSuchElementException:
            self.verbose_mode("<" + locator_definition + "> Selector not found, please check it out")
        except InvalidSelectorException:
            self.verbose_mode("<" + locator_definition + "> Selector is invalid please check it out.")

    def set_webdriver(self):
        if self.browser == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        if self.browser == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        if self.browser == "brave":
            return webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def is_page_load(self, trusted_key_element=DEFAULT_TRUSTED_KEY_ELEMENT):
        by_string = get_by_string(trusted_key_element)
        try:
            WebDriverWait(self.driver, self.PAGE_TIME_OUT).until(ec.presence_of_element_located((by_string[0],
                                                                                                 by_string[1])))
        except TimeoutException:
            self.verbose_mode("Timed out waiting for page to load, please check the trusted key element <"
                              + trusted_key_element + "> provided")
        finally:
            self.verbose_mode("The trusted key element <" + trusted_key_element + "> provided was found, so we can "
                                                                                  "assume that the page has been "
                                                                                  "loaded.")

    def launch_site(self, base_url, anchor_locator_definition=DEFAULT_TRUSTED_KEY_ELEMENT):
        self.driver = self.set_webdriver()
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.is_page_load(anchor_locator_definition)
        return self.driver

    def do_click(self, locator_definition):
        try:
            ActionChains(self.driver).move_to_element(self.get_element(locator_definition)).click().perform()
        except AttributeError:
            self.verbose_mode("<" + locator_definition + "> does not work.")

    def fill_input_text(self, locator_definition, text):
        element = self.get_element(locator_definition)
        element.clear()
        element.send_keys(text)
