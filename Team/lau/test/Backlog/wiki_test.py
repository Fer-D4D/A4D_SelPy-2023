from core.Common_II import TinyCore

# Test Data
TEST_URL = "https://duckduckgo.com/?t=h"
BROWSER = "chrome"
VIEWER_MODE = "OFF"
VERBOSE_MODE = "OFF"
HIGHLIGHT_MODE = "OFF"

# Test Elements
SEARCH_INPUT_TEXT = "XPATH://input[@id='search_form_input_homepage']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"
FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, SEARCH_INPUT_TEXT)

my_search_list = ["Jacket", "Panic", "Alchemist"]

for idx in my_search_list:
    letsAutomate.fill_input_text(SEARCH_INPUT_TEXT, "Full Metal " + idx)
    letsAutomate.do_click(SEARCH_BUTTON)
    print(letsAutomate.get_element_inner_text(FIRST_RESULT_TITTLE_SPAN))
    letsAutomate.page_back()
