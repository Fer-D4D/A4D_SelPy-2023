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
    VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used
    TESTING_ITEM_NAMES = ["Sauce Labs Backpack",
                          "Sauce Labs Fleece Jacket"]
    TEST_SUMMARY = "Sauce Purchasing Functionality"


"""
Function: Validate the functionality to make a purchase on the Sauce site.

Given the user is already registered on the Sauce website.
Given that the user is able to log in to the Sauce site.
Given that the user has added a backpack and a jacket to the shopping cart.
Given that the user checks the contents of his shopping cart.
And the user clicks on the Checkout button
Then the "Checkout: Your information" screen is displayed.
And the user will be able to enter his data
And the user can proceed to the "Checkout: Summary" by clicking on the Continue button
And the user validates that the total of the purchase, taxes included, is correct.
Finally, the user must place the order by clicking the Finish button.
"""

login_page = LoginPage(TestData.BROWSER,
                       TestData.VIEWER_MODE,
                       TestData.VERBOSE_MODE,
                       TestData.HIGHLIGHT_MODE)

test_driver = login_page.launch_site(TestData.TEST_URL)

test_doc = login_page.create_test_doc()

landing_page = LandingPage(test_driver,
                           TestData.VIEWER_MODE,
                           TestData.VERBOSE_MODE,
                           TestData.HIGHLIGHT_MODE)

your_cart = YourCart(test_driver,
                     TestData.VIEWER_MODE,
                     TestData.VERBOSE_MODE,
                     TestData.HIGHLIGHT_MODE)

checkout_your_information = CheckoutYourInformation(test_driver,
                                                    TestData.VIEWER_MODE,
                                                    TestData.VERBOSE_MODE,
                                                    TestData.HIGHLIGHT_MODE)

checkout_overview = CheckoutOverview(test_driver,
                                     TestData.VIEWER_MODE,
                                     TestData.VERBOSE_MODE,
                                     TestData.HIGHLIGHT_MODE)

checkout_complete = CheckoutComplete(test_driver,
                                     TestData.VIEWER_MODE,
                                     TestData.VERBOSE_MODE,
                                     TestData.HIGHLIGHT_MODE)


def test_user_is_able_to_login():
    login_page.add_step_to_test_doc(test_doc, "Go Sauce site and enter credentials. ",
                                    login_page.get_full_screenshot())
    login_page.do_login()
    check.is_true(landing_page.check_for_login_granted(), "Login granted test - Failed ")
    login_page.add_step_to_test_doc(test_doc, "User is able to login Sauce, Home page is displayed.",
                                    login_page.get_full_screenshot())


def test_user_adding_items():
    landing_page.add_items_to_shopping_cart_from_list(TestData.TESTING_ITEM_NAMES)
    login_page.add_step_to_test_doc(test_doc, "User has added a backpack and a jacket to the shopping cart.",
                                    login_page.get_full_screenshot())
    check.is_true(landing_page.compare_lists(landing_page.get_added_item_names_list(), TestData.TESTING_ITEM_NAMES))


def test_user_can_checks_shopping_cart_contents():
    landing_page.proceed_to_your_cart_page()
    login_page.add_step_to_test_doc(test_doc, " User checks the contents of his shopping cart.",
                                    login_page.get_full_screenshot())
    check.is_true(your_cart.compare_lists(landing_page.get_added_item_names_list(), TestData.TESTING_ITEM_NAMES))


def test_user_can_start_checkout_process():
    your_cart.proceed_to_checkout_your_information_page()
    login_page.add_step_to_test_doc(test_doc, 'The "Checkout: Your information" screen is displayed.',
                                    login_page.get_full_screenshot())
    checkout_your_information.fill_your_information_form()
    login_page.add_step_to_test_doc(test_doc, 'The "Checkout: Your information" form is filled in.',
                                    login_page.get_full_screenshot())
    checkout_your_information.proceed_to_checkout_overview()


def test_user_validate_purchase_totals():
    check.is_true(checkout_overview.check_totals())
    login_page.add_step_to_test_doc(test_doc, 'User go to "Checkout: Summary" screen, totals are correct.',
                                    login_page.get_full_screenshot())


def test_user_place_the_order():
    checkout_overview.place_order()
    login_page.add_step_to_test_doc(test_doc, 'User place the order.',
                                    login_page.get_full_screenshot())
    check.is_true(checkout_complete.confirm_order())
    checkout_complete.save_test_doc(test_doc, TestData.TEST_SUMMARY)
