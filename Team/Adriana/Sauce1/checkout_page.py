from Team.Adriana.Sauce1.landing_page import LandingPage


class Selectors:
    CONTINUE_SHOPPING_BUTTON = "ID:continue-shopping"
    CHECKOUT_BUTTON = "ID:checkout"
class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"

class CheckoutPage(LandingPage):
    cps = Selectors()
    t = TestData()

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(self.driver)
        self.driver = driver
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def choice_continue_shopping(self):
        self.do_click(self.cps.CONTINUE_SHOPPING_BUTTON)

    def choice_checkout(self):
        self.do_click(self.cps.CHECKOUT_BUTTON)

