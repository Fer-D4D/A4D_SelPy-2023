from Team.Fer.core.Common_II import TinyCore


class Selectors:
    USER_NAME_FORM_FIELD = "ID:user-name"
    PASSWORD_FORM_FIELD = "ID:password"
    LOGIN_BUTTON = "ID:login-button"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"


class LoginPage(TinyCore):
    sd = Selectors()
    td = TestData()

    def __init__(self, browser='chrome', viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_browser(browser)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def do_login(self, user_name=td.STANDARD_USER_NAME):
        self.fill_login_form(user_name)
        self.proceed_landing_page()

    def fill_login_form(self, user_name=td.STANDARD_USER_NAME):
        self.fill_input_text(self.sd.USER_NAME_FORM_FIELD, user_name)
        self.fill_input_text(self.sd.PASSWORD_FORM_FIELD, self.td.GENERIC_PASSWORD)

    def proceed_landing_page(self):
        self.do_click(self.sd.LOGIN_BUTTON)
