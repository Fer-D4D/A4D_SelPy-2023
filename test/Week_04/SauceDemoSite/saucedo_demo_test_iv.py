import time

from core.Common_II import TinyCore
from test.Week_04.SauceDemoSite.login_page import LoginPage
from test.Week_04.SauceDemoSite.landing_page import LandingPage

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
# we need to set our login page class
login_page = LoginPage(global_driver)

# below LoginPage method perform the whole login process
login_page.do_login()

# no we need to set our landing page class
landing_page = LandingPage(global_driver)
landing_page.set_viewer_mode("ON")

if landing_page.check_expected_text("Swag Labs"):
    print("Successful Login: Test Passed")
    print("Number of items in the shopping cart = " + str(landing_page.check_shopping_cart()))
    landing_page.add_item_to_shopping_cart(landing_page.get_selector("SauceLabsBackPack_AddToCart_Button"))
    print("Number of items in the shopping cart = " + str(landing_page.check_shopping_cart()))
    landing_page.add_item_to_shopping_cart(landing_page.gen_item_selector("Sauce Labs Bike Light", "add"))
    landing_page.add_item_to_shopping_cart(landing_page.gen_item_selector("Sauce Labs Bolt T-Shirt", "add"))
    print("Number of items in the shopping cart = " + str(landing_page.check_shopping_cart()))
    landing_page.remove_item_from_shopping_cart(landing_page.get_selector("SauceLabsBackPack_Remove_Button"))
    landing_page.remove_item_from_shopping_cart(landing_page.gen_item_selector("Sauce Labs Bolt T-Shirt", "remove"))
    print("Number of items in the shopping cart = " + str(landing_page.check_shopping_cart()))
