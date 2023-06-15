import time

import pytest_check as check

from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_complete import CheckoutComplete
from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_overview import CheckoutOverview
from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_your_information import CheckoutYourInformation
from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage
from Team.Fer.Sauce.Second_Challenge_Week_05.login_page import LoginPage
from Team.Fer.Sauce.Second_Challenge_Week_05.your_cart import YourCart


class TestData:
    TEST_URL = "https://www.saucedemo.com/"
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used
    TESTING_ITEM_NAMES = ["Sauce Labs Backpack",
                          "Sauce Labs Fleece Jacket"]
    TEST_SUMMARY = "Sauce Purchasing Functionality"


login_page = LoginPage(TestData.BROWSER,
                       TestData.VIEWER_MODE,
                       TestData.VERBOSE_MODE,
                       TestData.HIGHLIGHT_MODE)

test_driver = login_page.launch_site(TestData.TEST_URL)

print(login_page.validate_login())

login_page.do_login()

if login_page.validate_login() > 0:
    print("Test passed: Error message is present")
print(login_page.validate_login())

time.sleep(0)
