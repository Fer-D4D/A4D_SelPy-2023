from Team.lau.test.Week1.sauce_test_methods import Page
from selenium.webdriver.common.by import By

class Prodlocators:

    ADD_FIRST_ITEM = "#add-to-cart-sauce-labs-backpack"
    ADD_SHIRT_ITEM = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    VIEW_CAR_OPTION = "//a[@class='shopping_cart_link']"
    IMAGE_SHIRT_ITEM = "//div[@class='inventory_item_img']//a[@id='item_3_img_link']/child::img"
    IMAGE_SHIRT_ITEM_ID = "item_3_img_link"
    TITLE_SHIRT = "//a[@id='item_3_title_link']//div[@class='inventory_item_name']"
    BACK_BUTTON = "//button[@id='back-to-products']"
    REMOVE_FIRST_ITEM = "#remove-sauce-labs-backpack"
    CHECKOUT_BUTTON = "//button[@id='checkout']"
    CHECKOUT_NAME = "//input[@id='first-name']"
    CHECKOUT_LASTNAME = "//input[@id='last-name']"
    CHECKOUT_ZIP = "//input[@id='postal-code']"
    CHECKOUT_CONTINUE = "//input[@id='continue']"
    VIEW_RESULT_PRINT8 = "//div[@class='summary_info']/child::div[8]"


class Checkout:
    checkout_name = "Laura"
    checkout_lastname = "Curtidor"
    checkout_zip = "044510"

class AddProducts(Page):

    def __init__(self):
        super().__init__()

    def adding_to_cart(self):
        self.do_click(By.CSS_SELECTOR, Prodlocators.ADD_FIRST_ITEM)
        self.do_click(By.XPATH, Prodlocators.IMAGE_SHIRT_ITEM)
        self.do_click(By.XPATH, Prodlocators.ADD_SHIRT_ITEM)
        self.back_page()
        self.do_click(By.CSS_SELECTOR, Prodlocators.REMOVE_FIRST_ITEM)
