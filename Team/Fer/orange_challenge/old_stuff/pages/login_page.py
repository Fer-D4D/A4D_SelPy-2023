from Team.Fer.core.common_iv import TinyCore
from Team.Fer.orange_challenge.old_stuff.pages.home_page import HomePage


class LOCATORS:
    USERNAME_FIELD = "XPATH://*[@name='username']"
    PASSWORD_FIELD = "XPATH://*[@name='password']"
    LOGIN_BUTTON = "XPATH://button[@type='submit']"


class TESTDATA:
    USERNAME = "Admin"
    PASSWORD = "admin123"


class LoginPage(TinyCore):
    def __init__(self, working_driver):
        super(LoginPage, self).__init__()
        self.MAIN_DRIVER = working_driver

    def do_simple_login(self):
        self.fill_field(LOCATORS.USERNAME_FIELD, TESTDATA.USERNAME)
        self.fill_field(LOCATORS.PASSWORD_FIELD, TESTDATA.PASSWORD)
        self.do_click(LOCATORS.LOGIN_BUTTON)
        return HomePage(self.MAIN_DRIVER)
