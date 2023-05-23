from Team.Fer.Sauce.landing_page import LandingPage


class Selectors:
    ITEM_TITLE = "XPATH://div[@class='inventory_details_name large_size']"
    BACK_TO_PRODUCTS_LINK = "ID:back-to-products"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"


class ProductPage(LandingPage):
    ProductPageSelectors = Selectors()
    t = TestData()

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(self.driver)
        self.driver = driver
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def lets_back_to_products(self):
        if self.get_number_of_elements(self.ProductPageSelectors.BACK_TO_PRODUCTS_LINK) == 1:
            self.do_click(self.ProductPageSelectors.BACK_TO_PRODUCTS_LINK)

