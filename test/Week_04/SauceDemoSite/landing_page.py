from core.Common_II import TinyCore


class LandingPage:
    driver = None
    letsAutomateLocal = None
    VIEWER_MODE = False

    __selectors_dic = {"Title": "XPATH://div[text()='Swag Labs']",
                       "ShoppingCart": "XPATH://div[@id='shopping_cart_container']/a",
                       "ShoppingCartCounter": "XPATH://div[@id='shopping_cart_container']//span",
                       "SauceLabsBackPack_AddToCart_Button": "ID:add-to-cart-sauce-labs-backpack",
                       "SauceLabsBackPack_Remove_Button": "ID:remove-sauce-labs-backpack",
                       "SauceItemsDynamicID": "ID:$%$"}

    def get_selector(self, desired_selector):
        return self.__selectors_dic[desired_selector]

    def set_viewer_mode(self, viewer_mode="Viewer-Mode-OFF"):
        if "on" in viewer_mode.lower():
            self.letsAutomateLocal.set_viewer_mode(viewer_mode)

    def __init__(self, driver):
        self.driver = driver
        self.letsAutomateLocal = TinyCore()
        self.letsAutomateLocal.set_driver(self.driver)

    def check_expected_text(self, text):
        if self.letsAutomateLocal.get_element_inner_text(self.get_selector("Title")) is not None:
            return self.letsAutomateLocal.get_element_inner_text(self.get_selector("Title")) == text
        return False

    def check_shopping_cart(self):
        if self.letsAutomateLocal.get_number_of_elements(self.get_selector("ShoppingCartCounter")) == 1:
            return self.letsAutomateLocal.get_element_inner_text(self.get_selector("ShoppingCartCounter"))
        return '0'

    def add_item_to_shopping_cart(self, item):
        self.letsAutomateLocal.viewer_mode()
        if self.letsAutomateLocal.get_number_of_elements(item) > 0 \
                and self.letsAutomateLocal.get_element_inner_text(item).lower() != "remove":
            self.letsAutomateLocal.do_click(item)

    def remove_item_from_shopping_cart(self, item):
        self.letsAutomateLocal.viewer_mode()
        if self.letsAutomateLocal.get_number_of_elements(item) > 0 \
                and self.letsAutomateLocal.get_element_inner_text(item).lower() == "remove":
            self.letsAutomateLocal.do_click(item)

    @staticmethod
    def gen_item_selector(item_description_text, selector_type):
        main_text = item_description_text.replace(" ", "-").lower()
        if selector_type.lower() == "add":
            return "ID:add-to-cart-" + main_text
        else:
            return "ID:remove-" + main_text
