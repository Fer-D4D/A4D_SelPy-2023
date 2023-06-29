import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class Using:
    Chrome = "chrome"
    FireFox = "firefox"
    Edge = "edge"


class Utils:
    DEFAULT_SNORING_TIME = 1
    using = Using()

    @staticmethod
    def define_webdriver(browser=Using.Chrome):
        if browser == Using.Edge:
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        if browser == Using.FireFox:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        if browser == Using.Chrome:
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @staticmethod
    def snore(how_long=DEFAULT_SNORING_TIME):
        time.sleep(how_long)
