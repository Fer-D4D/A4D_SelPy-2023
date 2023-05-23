import time

from core.Common_II import TinyCore
from test.Week_05.SauceDemoSite_v2.landing_page import LandingPage
from test.Week_05.SauceDemoSite_v2.login_page import LoginPage


"""
Scenario:
As a standard user I can access the Sauce website and once I am on the home page 
I will be able to both add and remove any number of products to the shopping cart.
"""

# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "chrome"
VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test actions
lets_automate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

global_driver = lets_automate.launch_site(TEST_URL)  # Important step

login_page = LoginPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

login_page.do_login()

landing_page = LandingPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

if landing_page.check_for_login_granted():
    print("Successful Login: Test Passed")
    landing_page.add_item_to_shopping_cart("Sauce Labs Backpack")
    landing_page.sele
    time.sleep(10)
