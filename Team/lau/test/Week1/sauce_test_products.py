from Team.lau.test.Week1.sauce_test_methods import Page
from selenium.webdriver.common.by import By

class Prodlocators:

    ADD_FIRST_ITEM = "#add-to-cart-sauce-labs-backpack"
    IMAGE_SHIRT_ITEM = "//div[@class='inventory_item_img']//a[@id='item_3_img_link']/child::img"
    ADD_SHIRT_ITEM = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    REMOVE_FIRST_ITEM = "#remove-sauce-labs-backpack"
    VIEW_CAR_OPTION = "//a[@class='shopping_cart_link']"
    TITLE_SHIRT = "//a[@id='item_3_title_link']//div[@class='inventory_item_name']"
    RESUME_SHIRT = "//div[@class='inventory_item_desc']"
    PRICE_SHIRT = "//div[@class='inventory_item_price']"
    BACK_BUTTON = "//button[@id='back-to-products']"
    CHECKOUT_BUTTON = "//button[@id='checkout']"
    CHECKOUT_NAME = "//input[@id='first-name']"
    CHECKOUT_LASTNAME = "//input[@id='last-name']"
    CHECKOUT_ZIP = "//input[@id='postal-code']"
    CHECKOUT_CONTINUE = "//input[@id='continue']"
    VIEW_RESULT_PRINT8 = "//div[@class='summary_info_label summary_total_label']"
    FINISH_BUTTON = "#finish"
    SUCCESS_MESSAGE = ".complete-header"

class Checkout:
    checkout_name = "Laura"
    checkout_lastname = "Curtidor"
    checkout_zip = "044510"

class AddProducts(Page):

    def __init__(self, OnDriver):
        self.set_driver(OnDriver)

    # PL = Prodlocators() tiene que llamarla self.PL.ADD_FIRST_ITEM
    def adding_to_cart(self):
        self.do_click(By.CSS_SELECTOR, Prodlocators.ADD_FIRST_ITEM)
        self.do_click(By.XPATH, Prodlocators.IMAGE_SHIRT_ITEM)
        self.do_click(By.XPATH, Prodlocators.ADD_SHIRT_ITEM)
        self.do_click(By.XPATH, Prodlocators.BACK_BUTTON)
        self.do_click(By.CSS_SELECTOR, Prodlocators.REMOVE_FIRST_ITEM)

    def summary_cart(self):
        self.do_click(By.XPATH, Prodlocators.VIEW_CAR_OPTION)
        print(self.get_text_to_element(By.XPATH, Prodlocators.TITLE_SHIRT))
        print(self.get_text_to_element(By.XPATH, Prodlocators.RESUME_SHIRT))
        print(self.get_text_to_element(By.XPATH, Prodlocators.PRICE_SHIRT))

    def set_checkout(self):
        self.do_click(By.XPATH, Prodlocators.CHECKOUT_BUTTON)
        self.fill_text_to_element(By.XPATH, Prodlocators.CHECKOUT_NAME, Checkout.checkout_name)
        self.fill_text_to_element(By.XPATH, Prodlocators.CHECKOUT_LASTNAME, Checkout.checkout_lastname)
        self.fill_text_to_element(By.XPATH, Prodlocators.CHECKOUT_ZIP, Checkout.checkout_zip)
        self.do_click(By.XPATH, Prodlocators.CHECKOUT_CONTINUE)
        print(self.get_text_to_element(By.XPATH, Prodlocators.VIEW_RESULT_PRINT8))
        self.do_click(By.CSS_SELECTOR, Prodlocators.FINISH_BUTTON)
        print(self.get_text_to_element(By.CSS_SELECTOR, Prodlocators.SUCCESS_MESSAGE))


