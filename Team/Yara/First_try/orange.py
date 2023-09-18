import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

PAGE = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

DRIVER.implicitly_wait(5)
#page
DRIVER.get(PAGE)

#In this class can fin the locators_strategies
class locators:

    locator_user = "username"
    locator_pass = "password"
    locator_login = "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"

#In this class can find the data to test
class data:
    ADMIN_USER = "Admin"
    ADMIN_PASS = "admin123"


def get_user(locator_user, user):
    DRIVER.find_element(By.NAME, locator_user).send_keys(user)

def get_pass(locator_pass, password):
    DRIVER.find_element(By.NAME, locator_pass).send_keys(password)

def login_success(locator_button):
    try:
        DRIVER.find_element(By.CSS_SELECTOR, locator_button).click()
    except ElementClickInterceptedException:
        print("Re-clicking")


get_user(locators.locator_user, data.ADMIN_USER)

get_pass(locators.locator_pass, data.ADMIN_PASS)
login_success(locators.locator_login)



