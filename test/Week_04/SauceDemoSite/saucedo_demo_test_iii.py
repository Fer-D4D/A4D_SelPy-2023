from core.Common_II import TinyCore

"""
Scenario:
As a standard user I can access the Sauce website and once I am on the home page 
I will be able to both add and remove products to the shopping cart.
"""

# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "chrome"
VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "ON"  # Turning this ON will highlight the element being used

# Test Elements
# Login Page
USER_NAME_FORM_TEXT = "ID:user-name"
PASSWORD_FORM_TEXT = "ID:password"
LOGIN_BUTTON = "ID:login-button"

# Landing/Home Page
TITLE_TEXT = "XPATH://div[text()='Swag Labs']"
SAUCE_LABS_BACKPACK_ADD_TO_CART_BUTTON = "ID:add-to-cart-sauce-labs-backpack"
SAUCE_LABS_BACKPACK_REMOVE_BUTTON = "ID:remove-sauce-labs-backpack"
SHOPPING_CART_QUANTITY = "XPATH://div[@id='shopping_cart_container']//span"
SAUCE_LABS_ONESIE_ADD_TO_CART_BUTTON = "ID:add-to-cart-sauce-labs-onesie"
SAUCE_LABS_ONESIE_REMOVE_BUTTON = "ID:remove-sauce-labs-onesie"

# Test actions
lets_automate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
lets_automate.launch_site(TEST_URL, LOGIN_BUTTON)

lets_automate.fill_input_text(USER_NAME_FORM_TEXT, "standard_user")
lets_automate.fill_input_text(PASSWORD_FORM_TEXT, "secret_sauce")
lets_automate.do_click(LOGIN_BUTTON)

if lets_automate.get_element_inner_text(TITLE_TEXT) == "Swag Labs":
    lets_automate.do_click(SAUCE_LABS_BACKPACK_ADD_TO_CART_BUTTON)
    lets_automate.do_click(SAUCE_LABS_ONESIE_ADD_TO_CART_BUTTON)
    items_in_shopping_cart = lets_automate.get_element_inner_text(SHOPPING_CART_QUANTITY)
    print("Products added to the shopping cart: " + items_in_shopping_cart)
    lets_automate.do_click(SAUCE_LABS_BACKPACK_REMOVE_BUTTON)
    if lets_automate.get_element_inner_text(SHOPPING_CART_QUANTITY) < items_in_shopping_cart:
        print("Product was removed from the shopping cart: Test Passed")
