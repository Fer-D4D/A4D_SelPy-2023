from core.common2 import TinyCore
class TestData:
    search_text_name = "standard_user"
    search_text_password = "secret_sauce"
class LoginPage(TinyCore):
    SEARCH_USERNAME_TEXT = "CSS:#user-name"
    SEARCH_PASSWORD_TEXT = "CSS:#password"
    SEARCH_BUTTON = "CSS:.submit-button.btn_action"
    def get_username_text(self):
        return self.SEARCH_USERNAME_TEXT

    def get_password_text(self):
        return self.SEARCH_PASSWORD_TEXT

    def get_submit_text(self):
        return self.SEARCH_BUTTON
    def do_login(self):
        # self.set_driver(self.driver)
        self.fill_input_text(self.SEARCH_USERNAME_TEXT, TestData.search_text_name)
        self.fill_input_text(self.SEARCH_PASSWORD_TEXT, TestData.search_text_password)
        self.do_click(self.SEARCH_BUTTON)

class AddProducts:
    ADD_FIRST_ITEM = "CSS:#add-to-cart-sauce-labs-backpack"
    ADD_SECOND_ITEM = "CSS:#add-to-cart-sauce-labs-fleece-jacket"
    ADD_THIRD_ITEM = "CSS:#add-to-cart-sauce-labs-onesie"
    ADD_SHIRT_ITEM = "XPATH://button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    VIEW_CAR_OPTION = "XPATH://a[@class='shopping_cart_link']"
    VIEW_RESULT_ITEM1 = "XPATH://div[@class='cart_item_label']//a[@id='item_4_title_link']/child::div[1]"
    VIEW_RESULT_ITEM2 = "XPATH://div[@class='cart_item_label']//a[@id='item_3_title_link']/child::div[1]"
    VIEW_RESULT_PRICE = "XPATH://*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
    IMAGE_FIRST_ITEM = "XPATH://div[@class='inventory_item_img']//a[@id='item_4_img_link']/child::img"
    IMAGE_SHIRT_ITEM = "XPATH://div[@class='inventory_item_img']//a[@id='item_3_img_link']/child::img"
    BACK_BUTTON = "XPATH://button[@id='back-to-products']"
    REMOVE_FIRST_ITEM = "CSS:#remove-sauce-labs-backpack"
    def add_items_car(self):
        return self.ADD_FIRST_ITEM, self.ADD_SECOND_ITEM, self.ADD_THIRD_ITEM
    def viewcar_items(self):
        return self.VIEW_CAR_OPTION
    def view_result(self):
        return self.VIEW_RESULT_ITEM1, self.VIEW_RESULT_ITEM2, self.VIEW_RESULT_PRICE
    def add_firstitem(self):
        return self.IMAGE_FIRST_ITEM
    def add_shirtitem(self):
        return self.IMAGE_SHIRT_ITEM

class ResultsPage:
    FIRST_RESULT_TITTLE_SPAN = "Ha iniciado sesión exitosamente"
    PRODUCT_ADDED = "Your product were added"
    def get_result_text(self):
        return self.FIRST_RESULT_TITTLE_SPAN
    def get_added_text(self):
        return self.PRODUCT_ADDED
