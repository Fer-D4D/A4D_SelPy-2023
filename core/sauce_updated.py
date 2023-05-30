from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common import NoSuchElementException

#mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def launch_site(driver,base_url):
    driver.get(base_url)

def delay_time(waiting_time_value):
    time.sleep(waiting_time_value)
    print(f"Waited for {waiting_time_value} seconds. Continuing with additional actions.")

def find_element_by_css(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator)

def find_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def get_text_from_element(driver, locator):
    return driver.find_element(By.XPATH, locator).text


def fill_text_to_element(driver, locator, text):
        return driver.find_element(By.XPATH, locator).send_keys(text)

def do_click(driver, locator):
        return driver.find_element(By.XPATH, locator).click()

def do_login(driver, username, password):
    fill_text_to_element(driver, "//input[@id='user-name']", username)
    fill_text_to_element(driver, "//input[@id='password']", password)
    do_click(driver, "//input[@id='login-button']")