from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "Edge"
TEXT_2_SEARCH = "Peaches, peaches"


# Test Elements
XPATH_SEARCH_INPUT_TEXT = "XPATH://input[@id='search_form_input_homepage']"
SEARCH_INPUT_TEXT = "CSS:#search_form_input_homepage"
SEARCH_BUTTON = "ID:search_button_homepage"
XPATH_SEARCH_BUTTON = "XPATH://input[@id='search_button_homepage']"
FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"
FIRST_RESULT_SUMMARY_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[3]//child::span[%$%]"

# Test Actions
letsAutomate = Common(BROWSER)

letsAutomate.launch_site(TEST_URL, SEARCH_BUTTON)
letsAutomate.fill_input_text(XPATH_SEARCH_INPUT_TEXT, TEXT_2_SEARCH)
letsAutomate.do_click(SEARCH_BUTTON)
print(letsAutomate.get_text_from_element(FIRST_RESULT_TITTLE_SPAN))
print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "1")))
print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "2")))
