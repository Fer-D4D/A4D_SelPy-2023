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

mi_driver.get("http://advantageonlineshopping.com/")

ADVANTAGE_USER_ICON = "#hrefUserIcon"

mi_driver.find_element(By.CSS_SELECTOR, ADVANTAGE_USER_ICON).click()

ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON = ".create-new-account.ng-scope"

mi_driver.find_element(By.CSS_SELECTOR, ADVANTAGE_CREATE_NEW_ACCOUNT_BUTTON).click()

ADVANTAGE_USERNAME_FORM_FIELD = "//*[@name='usernameRegisterPage']"
ADVANTAGE_EMAIL_FORM_FIELD = "//*[@name='emailRegisterPage']"
ADVANTAGE_PASSWORD_FORM_FIELD = "//*[@name='passwordRegisterPage']"
ADVANTAGE_CONFIRM_PASSWORD_FORM_FIELD = "//*[@name='confirm_passwordRegisterPage']"

mi_driver.find_element(By.XPATH, ADVANTAGE_USERNAME_FORM_FIELD).send_keys("donfer")

mi_driver.find_element(By.XPATH, ADVANTAGE_EMAIL_FORM_FIELD).send_keys("donfer@donfer.tv")

mi_driver.find_element(By.XPATH, ADVANTAGE_PASSWORD_FORM_FIELD).send_keys("aaBB11")

mi_driver.find_element(By.XPATH, ADVANTAGE_CONFIRM_PASSWORD_FORM_FIELD).send_keys("aaBB11")

ADVANTAGE_I_AGREE_CHECKBOX = "//*[@name='i_agree']"

mi_driver.find_element(By.XPATH, ADVANTAGE_I_AGREE_CHECKBOX).click()

ADVANTAGE_REGISTER_BUTTON = "#register_btnundefined"

mi_driver.find_element(By.CSS_SELECTOR, ADVANTAGE_REGISTER_BUTTON).click()
