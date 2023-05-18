import time

from selenium.common import NoSuchElementException

from core.Common_II import TinyCore, waste_some_time
from test.Week_04.SauceDemoSite.login_page import LoginPage
from test.Week_04.SauceDemoSite.landing_page import LandingPage

"""
Scenario:
As a standard user I can access the Sauce website and once I am on the home page 
I will be able to both add and remove any number of products to the shopping cart.
"""

# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "firefox"
VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used
TEST_URL_B = "https://duckduckgo.com/"

DUCK_DUCK_GO_SEARCH_FORM = "//*[@id='searchbox_input']"
SAUCE_USER_NAME = "user-name"


def name_str(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def print_helper(driver_list):
    str_to_print = ""
    for driver in driver_list:
        str_to_print = str_to_print + "Driver <" + name_str(driver, globals())[0] + "> has a " + \
                       str(driver).replace("<selenium.webdriver.firefox.webdriver.WebDriver (", "")
        str_to_print = str_to_print.replace(")>", " | ")
    print(str_to_print)


# Test actions
lets_automate_sauce = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
lets_automate_duckDuckGo = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

driver_from_sauce = lets_automate_sauce.launch_site(TEST_URL)
driver_from_ducky = lets_automate_duckDuckGo.launch_site(TEST_URL_B)
print_helper([driver_from_sauce, driver_from_ducky])

waste_some_time(3)

driver_from_sauce.find_element("id", SAUCE_USER_NAME).send_keys("lets_automate_sauce")
driver_from_ducky.find_element("xpath", DUCK_DUCK_GO_SEARCH_FORM).send_keys("lets_automate_duckDuckGo")


try:
    driver_from_ducky.find_element("id", SAUCE_USER_NAME).clear()
except NoSuchElementException:
    print("Are you using Sauce driver to work in Duck Duck go?")

# Remember that even if both drivers are obtained in a similar way, they are still independent entities.
# So the Willow driver is only aware of what happens in the browser that was launched for it.

counselor_driver = driver_from_ducky
print_helper([driver_from_sauce, driver_from_ducky, counselor_driver])
waste_some_time(2)

try:
    counselor_driver.find_element("xpath", DUCK_DUCK_GO_SEARCH_FORM).clear()
except NoSuchElementException:
    print("Are you using Sauce driver to work in Duck Duck go?")

try:
    driver_from_ducky.find_element("id", SAUCE_USER_NAME).clear()
except NoSuchElementException:
    print("Are you using DuckDuckGo driver to work in Sauce")

driver_from_ducky = driver_from_sauce

print_helper([driver_from_sauce, driver_from_ducky, counselor_driver])
driver_from_ducky.find_element("id", SAUCE_USER_NAME).clear()

driver_from_ducky = counselor_driver

print_helper([driver_from_sauce, driver_from_ducky, counselor_driver])
