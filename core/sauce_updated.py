from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

SEARCH_USERNAME_TEXT = "#user-name"
SEARCH_PASSWORD_TEXT = "#password"
SEARCH_BUTTON = ".submit-button.btn_action"
search_text_name = "standard_user"
search_text_password = "secret_sauce"

def delay_time(waiting_time_value):
    time.sleep(waiting_time_value)
    print(f"Waited for {waiting_time_value} seconds. Continuing with additional actions.")

def find_element_by_css(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator)

def find_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)
