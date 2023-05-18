from selenium import webdriver
from selenium.webdriver.common.by import By
# Config

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "edge"
TEXT_2_SEARCH = "Peaches, peaches"


# Test Elements
CSS_SEARCH_INPUT_TEXT = "#search_form_input_homepage"
ID_SEARCH_BUTTON = "search_button_homepage"
XPATH_FIRST_RESULT_TITTLE_SPAN = "//div[@id='links']/child::div[1]//child::div[2]//span"
XPATH_FIRST_RESULT_SUMMARY_SPAN = "//div[@id='links']/child::div[1]//child::div[3]//child::span[%$%]"
MENU_BUTTON = "CSS:.header__button--menu.js-side-menu-open"
MENU_SECTION_HEADERS = "XPATH:"
FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"
FIRST_RESULT_SUMMARY_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[3]//child::span[%$%]"

# Test Actions

driver = webdriver.Edge()
driver.get("https://duckduckgo.com/")
driver.maximize_window()
search_input_element = driver.find_element(By.CSS_SELECTOR, CSS_SEARCH_INPUT_TEXT)
search_input_element.clear()
search_input_element.send_keys(TEXT_2_SEARCH)
search_button_element = driver.find_element(By.ID, ID_SEARCH_BUTTON)
search_button_element.click()

search_result_tittle = driver.find_element(By.XPATH, XPATH_FIRST_RESULT_TITTLE_SPAN)
print(search_result_tittle.text)
search_result_body_1 = driver.find_element(By.XPATH, XPATH_FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "1"))
print(search_result_body_1)
search_result_body_2 = driver.find_element(By.XPATH, XPATH_FIRST_RESULT_SUMMARY_SPAN.replace("%$%", "2"))
print(search_result_body_2)
