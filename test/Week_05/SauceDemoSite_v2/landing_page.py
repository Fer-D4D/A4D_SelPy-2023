from selenium.common import NoSuchElementException

from core.Common_II import TinyCore


class SelectorsDic:
    LANDING_PAGE_HEADER = "XPATH://div[text()='Swag Labs']"
    SHOPPING_CART_ICON = "XPATH://div[@id='shopping_cart_container']/a"
    SHOPPING_CART_COUNTER = "XPATH://div[@id='shopping_cart_container']//span"
    DYNAMIC_ITEM_BUTTON = "XPATH://*[@id='$%$']"


class TestData:
    EXPECTED_TITTLE_TEXT = "Swag Labs"
    REPLACEMENT_TOKEN = "$%$"


def map_button_state_to_boolean(button_state):
    try:
        if "add" in button_state.lower():
            return True
        if "remove" in button_state.lower():
            return False
    except AttributeError:
        return False


class LandingPage(TinyCore):
    sd = SelectorsDic()
    td = TestData()

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.driver = driver
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def check_for_login_granted(self):
        return self.wait_for_page_safe_load(self.sd.SHOPPING_CART_ICON) and \
               self.compare_element_inner_text(self.sd.LANDING_PAGE_HEADER, self.td.EXPECTED_TITTLE_TEXT)

    def gen_item_selector(self, item_description_text, add_button=True):
        main_text = item_description_text.replace(" ", "-").lower()
        if add_button:
            return self.sd.DYNAMIC_ITEM_BUTTON.replace(self.td.REPLACEMENT_TOKEN, "add-to-cart-" + main_text)
        else:
            return self.sd.DYNAMIC_ITEM_BUTTON.replace(self.td.REPLACEMENT_TOKEN, "remove-" + main_text)

    def get_button_state(self, locator_definition):
        try:
            return map_button_state_to_boolean(self.get_element_inner_text(self.gen_item_selector(locator_definition)))
        except NoSuchElementException:
            return map_button_state_to_boolean(self.get_element_inner_text(self.gen_item_selector(locator_definition, False)))

    def add_item_to_shopping_cart(self, item_selector):
        if self.get_button_state(item_selector):
            self.do_click(self.gen_item_selector(item_selector))

    def remove_item_from_shopping_cart(self, item_selector):
        if not self.get_button_state(item_selector):
            self.do_click(self.gen_item_selector(item_selector, False))
