from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"Δt = {dt}")
        return result

    return wrapper


def oneSec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(1)
        return result

    return wrapper


def twoSec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(2)
        return result

    return wrapper


def sleepy_dog(waiting_time=2):
    for idx in range(1, waiting_time):
        time.sleep(1)


class Using:
    Chrome = "chrome"
    FireFox = "firefox"
    Edge = "Edge"


class Utils:
    GENERIC_TOKEN = "$%$"

    @staticmethod
    def waste_some_time(waiting_time=.1):
        time.sleep(waiting_time)

    def build_byString(self, selector_definition, dynamic_selector_text=""):
        selector_definition = selector_definition.replace(self.GENERIC_TOKEN, dynamic_selector_text)
        if "CSS:" in selector_definition:
            return {"By": "css selector", "custom_selector": selector_definition.replace("CSS:", "")}
        if "ID:" in selector_definition:
            return {"By": "css selector", "custom_selector": selector_definition.replace("ID:", "#")}
        if "XPATH:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("XPATH:", "")}
        if "NAME:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("NAME:", "//*[@name='") + "']"}
        if "LINK_TEXT:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("LINK_TEXT:",
                                                                                  "//a[contains(text(),'") + "']"}

    @staticmethod
    def define_webdriver(browser):
        if browser == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        if browser == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        if browser == "chrome":
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @staticmethod
    def translate_to_boolean(entry_value, baseline_for_true="on"):
        if baseline_for_true.lower() in entry_value.lower():
            return True
        return False

    @staticmethod
    def get_current_ddMMYYYYHHmm():
        now = datetime.now()
        return f"{now.month:02d}/{now.day:02d}/{now.year} {now.hour:02d}:{now.minute:02d}"

    @staticmethod
    def validate_object(object_to_check):
        if object_to_check is None:
            return False
        return True

    @staticmethod
    def compare_two_texts(left_text, right_text):
        return left_text == right_text

    @staticmethod
    def check_for_empty_list(list_to_check):
        return not len(list_to_check) > 0
