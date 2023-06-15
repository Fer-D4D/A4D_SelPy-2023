from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from test.week_06.my_framework_from_scratch import OtherTinyCore

"""
Scenario: 

As a standard user I can access the Sauce website and once on the home page I will be able to add the 
"Sauce Labs backpack", in addition I can click on the product image called "Test.allTheThings() T-Shirt (Red)" and 
add the item from the product description page, and then return to the home page by clicking on the "Back to 
products" button and then remove the backpack. 

Expected Results:
The product counter in the shopping cart should reflect the actions taken and be equal to 1.
"""

# This step may vary, depending on whether you use the WebDriver-Manager package and also
# the browser you choose to use.And the purpose is to generate the controller that we will
# use to interact with the chosen browser.

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Now that we have a way to interact with the browser we can launch it at the desired URL,
# for this we use the native selenium method called "get()".

mi_driver.get("https://www.saucedemo.com/")

# Ok, chrome is launched and the desired site is visible, now we need to enter the required
# credentials to login, so we need a way to interact with the required web elements,
# which are Username, Password and Login button.

USER_NAME_FORM_FIELD = "user-name"
PASSWORD_FORM_FIELD = "password"
LOGIN_BUTTON = "login-button"

# Fortunately, all three elements have the attribute id! With the selectors in hand,
# we can interact with them using selenium's native methods

user_name_web_element = mi_driver.find_element(By.ID, USER_NAME_FORM_FIELD)

# Let's explain the latter, first we use my_driver to access the browser,
# then we make use of the "find_element" method of the WebDriver class
# to have control of the desired element which we store in the variable "user_name_web_element".

user_name_web_element.send_keys("standard_user")

# the type of the variable just created, is WebElement, this class has several useful methods,
# for now we only care about send_keys() and click(). Both although self-descriptive are a little different,
# in the case of send_keys it is necessary to pass a string, but click() does not require arguments.

mi_driver.find_element(By.ID, PASSWORD_FORM_FIELD).send_keys("secret_sauce")

# For the case of the password element, we skip the intermediate step of creating a variable and access
# the send_keys method in an abbreviated way. How does this work? Recall that the find_element() method
# returns an object of type WebElement, so we can access it without storing it in a variable.

mi_driver.find_element(By.ID, LOGIN_BUTTON).click()

# Here we use the clik() method using the shorthand technique that we saw in the previous step. With this done the
# home page should be displayed, and therefore we will have access to the products. You know what's next, don't you?
# that's right, we need a few selectors

SAUCE_LABS_BACKPACK_ADD_BUTTON = "//*[@id='add-to-cart-sauce-labs-backpack']"
T_SHRT_RED_IMG = "//img[@alt='Test.allTheThings() T-Shirt (Red)']"

# Bello, we already have the selectors, and we know how to use the click method, let's apply it.

mi_driver.find_element(By.XPATH, SAUCE_LABS_BACKPACK_ADD_BUTTON).click()
mi_driver.find_element(By.XPATH, T_SHRT_RED_IMG).click()

# I don't think this needs any explanation, except for the fact that we have changed a little
# the way we use the find_element method, indicating that it will not be by ID but by XPATH.
# Now we are on the product detail page. Yep, we need more selectors to continue

T_SHRT_RED_ADD_BUTTON = "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
BACK_TO_PRODUCTS_LINK = "back-to-products"

# Fine, now we have the selectors, and we know how to use the click method, go ahead and apply it.

mi_driver.find_element(By.XPATH, T_SHRT_RED_ADD_BUTTON).click()
mi_driver.find_element(By.ID, BACK_TO_PRODUCTS_LINK).click()

# no explanations are required, right? Well with the above accomplished, yes, more selectors are needed lol

SAUCE_LABS_BACKPACK_REMOVE_BUTTON = "//*[@id='remove-sauce-labs-backpack']"
SHOPPING_CART_COUNTER = "//div[@id='shopping_cart_container']//span"

# you know what to do, don't you? clickityclick

mi_driver.find_element(By.XPATH, SAUCE_LABS_BACKPACK_REMOVE_BUTTON).click()

# almost there, it only remains to validate the number of products in the shopping cart, for that we will make use of
# another method of the WebElement class, I speak of the property "text" this will return the text associated with an
# item

if int(mi_driver.find_element(By.XPATH, SHOPPING_CART_COUNTER).text) == 1:
    print("Test completed")

# According to the test scenario it is expected that the shopping cart contains only one product, that's why we do a
# validation by comparing the text associated with the shopping cart item and if it is equal to 1, we can sing victory
