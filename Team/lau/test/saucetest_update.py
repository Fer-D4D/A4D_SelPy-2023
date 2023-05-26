from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from core.sauce_updated import delay_time

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

SEARCH_USERNAME_TEXT = "#user-name"
SEARCH_PASSWORD_TEXT = "#password"
SEARCH_BUTTON = ".submit-button.btn_action"
search_text_name = "standard_user"
search_text_password = "secret_sauce"

ADD_FIRST_ITEM = "#add-to-cart-sauce-labs-backpack"
ADD_SECOND_ITEM = "CSS:#add-to-cart-sauce-labs-fleece-jacket"
ADD_THIRD_ITEM = "CSS:#add-to-cart-sauce-labs-onesie"
ADD_SHIRT_ITEM = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
VIEW_CAR_OPTION = "XPATH://a[@class='shopping_cart_link']"
VIEW_RESULT_ITEM1 = "XPATH://div[@class='cart_item_label']//a[@id='item_4_title_link']/child::div[1]"
VIEW_RESULT_ITEM2 = "XPATH://div[@class='cart_item_label']//a[@id='item_3_title_link']/child::div[1]"
VIEW_RESULT_PRICE = "XPATH://*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
IMAGE_FIRST_ITEM = "XPATH://div[@class='inventory_item_img']//a[@id='item_4_img_link']/child::img"
IMAGE_SHIRT_ITEM = "XPATH://div[@class='inventory_item_img']//a[@id='item_3_img_link']/child::img"
IMAGE_SHIRT_ITEM_ID = "item_3_img_link"
BACK_BUTTON = "XPATH://button[@id='back-to-products']"
REMOVE_FIRST_ITEM = "CSS:#remove-sauce-labs-backpack"
CHECKOUT_BUTTON = "XPATH://button[@id='checkout']"
CHECKOUT_NAME = "XPATH://input[@id='first-name']"
CHECKOUT_LASTNAME = "XPATH://input[@id='last-name']"
CHECKOUT_ZIP = "XPATH://input[@id='postal-code']"
CHECKOUT_CONTINUE = "XPATH://input[@id='continue']"
VIEW_RESULT_PRINT1 = "XPATH://div[@class='summary_info']/child::div[1]"
VIEW_RESULT_PRINT2 = "XPATH://div[@class='summary_info']/child::div[2]"
VIEW_RESULT_PRINT3 = "XPATH://div[@class='summary_info']/child::div[3]"
VIEW_RESULT_PRINT4 = "XPATH://div[@class='summary_info']/child::div[4]"
VIEW_RESULT_PRINT5 = "XPATH://div[@class='summary_info']/child::div[5]"
VIEW_RESULT_PRINT6 = "XPATH://div[@class='summary_info']/child::div[6]"
VIEW_RESULT_PRINT7 = "XPATH://div[@class='summary_info']/child::div[7]"
VIEW_RESULT_PRINT8 = "XPATH://div[@class='summary_info']/child::div[8]"
checkout_name = "Laura"
checkout_lastname = "Curtidor"
checkout_zip = "044510"


#Inicio
mi_driver.get("https://www.saucedemo.com/")

#username_input = mi_driver.find_element(By.CSS_SELECTOR, "#user-name")
#add_shirt_cart = mi_driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
#opening_image = mi_driver.find_element(By.ID, "item_3_img_link")

# Find username input field
username_input = mi_driver.find_element(By.CSS_SELECTOR, SEARCH_USERNAME_TEXT)
username_input.send_keys("standard_user")
delay_time(2)
# Find password input field
password_input = mi_driver.find_element(By.CSS_SELECTOR, SEARCH_PASSWORD_TEXT)
password_input.send_keys("secret_sauce")
delay_time(2)
# Find submit button
submit_button_input = mi_driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
submit_button_input.click()
delay_time(2)
#add the "Sauce Labs backpack"
adding_first_item = mi_driver.find_element(By.CSS_SELECTOR, ADD_FIRST_ITEM)
adding_first_item.click()
delay_time(2)
#click on the product image called "Test.allTheThings() T-Shirt (Red)"
opening_image = mi_driver.find_element(By.ID, "item_3_img_link")
opening_image.click()
delay_time(2)
#add T-Shirt (Red) to the cart
add_shirt_cart = mi_driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
add_shirt_cart.click()
delay_time(2)