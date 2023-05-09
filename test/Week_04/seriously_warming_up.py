from core.Common_II import TinyCore

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "edge"
# some changes here, an easy way to configure your tests
VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
VERBOSE_MODE = "ON"  # By turning this ON you will get some useful information about the test run
HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

# Test Elements

SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"
FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, SEARCH_INPUT_TEXT)

# Let's apply our basic python from last week :)
# A small list for our search terms
my_search_list = ["Jacket", "Panic", "Alchemist"]

# Now using a For loop, let's execute search process
for idx in my_search_list:
    search_text = "Full Metal " + idx

    letsAutomate.fill_input_text(SEARCH_INPUT_TEXT, search_text)
    # What do we have here?! yup this is new, screenshots!!!
    letsAutomate.get_emphasis_screenshot(search_text + "-A", SEARCH_INPUT_TEXT)

    letsAutomate.do_click(SEARCH_BUTTON)
    letsAutomate.get_element_inner_text(FIRST_RESULT_TITTLE_SPAN)
    letsAutomate.get_emphasis_screenshot(search_text + "-B", FIRST_RESULT_TITTLE_SPAN)
    letsAutomate.page_back()
