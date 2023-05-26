from core.common2 import TinyCore
from core.sauce_test import LoginInto, ResultsPage, AddProducts, Locators, TestData


# Test Data
TEST_URL = "https://www.saucedemo.com/"
BROWSER = "Chrome"
# some changes here, an easy way to configure your tests
VIEWER_MODE = "ON"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test Elements

loginpagenew = LoginInto()
localizadores = Locators()
testdata = TestData()
pageresults = ResultsPage()
addproductcar = AddProducts()

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, localizadores.SEARCH_USERNAME_TEXT)

letsAutomate.fill_input_text(localizadores.SEARCH_USERNAME_TEXT, testdata.search_text_name)
# What do we have here?! yup this is new, screenshots!!!
#letsAutomate.get_emphasis_screenshot(search_text_name + "-A", loginpagenew.get_username_text())
letsAutomate.fill_input_text(localizadores.SEARCH_PASSWORD_TEXT, testdata.search_text_password)
#letsAutomate.get_emphasis_screenshot(search_text_password + "-B", loginpagenew.get_password_text())
letsAutomate.do_click(localizadores.SEARCH_BUTTON)
print(pageresults.get_result_text())
letsAutomate.do_click(addproductcar.ADD_FIRST_ITEM)
letsAutomate.do_click(addproductcar.ADD_SECOND_ITEM)
letsAutomate.do_click(addproductcar.ADD_THIRD_ITEM)
#print("Your products were added")
print(pageresults.get_added_text())
letsAutomate.do_click(addproductcar.VIEW_CAR_OPTION)
print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_ITEM1))
print(letsAutomate.get_text_from_element(addproductcar.VIEW_RESULT_PRICE))
letsAutomate.page_back()