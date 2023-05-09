from core.Common_II import TinyCore
from test.Week_04.duck_duck_go_page import SearchPage, ResultsPage


# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "edge"
# some changes here, an easy way to configure your tests
VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "ON"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test Elements

duckx2Elements = SearchPage()
duckx2ResultElem = ResultsPage()

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, duckx2Elements.SEARCH_INPUT_TEXT)

# Let's apply our basic python from last week :)
# A small list for our search terms
my_search_list = ["Jacket", "Panic", "Alchemist"]

# Now using a For loop, let's execute search process
for idx in my_search_list:
    search_text = "Full Metal " + idx

    letsAutomate.fill_input_text(duckx2Elements.get_search_text_field(), search_text)
    # What do we have here?! yup this is new, screenshots!!!
    letsAutomate.get_emphasis_screenshot(search_text + "-A", duckx2Elements.get_search_text_field())

    letsAutomate.do_click(duckx2Elements.get_search_button())
    letsAutomate.get_element_inner_text(duckx2ResultElem.get_result_text())
    letsAutomate.get_emphasis_screenshot(search_text + "-B", duckx2ResultElem.get_result_text())
    letsAutomate.page_back()
