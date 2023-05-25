from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_complete import CheckoutComplete
from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_overview import CheckoutOverview
from Team.Fer.Sauce.Second_Challenge_Week_05.checkout_your_information import CheckoutYourInformation
from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage
from Team.Fer.Sauce.Second_Challenge_Week_05.login_page import LoginPage
from Team.Fer.Sauce.Second_Challenge_Week_05.product_page import ProductPage
from Team.Fer.Sauce.Second_Challenge_Week_05.your_cart import YourCart


class Setup:
    TEST_URL = "https://www.saucedemo.com/"
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

    COVER_ITEMS_DIC = {"Project": "A4D-Selenium Python",
                       "Summary": "YouTube Simple Searching test",
                       "Environment": "PROD V34",
                       "Tested by": "Fernando Perez",
                       "Date": "%$%",
                       "Otra cosa": "lo que sea"}


login_page = LoginPage(Setup.BROWSER,
                       Setup.VIEWER_MODE,
                       Setup.VERBOSE_MODE,
                       Setup.HIGHLIGHT_MODE)

main_flow = login_page
main_flow.set_ss_fail_mode("OFF")

test_driver = login_page.launch_site(Setup.TEST_URL)

landing_page = LandingPage(test_driver,
                           Setup.VIEWER_MODE,
                           Setup.VERBOSE_MODE,
                           Setup.HIGHLIGHT_MODE)

product_page = ProductPage(test_driver,
                           Setup.VIEWER_MODE,
                           Setup.VERBOSE_MODE,
                           Setup.HIGHLIGHT_MODE)

your_cart = YourCart(test_driver,
                     Setup.VIEWER_MODE,
                     Setup.VERBOSE_MODE,
                     Setup.HIGHLIGHT_MODE)

checkout_your_information = CheckoutYourInformation(test_driver,
                                                    Setup.VIEWER_MODE,
                                                    Setup.VERBOSE_MODE,
                                                    Setup.HIGHLIGHT_MODE)

checkout_overview = CheckoutOverview(test_driver,
                                     Setup.VIEWER_MODE,
                                     Setup.VERBOSE_MODE,
                                     Setup.HIGHLIGHT_MODE)

checkout_complete = CheckoutComplete(test_driver,
                                     Setup.VIEWER_MODE,
                                     Setup.VERBOSE_MODE,
                                     Setup.HIGHLIGHT_MODE)


def workflow_mapper(xlsx_data):
    for test_data in xlsx_data:
        if test_data['Workflow'] == "Full Flow Fast Product Addition":
            full_flow_fast_product_addition(test_data["Test Data"].split(", "), test_data)
        if test_data['Workflow'] == "Full Flow Long Product Addition":
            full_flow_long_product_addition(test_data["Test Data"].split(", "), test_data)


def full_flow_fast_product_addition(item_list, cover_details):
    print(item_list)
    print(cover_details)
    main_flow.start_test_doc()
    main_flow.add_cover_page(cover_details)
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
    main_flow.save_doc_results(f"{cover_details['Summary']}-Test Run_{main_flow.update_test_run():03d}")


def full_flow_long_product_addition(item_list, cover_details):
    print(item_list)
    print(cover_details)
    main_flow.start_test_doc()
    main_flow.add_cover_page(cover_details)
    login_page.fill_login_form()
    main_flow.document_assert_results(True, "User go Sauce site and enter credentials")
    login_page.proceed_landing_page()

    main_flow.document_assert_results(landing_page.check_expected_condition("Swag Labs"),
                                      "User can login Sauce, Home page is displayed",
                                      "Expected Title does not match.")

    if main_flow.get_flow_control_flag_status():
        for item in item_list:
            landing_page.img_clicking(item)
            product_page.add_item_to_shopping_cart(item)
            main_flow.document_assert_results(True, "User go to products details and then add it")
            product_page.lets_back_to_products()

    if main_flow.get_flow_control_flag_status():
        main_flow.document_assert_results(landing_page.compare_lists(landing_page.get_added_item_names_list(),
                                                                     item_list),
                                          "Products added are reflected in home page")
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
    main_flow.save_doc_results(f"{cover_details['Summary']}-Test Run_{main_flow.update_test_run():03d}")
