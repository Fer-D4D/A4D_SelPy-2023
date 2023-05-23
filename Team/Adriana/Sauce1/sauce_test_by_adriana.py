from Team.Adriana.Sauce1.checkout_page import CheckoutPage
from Team.Adriana.Sauce1.your_information_page import YourInformationPage
from core.Common_II import TinyCore
from login_page import LoginPage
from landing_page import LandingPage
from product_page import ProductPage

# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "chrome"
VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test actions
lets_automate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
global_driver = lets_automate.launch_site(TEST_URL)  # Important step


login_page = LoginPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
landing_page = LandingPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
product_page = ProductPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
checkout_page = CheckoutPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
your_information_page = YourInformationPage(global_driver, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)


login_page.do_login()
landing_page.add_item_to_shopping_cart('Sauce Labs Backpack')
landing_page.remove_item_from_shopping_cart('Sauce Labs Backpack')
landing_page.img_clicking('Test.allTheThings() T-Shirt (Red)')
product_page.add_item_to_shopping_cart('Test.allTheThings() T-Shirt (Red)')
product_page.lets_back_to_products()
landing_page.checkout_shopping_cart()
checkout_page.choice_checkout()
your_information_page.do_fill_form()
