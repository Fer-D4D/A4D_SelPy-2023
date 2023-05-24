from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage


class Selectors:
    ITEM_TITLE = "XPATH://div[@class='inventory_details_name large_size']"
    BACK_TO_PRODUCTS_LINK = "ID:back-to-products"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"


class ProductPage(LandingPage):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(driver)
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def lets_back_to_products(self):
        if self.get_number_of_elements(Selectors.BACK_TO_PRODUCTS_LINK) == 1:
            self.do_click(Selectors.BACK_TO_PRODUCTS_LINK)

