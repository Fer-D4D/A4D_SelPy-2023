from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage


class Selectors:
    PAGE_TITLE = "CSS:.title"
    CONTINUE_SHOPPING_BUTTON = "ID:continue-shopping"
    CHECKOUT_BUTTON = "ID:checkout"


class YourCart(LandingPage):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(driver)
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def proceed_to_checkout_your_information_page(self):
        if self.safe_to_proceed(Selectors.CHECKOUT_BUTTON):
            self.do_click(Selectors.CHECKOUT_BUTTON)
