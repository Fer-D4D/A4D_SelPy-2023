#Scenario:As a standard user I can access the Sauce website
# and once on the home page I will be able to add the "Sauce Labs backpack",
# in addition I can click on the product image called "Test.allTheThings()
# T-Shirt (Red)" and add the item from the product description page,
# and then return to the home page by clicking on the "Back to products"
# button and then remove the backpack.
#Expected Results:
#The product counter in the shopping cart should reflect the actions taken and be equal to 1.
from core.common2 import TinyCore
from core.sauce_test import TestData, Locators, ResultsPage, AddProducts, LoginPage


# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "Chrome"
# some changes here, an easy way to configure your tests
VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

localizadores = Locators()
testdata = TestData()
pageresults = ResultsPage()
addproductcar = AddProducts()
loginpage = LoginPage()

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, localizadores.SEARCH_USERNAME_TEXT)

#letsAutomate.fill_input_text(localizadores.SEARCH_USERNAME_TEXT, testdata.search_text_name)
# What do we have here?! yup this is new, screenshots!!!
#letsAutomate.get_emphasis_screenshot(search_text_name + "-A", loginpagenew.get_username_text())
#letsAutomate.fill_input_text(localizadores.SEARCH_PASSWORD_TEXT, testdata.search_text_password)
#letsAutomate.get_emphasis_screenshot(search_text_password + "-B", loginpagenew.get_password_text())
#letsAutomate.do_click(localizadores.SEARCH_BUTTON)

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
letsAutomate.do_click(addproductcar.CHECKOUT_BUTTON)
letsAutomate.fill_input_text(addproductcar.CHECKOUT_NAME, testdata.checkout_name)
letsAutomate.fill_input_text(addproductcar.CHECKOUT_LASTNAME, testdata.checkout_lastname)
letsAutomate.fill_input_text(addproductcar.CHECKOUT_ZIP, testdata.checkout_zip)
addproductcar.print_content()
letsAutomate.do_click(addproductcar.CHECKOUT_CONTINUE)
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT1))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT2))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT3))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT4))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT5))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT6))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT7))
#print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRINT8))
letsAutomate.page_back()