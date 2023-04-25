from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "chrome"
TEXT_2_SEARCH = "Peaches, peaches"

# Test Elements
XPATH_SEARCH_INPUT_TEXT = "XPATH://input[@id='search_form_input_homepage']"
CSS_SEARCH_INPUT_TEXT = "CSS:input[name='q']"
LAURA_MENU_ICON = "CSS:.header__button--menu.js-side-menu-open"
SEARCH_INPUT_TEXT = "CSS:#search_form_input_homepage"
SEARCH_BUTTON = "ID:search_button_homepage"
CSS_SEARCH_BUTTON = "CSS:.searchbox_searchButton__F5Bwq.iconButton_button__6x_9C"
XPATH_SEARCH_BUTTON = "XPATH://input[@id='search_button_homepage']"
MENU_BUTTON = "CSS:.header__button--menu.js-side-menu-open"
MENU_SECTION_HEADERS = "XPATH:"
FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"
FIRST_RESULT_SUMMARY_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[3]//child::span[%$%]"

# Test Actions
letsAutomate = Common(BROWSER)
letsAutomate.launch_site(TEST_URL, CSS_SEARCH_BUTTON)

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, TEXT_2_SEARCH)
letsAutomate.do_click(CSS_SEARCH_BUTTON)

print(letsAutomate.get_text_from_element(FIRST_RESULT_TITTLE_SPAN))
print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "1")))
print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "2")))
