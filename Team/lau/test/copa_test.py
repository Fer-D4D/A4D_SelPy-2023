from core.Common import Common, waste_some_time

# Test Data
TEST_URL = "https://copacom-qa.copa.s4n.co/en-gs/form_pruebas/"
BROWSER = "chrome"
TEXT_INPUT_NAME = "AJ3AF0"
TEXT_INPUT_LAST_NAME = "Marin"

# Test Elements
XPATH_PNR_INPUT_TEXT = "XPATH://input[@id='mui-1']"
PNR_INPUT_TEXT = "CSS:#mui-1"
SEARCH_PNR_INPUT = "ID:mui-1"
XPATH_LAST_NAME_INPUT_TEXT = "XPATH://input[@id='mui-2']"
LAST_NAME_INPUT_TEXT = "CSS:#mui-2"
SEARCH_LAST_NAME_INPUT = "ID:mui-2"
XPATH_SUBMIT_BUTTON = "XPATH://input[@buttontype='Regular']"
# MENU_BUTTON = "CSS:.header__button--menu.js-side-menu-open"
# MENU_SECTION_HEADERS = "XPATH:"
# FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"
# FIRST_RESULT_SUMMARY_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[3]//child::span[%$%]"

# Test Actions
letsAutomate = Common(BROWSER)
letsAutomate.launch_site(TEST_URL, SEARCH_PNR_INPUT)
waste_some_time(2)
letsAutomate.fill_input_text(XPATH_PNR_INPUT_TEXT, TEXT_INPUT_NAME)
waste_some_time(2)
letsAutomate.fill_input_text(XPATH_LAST_NAME_INPUT_TEXT, TEXT_INPUT_LAST_NAME)
waste_some_time(2)
letsAutomate.do_click(XPATH_SUBMIT_BUTTON)
waste_some_time(5)

# print(letsAutomate.get_text_from_element(FIRST_RESULT_TITTLE_SPAN))
# print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "1")))
# print(letsAutomate.get_text_from_element(FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "2")))
