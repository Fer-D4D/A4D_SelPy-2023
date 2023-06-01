from Team.lau.test.Orden.sauce_login_page import LoginPage
from Team.lau.test.Orden.sauce_test_version3 import Page
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
VIEW_RESULT_PRINT8 = "//div[@class='summary_info']/child::div[8]"
checkout_name = "Laura"
checkout_lastname = "Curtidor"
checkout_zip = "044510"

# Clases

my_test_run = LoginPage()
my_test_run.do_login()
