#Scenario:As a standard user I can access the Sauce website
# and once on the home page I will be able to add the "Sauce Labs backpack",
# in addition I can click on the product image called "Test.allTheThings()
# T-Shirt (Red)" and add the item from the product description page,
# and then return to the home page by clicking on the "Back to products"
# button and then remove the backpack.
#Expected Results:
#The product counter in the shopping cart should reflect the actions taken and be equal to 1.
from core.common2 import TinyCore
from core.sauce_test import TestData, LoginPage, ResultsPage, AddProducts


# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "Chrome"
# some changes here, an easy way to configure your tests
VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test Elements
pageresults = ResultsPage()
addproductcar = AddProducts()
loginpage = LoginPage()
# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL)

loginpage.do_login()

# What do we have here?! yup this is new, screenshots!!!
#letsAutomate.get_emphasis_screenshot(search_text_name + "-A", loginpagenew.get_username_text())
#letsAutomate.get_emphasis_screenshot(search_text_password + "-B", loginpagenew.get_password_text())
print(pageresults.get_result_text())
letsAutomate.do_click(addproductcar.ADD_FIRST_ITEM)
print(pageresults.get_added_text())
letsAutomate.do_click(addproductcar.IMAGE_SHIRT_ITEM)
letsAutomate.do_click(addproductcar.ADD_SHIRT_ITEM)
print(pageresults.get_added_text())
letsAutomate.do_click(addproductcar.BACK_BUTTON)
letsAutomate.do_click(addproductcar.REMOVE_FIRST_ITEM)
letsAutomate.do_click(addproductcar.VIEW_CAR_OPTION)
print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_ITEM2))
print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRICE))
letsAutomate.page_back()