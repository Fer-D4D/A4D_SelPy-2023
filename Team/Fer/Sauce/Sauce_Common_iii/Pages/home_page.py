from Team.Fer.core.common_iii import TinyCore


class Selectors:
    LANDING_PAGE_HEADER = "XPATH://div[text()='Swag Labs']"
    SHOPPING_CART_ICON = "XPATH://div[@id='shopping_cart_container']/a"
    SHOPPING_CART_COUNTER = "XPATH://div[@id='shopping_cart_container']//span"
    DYNAMIC_ITEM_BUTTON = "XPATH://*[@id='$%$']"
    DYNAMIC_ITEM_IMG = "XPATH://img[@alt='$%$']"
    GENERIC_ITEM_DEFINITION = "CSS:.inventory_item_name"
    BURGER_BUTTON = "ID:react-burger-menu-btn"
    LOGOUT_LINK = "ID:logout_sidebar_link"
    RESET_PRODUCTS = "ID:reset_sidebar_link"


class TestData:
    EXPECTED_TITTLE_TEXT = "Swag Labs - Wrong"
    REPLACEMENT_TOKEN = "$%$"


class HomePage(TinyCore):

    def __init__(self, tiny_core_object):
        super().__init__(tiny_core_object.TEST_URL)
        self.DRIVER = tiny_core_object.DRIVER
        self.VIEWER_MODE = tiny_core_object.VIEWER_MODE
        self.VERBOSE_MODE = tiny_core_object.VERBOSE_MODE
        self.HIGHLIGHT_MODE = tiny_core_object.HIGHLIGHT_MODE
        self.FLOW_CONTROL_FLAG = tiny_core_object.FLOW_CONTROL_FLAG

    @staticmethod
    def get_trusted_selector():
        return Selectors.SHOPPING_CART_ICON

    def add_item_to_shopping_cart(self, item_name):
        item_name = item_name.replace(" ", "-").lower()
        return self.do_click_and_check(Selectors.DYNAMIC_ITEM_BUTTON,
                                       Selectors.DYNAMIC_ITEM_BUTTON,
                                       "add-to-cart-" + item_name,
                                       "remove-" + item_name)

    def add_items_to_shopping_cart_from_list(self, item_names_list):
        for item_name in item_names_list:
            self.add_item_to_shopping_cart(item_name.strip())

