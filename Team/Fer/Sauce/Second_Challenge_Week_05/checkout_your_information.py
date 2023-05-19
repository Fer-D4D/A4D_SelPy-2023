from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage


class Selectors:
    FIRST_NAME = "ID:first-name"
    LAST_NAME = "ID:last-name"
    POSTAL_CODE = "ID:postal-code"
    CONTINUE_BUTTON = "ID:continue"


class TestData:
    FIRST_NAME = "Fer"
    LAST_NAME = "Perez"
    POSTAL_CODE = "77777"


class CheckoutYourInformation(LandingPage):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(driver)
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def fill_your_information_form(self, first_name=TestData.FIRST_NAME,
                                   last_name=TestData.LAST_NAME,
                                   postal_code=TestData.POSTAL_CODE):
        if self.safe_to_proceed(Selectors.FIRST_NAME):
            self.fill_input_text(Selectors.FIRST_NAME, first_name)
            self.fill_input_text(Selectors.LAST_NAME, last_name)
            self.fill_input_text(Selectors.POSTAL_CODE, postal_code)

    def proceed_to_checkout_overview(self):
        if self.safe_to_proceed(Selectors.CONTINUE_BUTTON):
            self.do_click(Selectors.CONTINUE_BUTTON)