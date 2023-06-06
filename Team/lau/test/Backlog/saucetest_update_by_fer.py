from selenium.webdriver.common.by import By

from Team.lau.test.Backlog.sauce_updated_class import Laura

from Team.lau.test.Backlog.sauce_updated_class import find_element_by_id
from Team.lau.test.Backlog.sauce_updated_class import get_text_from_element
from Team.lau.test.Backlog.sauce_updated_class import fill_text_to_element
from Team.lau.test.Backlog.sauce_updated_class import do_login

my_class = Laura()
mi_driver = my_class.setup_driver()

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
TITLE_SHIRT = "//a[@id='item_3_title_link']//div[@class='inventory_item_name']"
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
VIEW_RESULT_PRINT8 = "//div[@class='summary_info']/child::div[8]"
checkout_name = "Laura"
checkout_lastname = "Curtidor"
checkout_zip = "044510"


#Inicio
#mi_driver.get("https://www.saucedemo.com/")

my_class.launch_site(mi_driver, "https://www.saucedemo.com/", 800, 600)


#FIND ELEMENT CSS: username_input = mi_driver.find_element(By.CSS_SELECTOR, "#user-name")
#FIND ELEMENT XPATH: add_shirt_cart = mi_driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
#FIND ELEMENT ID: opening_image = mi_driver.find_element(By.ID, "item_3_img_link")
#GET TEXT FROM AN ELEMENT:shirt_information = mi_driver.find_element(By.XPATH, "//a[@id='item_3_title_link']//div[@class='inventory_item_name']").text
#DELAY:my_class.delay_time(2)
#BACK TO PREVIUS PAGE: mi_driver.back()

loginPage = do_login(mi_driver, "standard_user", "secret_sauce")

# Find username input field
#username_input = find_element_by_css(mi_driver, SEARCH_USERNAME_TEXT)
#username_input.send_keys("standard_user")

# Find password input field
#password_input = mi_driver.find_element(By.CSS_SELECTOR, SEARCH_PASSWORD_TEXT)
#password_input.send_keys("secret_sauce")

# Find submit button
#submit_button_input = do_click(mi_driver, "//input[@id='login-button']")
#submit_button_input = mi_driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
#submit_button_input.click()
my_class.delay_time(2)
#add the "Sauce Labs backpack"
adding_first_item = mi_driver.find_element(By.CSS_SELECTOR, ADD_FIRST_ITEM)
adding_first_item.click()

#click on the product image called "Test.allTheThings() T-Shirt (Red)"
opening_image = find_element_by_id(mi_driver, "item_3_img_link")
opening_image.click()

#add T-Shirt (Red) to the cart
add_shirt_cart = mi_driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
add_shirt_cart.click()

#backpage
mi_driver.back()
#remove backpack
remove_pack = mi_driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
remove_pack.click()

#Go to the cart
go_to_cart = mi_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
go_to_cart.click()

#print shirt info
shirt_information = mi_driver.find_element(By.XPATH, "//a[@id='item_3_title_link']//div[@class='inventory_item_name']").text
shirt_description = mi_driver.find_element(By.XPATH, "//div[@class='cart_item_label']//div[@class='inventory_item_desc']").text
shirt_price = mi_driver.find_element(By.XPATH, "//div[@class='item_pricebar']//div[@class='inventory_item_price']").text
print("Response text:", shirt_information, shirt_description, shirt_price)

my_class.delay_time(3)
#checkout button

checkout_product = mi_driver.find_element(By.XPATH, "//button[@id='checkout']").click()

#fill checkout

fill_name_checkout = fill_text_to_element(mi_driver, "//input[@id='first-name']", "Laura")

#fill_checkout_name = mi_driver.find_element(By.XPATH, "//input[@id='first-name']")
#fill_checkout_name.send_keys("Laura")
fill_checkout_lastname = mi_driver.find_element(By.XPATH, "//input[@id='last-name']")
fill_checkout_lastname.send_keys("Curtidor")
fill_checkout_zip = mi_driver.find_element(By.XPATH, "//input[@id='postal-code']")
fill_checkout_zip.send_keys("044510")
checkout_button = mi_driver.find_element(By.XPATH, "//input[@id='continue']").click()

#total_price = mi_driver.find_element(By.XPATH, "//div[@class='summary_info']/child::div[8]").text
#print("Response text:", total_price)

get_info_total_price = get_text_from_element(mi_driver, VIEW_RESULT_PRINT8)
print("Response text", get_info_total_price)
