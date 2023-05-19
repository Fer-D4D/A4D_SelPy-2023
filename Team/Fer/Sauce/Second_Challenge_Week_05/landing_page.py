from Team.Fer.core.Common_II import TinyCore


class SelectorsDic:
    LANDING_PAGE_HEADER = "XPATH://div[text()='Swag Labs']"
    SHOPPING_CART_ICON = "XPATH://div[@id='shopping_cart_container']/a"
    SHOPPING_CART_COUNTER = "XPATH://div[@id='shopping_cart_container']//span"
    DYNAMIC_ITEM_BUTTON = "XPATH://*[@id='$%$']"
    DYNAMIC_ITEM_IMG = "XPATH://img[@alt='$%$']"
    GENERIC_ITEM_DEFINITION = "CSS:.inventory_item_name"


class TestData:
    EXPECTED_TITTLE_TEXT = "Swag Labs"
    REPLACEMENT_TOKEN = "$%$"


def map_button_state_to_boolean(button_state):
    if "add" in button_state.lower():
        return True
    return False


class LandingPage(TinyCore):
    sd = SelectorsDic()
    td = TestData()

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def check_for_login_granted(self):
        return self.wait_for_page_safe_load(self.sd.SHOPPING_CART_ICON) and \
               self.compare_element_inner_text(self.sd.LANDING_PAGE_HEADER, self.td.EXPECTED_TITTLE_TEXT)

    def gen_button_item_selector(self, item_description_text, add_button=True):
        main_text = item_description_text.replace(" ", "-").lower()
        if add_button:
            return self.sd.DYNAMIC_ITEM_BUTTON.replace(self.td.REPLACEMENT_TOKEN, "add-to-cart-" + main_text)
        else:
            return self.sd.DYNAMIC_ITEM_BUTTON.replace(self.td.REPLACEMENT_TOKEN, "remove-" + main_text)

    def gen_img_item_selector(self, item_description_text):
        return self.sd.DYNAMIC_ITEM_IMG.replace(self.td.REPLACEMENT_TOKEN, item_description_text)

    def get_button_state(self, item_name):
        if self.get_number_of_elements(self.gen_button_item_selector(item_name)) == 1:
            return "add"
        elif self.get_number_of_elements(self.gen_button_item_selector(item_name, False)) == 1:
            return "remove"
        return "na"

    def add_item_to_shopping_cart(self, item_name):
        if "add" in self.get_button_state(item_name):
            self.do_click(self.gen_button_item_selector(item_name))

    def remove_item_from_shopping_cart(self, item_name):
        if "remove" in self.get_button_state(item_name):
            self.do_click(self.gen_button_item_selector(item_name, False))

    def img_clicking(self, item_name):
        return self.do_click(self.gen_img_item_selector(item_name))

    def get_shopping_cart_item_number(self):
        if self.get_number_of_elements(self.sd.SHOPPING_CART_COUNTER) != 0:
            return int(self.get_element_inner_text(self.sd.SHOPPING_CART_COUNTER))

    def add_items_to_shopping_cart_from_list(self, item_names_list):
        for item_name in item_names_list:
            self.add_item_to_shopping_cart(item_name)

    def remove_items_from_shopping_cart_from_list(self, item_names_list):
        for item_name in item_names_list:
            self.remove_item_from_shopping_cart(item_name)

    def get_added_item_names_list(self):
        items = self.get_elements_list(self.sd.GENERIC_ITEM_DEFINITION)
        item_names = []
        if len(items) > 0:
            for item in items:
                if self.get_button_state(item.text) == "remove":
                    item_names.append(item.text)
        return item_names

    def proceed_to_your_cart_page(self):
        if self.safe_to_proceed(self.sd.SHOPPING_CART_ICON):
            self.do_click(self.sd.SHOPPING_CART_ICON)
