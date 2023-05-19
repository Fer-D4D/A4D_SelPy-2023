from Team.Fer.core.Common_II import TinyCore
from Team.Fer.Sauce.landing_page import LandingPage
from Team.Fer.Sauce.login_page import LoginPage
from Team.Fer.Sauce.product_page import ProductPage

"""
Scenario: 

As a standard user I can access the Sauce website and once on the home page I will be able to add the 
"Sauce Labs backpack", in addition I can click on the product image called "Test.allTheThings() T-Shirt (Red)" and 
add the item from the product description page, and then return to the home page by clicking on the "Back to 
products" button and then remove the backpack. 

Expected Results:
The product counter in the shopping cart should reflect the actions taken and be equal to 1.
"""

# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "chrome"
VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test actions
lets_automate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

test_doc = lets_automate.create_test_doc()

global_driver = lets_automate.launch_site(TEST_URL)  # Important step

login_page = LoginPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

login_page.add_step_to_test_doc(test_doc, "Step: Go Sauce site and enter credentials: ",
                                login_page.get_full_screenshot("landing"))

login_page.do_login()

landing_page = LandingPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)

if landing_page.check_for_login_granted():
    landing_page.add_step_to_test_doc(test_doc, "Step: As a standard user I can access the Sauce website",
                                      landing_page.get_full_screenshot("landing"))
    landing_page.add_item_to_shopping_cart("Sauce Labs Backpack")

    landing_page.add_step_to_test_doc(test_doc, "Step: The 'Sauce Labs backpack' item is added: ",
                                      landing_page.get_full_screenshot("Backpack"))
    landing_page.img_clicking("Test.allTheThings() T-Shirt (Red)")

    product_page = ProductPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
    product_page.add_item_to_shopping_cart("Test.allTheThings() T-Shirt (Red)")

    product_page.add_step_to_test_doc(test_doc, "Step: The product called 'Test.allTheThings() T-Shirt (Red)' added "
                                                "to the cart",
                                      product_page.get_full_screenshot("T_shirt_red"))

    product_page.lets_back_to_products()
    landing_page.add_step_to_test_doc(test_doc, "Step: The 'Sauce Labs backpack' item is removed: ",
                                      landing_page.get_full_screenshot("Backpack"))
    landing_page.remove_item_from_shopping_cart("Sauce Labs Backpack")
    if landing_page.get_shopping_cart_item_number() == 1:
        print(f"Shopping cart product number = {landing_page.get_shopping_cart_item_number()} <Test Passed>")
        landing_page.add_step_to_test_doc(test_doc, "The product counter in the shopping cart should reflect the "
                                                    "actions taken and be equal to 1. ",
                                          landing_page.get_full_screenshot("Backpack"))
    product_page.save_test_doc(test_doc, "Mi Test Doc")
