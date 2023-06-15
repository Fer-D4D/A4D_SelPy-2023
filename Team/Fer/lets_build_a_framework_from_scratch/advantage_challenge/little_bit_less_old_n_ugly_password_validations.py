import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Go Advantage site, then try to create new account and then check password rules
"""

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

mi_driver.get("http://advantageonlineshopping.com/")

ADVANTAGE_USER_ICON = "#hrefUserIcon"

mi_driver.find_element(By.CSS_SELECTOR, ADVANTAGE_USER_ICON).click()

ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON = ".create-new-account.ng-scope"

time.sleep(3)

mi_driver.find_element(By.CSS_SELECTOR, ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON).click()

time.sleep(2)
ADVANTAGE_CREATE_ACCOUNT_TITTLE = "//H3[text()[contains(.,'CREATE ACCOUNT')]]"
ADVANTAGE_PASSWORD_FORM = "//input[@name='passwordRegisterPage']"
ADVANTAGE_PASSWORD_ERROR_LABEL = "//input[@name='passwordRegisterPage']/following-sibling::label"


def password_fill_n_check(password):
    mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).clear()
    mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).send_keys(password)
    mi_driver.find_element(By.XPATH, ADVANTAGE_CREATE_ACCOUNT_TITTLE).click()
    return mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text


def rule_validator(expected_value, actual_value):
    if expected_value == actual_value:
        print(
            f"Getting expected message -> {mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text} -- Pass")
    else:
        print("Test failed")


print("Validating minimum length of password field:")
rule_validator("Use 4 character or longer", password_fill_n_check("a"))
print("Validating maximum length of password field:")
rule_validator("Use maximum 12 character", password_fill_n_check("abcdefghijklm"))
print("Validating upper letter password rule field:")
rule_validator("One upper letter required", password_fill_n_check("abcd"))
print("Validating number password rule field:")
rule_validator("One number required", password_fill_n_check("Abcd"))

time.sleep(3)
