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

mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).send_keys("abc")

mi_driver.find_element(By.XPATH, ADVANTAGE_CREATE_ACCOUNT_TITTLE).click()

print("Validating minimum length of password field:")

if mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text == "Use 4 character or longer":
    print(f"Getting expected message -> {mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text} -- Pass")
else:
    print("Test failed")
mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).clear()
mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).send_keys("abcdefghijklm")

mi_driver.find_element(By.XPATH, ADVANTAGE_CREATE_ACCOUNT_TITTLE).click()

print("Validating maximum length of password field:")

if mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text == "Use maximum 12 character":
    print(f"Getting expected message -> {mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text} -- Pass")
else:
    print("Test failed")
mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).clear()
mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).send_keys("abcd")

mi_driver.find_element(By.XPATH, ADVANTAGE_CREATE_ACCOUNT_TITTLE).click()

print("Validating upper letter password rule field:")

if mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text == "One upper letter required":
    print(f"Getting expected message -> {mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text} -- Pass")
else:
    print("Test failed")

mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).clear()
mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM).send_keys("Abcd")

mi_driver.find_element(By.XPATH, ADVANTAGE_CREATE_ACCOUNT_TITTLE).click()

print("Validating number password rule field:")

if mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text == "One number required":
    print(f"Getting expected message -> {mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_ERROR_LABEL).text} -- Pass")
else:
    print("Test failed")

time.sleep(3)



