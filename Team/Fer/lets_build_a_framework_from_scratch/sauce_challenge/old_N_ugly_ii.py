from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Team.Fer.core.utils import oneSec, twoSec

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


class locators:
    USER_NAME_FORM_FIELD = "//*[@id='user-name']"
    PASSWORD_FORM_FIELD = "#password"
    LOGIN_BUTTON = "login-button"

class data:
    USER_NAME = "standard_user"
    PASSWORD = "secret_sauce"


class miBy:
    """Set of supported locator strategies."""

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


@oneSec
def poner_texto(customBy, locator, txt):
    mi_driver.find_element(customBy, locator).send_keys(txt)

@twoSec
def DAR_CLICK(customBy, locator):
    mi_driver.find_element(customBy, locator).click()


poner_texto(miBy.XPATH, locators.USER_NAME_FORM_FIELD, data.USER_NAME)
poner_texto(miBy.CSS_SELECTOR, locators.PASSWORD_FORM_FIELD, data.PASSWORD)
DAR_CLICK(miBy.ID, locators.LOGIN_BUTTON)
