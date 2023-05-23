from Team.Adriana.Sauce1.landing_page import LandingPage


class Selectors:
    CONTINUE_BUTTON = "ID:continue"
    CANCEL_BUTTON = "ID:cancel"
    FIRST_NAME_FORM_FIELD = "ID:first-name"
    LAST_NAME_FORM_FIELD = "ID:last-name"
    POSTAL_CODE_FORM_FIELD = "ID:postal-code"



class TestData:
    FIRST_NAME = "Adriana"
    LAST_NAME = "Ramirez"
    POSTAL_CODE = "45200"


class YourInformationPage(LandingPage):
    yips = Selectors()
    yiptd = TestData()

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(self.driver)
        self.driver = driver
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def do_fill_form(self):
        self.fill_input_text(self.yips.FIRST_NAME_FORM_FIELD, self.yiptd.FIRST_NAME)
        self.fill_input_text(self.yips.LAST_NAME_FORM_FIELD, self.yiptd.LAST_NAME)
        self.fill_input_text(self.yips.POSTAL_CODE_FORM_FIELD, self.yiptd.POSTAL_CODE)
        self.do_click(self.yips.CONTINUE_BUTTON)
