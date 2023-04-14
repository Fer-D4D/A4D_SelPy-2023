from core.Common import Common, fill_input_by_xpath, do_click_by_xpath, waste_some_time, get_text_from_element_by_xpath

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "Edge"
TEXT_2_SEARCH = "Peaches, peaches"
FIRST_RESULT_SPAN = "//div[@id='links']/child::div[1]//child::div[2]//span"

# Test Elements
SEARCH_INPUT_TEXT = "//input[@id='search_form_input_homepage']"
SEARCH_BUTTON = "//input[@id='search_button_homepage']"

# Test Actions
driver = Common(BROWSER).go_url(TEST_URL)
fill_input_by_xpath(driver, SEARCH_INPUT_TEXT, TEXT_2_SEARCH)
do_click_by_xpath(driver, SEARCH_BUTTON)
print(get_text_from_element_by_xpath(driver, FIRST_RESULT_SPAN))
waste_some_time()
