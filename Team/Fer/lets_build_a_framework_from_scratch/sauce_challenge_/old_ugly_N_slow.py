import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Function: Validate the functionality to make a purchase on the Sauce site.

Given the user is already registered on the Sauce website.
Given that the user is able to log in to the Sauce site.
Given that the user has added a backpack and a jacket to the shopping cart.
Given that the user checks the contents of his shopping cart.
And the user clicks on the Checkout button
Then the "Checkout: Your information" screen is displayed.
And the user will be able to enter his data
And the user can proceed to the "Checkout: Summary" by clicking on the Continue button
And the user validates that the total of the purchase, taxes included, is correct.
Finally, the user must place the order by clicking the Finish button.
"""

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

mi_driver.get("https://www.saucedemo.com/")

USER_NAME_FORM_FIELD = "user-name"
PASSWORD_FORM_FIELD = "password"
LOGIN_BUTTON = "login-button"

user_name_web_element = mi_driver.find_element(By.ID, USER_NAME_FORM_FIELD)

user_name_web_element.send_keys("standard_user")

time.sleep(1)

mi_driver.find_element(By.ID, PASSWORD_FORM_FIELD).send_keys("secret_sauce")

time.sleep(1)

mi_driver.find_element(By.ID, LOGIN_BUTTON).click()

time.sleep(1)

SAUCE_LABS_BACKPACK_ADD_BUTTON = "//*[@id='add-to-cart-sauce-labs-backpack']"

mi_driver.find_element(By.XPATH, SAUCE_LABS_BACKPACK_ADD_BUTTON).click()

time.sleep(1)

SAUCE_LABS_JACKET_ADD_BUTTON = "//*[@id='add-to-cart-sauce-labs-fleece-jacket']"

mi_driver.find_element(By.XPATH, SAUCE_LABS_JACKET_ADD_BUTTON).click()

time.sleep(1)

SAUCE_LABS_SHOPPING_CART_ICON = ".shopping_cart_link"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_SHOPPING_CART_ICON).click()

time.sleep(1)

SAUCE_LABS_CHECKOUT_BUTTON = "#checkout"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_CHECKOUT_BUTTON).click()

time.sleep(1)

SAUCE_LABS_CHECKOUT_FIRST_NAME = "#first-name"
SAUCE_LABS_CHECKOUT_LAST_NAME = "#last-name"
SAUCE_LABS_CHECKOUT_POSTAL_CODE = "#postal-code"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_CHECKOUT_FIRST_NAME).send_keys("Fer")

time.sleep(1)

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_CHECKOUT_LAST_NAME).send_keys("Perez")

time.sleep(1)

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_CHECKOUT_POSTAL_CODE).send_keys("00000")

time.sleep(1)

SAUCE_LABS_CONTINUE_BUTTON = "#continue"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_CONTINUE_BUTTON).click()

time.sleep(1)

SAUCE_LABS_FINISH_BUTTON = "#finish"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_FINISH_BUTTON).click()

time.sleep(1)

SAUCE_LABS_BACK_2_PRODUCTS_BUTTON = "#back-to-products"

mi_driver.find_element(By.CSS_SELECTOR, SAUCE_LABS_BACK_2_PRODUCTS_BUTTON).click()

time.sleep(1)

