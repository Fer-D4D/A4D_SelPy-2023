from core.Common_II import TinyCore

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "edge"
VIEWER_MODE = "OFF"
VERBOSE_MODE = "ON"
HIGHLIGHT_MODE = "OFF"

# Test Elements

# Selectors normal way
SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"

FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"

# Dictionary approach

search_page_dic = {"search_input_text": "CSS:input[placeholder='Search the web without being tracked']",
                   "search_button": "CSS:.search__button.js-search-button"}
search_result_page_dic = {"first_result_title_span": "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"}
duck_duck_go_site_dic = {"Search Page": search_page_dic, "Result Page": search_result_page_dic}


def get_selector_from_dic(site_dic, page_name, selector_name):
    return site_dic[page_name][selector_name]


# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, SEARCH_INPUT_TEXT)

my_search_list = ["Jacket", "Panic", "Alchemist"]

letsAutomate.fill_input_text(get_selector_from_dic(duck_duck_go_site_dic, "Search Page", "search_input_text"), "Carlitos way")
letsAutomate.get_emphasis_screenshot("Carlitos way-A", get_selector_from_dic(duck_duck_go_site_dic, "Search Page", "search_input_text"))
letsAutomate.do_click(duck_duck_go_site_dic["Search Page"]["search_button"])
letsAutomate.get_element_inner_text(get_selector_from_dic(duck_duck_go_site_dic, "Result Page", "first_result_title_span"))
letsAutomate.get_emphasis_screenshot("Carlitos way-B", get_selector_from_dic(duck_duck_go_site_dic, "Result Page", "first_result_title_span"))
letsAutomate.page_back()

for idx in my_search_list:
    search_text = "Full Metal " + idx
    letsAutomate.fill_input_text(SEARCH_INPUT_TEXT, search_text)
    letsAutomate.get_emphasis_screenshot(search_text + "-A", SEARCH_INPUT_TEXT)
    letsAutomate.do_click(SEARCH_BUTTON)
    letsAutomate.get_element_inner_text(FIRST_RESULT_TITTLE_SPAN)
    letsAutomate.get_emphasis_screenshot(search_text + "-B", FIRST_RESULT_TITTLE_SPAN)
    letsAutomate.page_back()
