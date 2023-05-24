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

    COVER_ITEMS_DIC = {"Project": "A4D-Selenium Python",
                       "Summary": "YouTube Simple Searching test",
                       "Environment": "PROD V34",
                       "Tested by": "Fernando Perez",
                       "Date": "%$%",
                       "Otra cosa": "lo que sea"}

    TESTING_ITEM_NAMES_MULTI = [TESTING_ITEM_NAMES,
                                ["Sauce Labs Onesie", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"],
                                ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie", "Sauce Labs Bike Light",
                                 "Sauce Labs Bolt T-Shirt"]]
    TEST_SUMMARY = "Sauce Purchasing Functionality"
    ENV_DETAILS = "PRE_PROD V34"
    TESTED_BY = "Fernando Perez"


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

main_flow = login_page
main_flow.set_ss_fail_mode("OFF")

test_driver = login_page.launch_site(TestData.TEST_URL)

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
    for item_list in TestData.TESTING_ITEM_NAMES_MULTI:
        main_flow.start_test_doc()
        main_flow.add_cover_page(TestData.COVER_ITEMS_DIC)
        login_page.fill_login_form()
        main_flow.document_assert_results(True, "User go Sauce site and enter credentials")
        login_page.proceed_landing_page()

        main_flow.document_assert_results(landing_page.check_expected_condition("Swag Labs"),
                                          "User can login Sauce, Home page is displayed",
                                          "Expected Title does not match.")

        if main_flow.get_flow_control_flag_status():
            landing_page.add_items_to_shopping_cart_from_list(item_list)
            main_flow.document_assert_results(landing_page.compare_lists(landing_page.get_added_item_names_list(),
                                                                         item_list),
                                              "User added expected items to the shopping cart")

        if main_flow.get_flow_control_flag_status():
            landing_page.proceed_to_your_cart_page()
            main_flow.document_assert_results(your_cart.compare_lists(your_cart.get_added_item_names_list(),
                                                                      item_list),
                                              "User checks the contents of his shopping cart")

        if main_flow.get_flow_control_flag_status():
            your_cart.proceed_to_checkout_your_information_page()
            checkout_your_information.fill_your_information_form()
            main_flow.document_assert_results(True, 'The "Checkout: Your information" screen is displayed, and user '
                                                    'adds '
                                                    'required information')

            checkout_your_information.proceed_to_checkout_overview()
            main_flow.document_assert_results(checkout_overview.check_totals(), 'User go to "Checkout: Summary" '
                                                                                'screen, '
                                                                                'to validate that totals are correct')
        if main_flow.get_flow_control_flag_status():
            checkout_overview.place_order()
            main_flow.document_assert_results(checkout_complete.confirm_order(), 'The order is placed', True)

        checkout_complete.do_logout()
        main_flow.save_doc_results(f"{TestData.TEST_SUMMARY}-Test Run_{main_flow.update_test_run():03d}")
