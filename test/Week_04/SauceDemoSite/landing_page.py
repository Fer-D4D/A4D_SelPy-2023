from core.Common_II import TinyCore


def check_button_state(button_web_element):
    if button_web_element != "remove":
        return True
    return False


class LandingPage:
    driver = None
    letsAutomate_landingPage = None
    VIEWER_MODE = False

    __selectors_dic = {"Title": "XPATH://div[text()='Swag Labs']",
                       "ShoppingCart": "XPATH://div[@id='shopping_cart_container']/a",
                       "ShoppingCartCounter": "XPATH://div[@id='shopping_cart_container']//span",
                       "SauceLabsBackPack_AddToCart_Button": "ID:add-to-cart-sauce-labs-backpack",
                       "SauceLabsBackPack_Remove_Button": "ID:remove-sauce-labs-backpack",
                       "SauceItemsDynamicID": "XPATH://*[@id='$%$']",
                       "ItemName": "CSS:.inventory_item_name"}

    def get_selector(self, desired_selector):
        return self.__selectors_dic[desired_selector]

    def set_viewer_mode(self, viewer_mode="Viewer-Mode-OFF"):
        if "on" in viewer_mode.lower():
            self.letsAutomate_landingPage.set_viewer_mode(viewer_mode)

    def __init__(self, driver):
        self.driver = driver
        self.letsAutomate_landingPage = TinyCore()
        self.letsAutomate_landingPage.set_driver(self.driver)

    def check_expected_text(self, text):
        if self.letsAutomate_landingPage.get_element_inner_text(self.get_selector("Title")) is not None:
            return self.letsAutomate_landingPage.get_element_inner_text(self.get_selector("Title")) == text
        return False

    def check_shopping_cart(self):
        if self.letsAutomate_landingPage.get_number_of_elements(self.get_selector("ShoppingCartCounter")) == 1:
            return self.letsAutomate_landingPage.get_element_inner_text(self.get_selector("ShoppingCartCounter"))
        return '0'

    def add_item_to_shopping_cart(self, item_selector):
        self.letsAutomate_landingPage.viewer_mode()
        if self.letsAutomate_landingPage.get_number_of_elements(item_selector) > 0 \
                and self.letsAutomate_landingPage.get_element_inner_text(item_selector).lower() != "remove":
            self.letsAutomate_landingPage.do_click(item_selector)

    def remove_item_from_shopping_cart(self, item_selector):
        self.letsAutomate_landingPage.viewer_mode()
        if self.letsAutomate_landingPage.get_number_of_elements(item_selector) > 0 \
                and self.letsAutomate_landingPage.get_element_inner_text(item_selector).lower() == "remove":
            self.letsAutomate_landingPage.do_click(item_selector)

    def add_all_items(self):
        items = self.letsAutomate_landingPage.get_elements_list(self.get_selector("ItemName"))
        if len(items) > 0:
            for item in items:
                # print(self.gen_item_selector(item.text, "add"))
                self.add_item_to_shopping_cart(self.gen_item_selector(item.text, "add"))

    def gen_item_selector(self, item_description_text, selector_type):
        main_text = item_description_text.replace(" ", "-").lower()
        if selector_type.lower() == "add":
            return self.get_selector("SauceItemsDynamicID").replace("$%$", "add-to-cart-" + main_text)
        else:
            return self.get_selector("SauceItemsDynamicID").replace("$%$", "remove-" + main_text)
