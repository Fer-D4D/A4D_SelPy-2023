from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage


class Selectors:
    THANK_YOU_MESSAGE = "CSS:.complete-header"
    BACK_HOME_BUTTON = "ID:back-to-products"


class CheckoutComplete(LandingPage):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(driver)
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def confirm_order(self):
        return self.safe_to_proceed(Selectors.THANK_YOU_MESSAGE)

