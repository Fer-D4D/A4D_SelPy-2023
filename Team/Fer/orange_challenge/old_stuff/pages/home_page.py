from Team.Fer.core.common_iv import TinyCore
from Team.Fer.orange_challenge.old_stuff.pages.admin_page import AdminPage


class LOCATORS:
    LEFT_MENU_ADMIN_OPTION = "XPATH://a/span[text()='Admin']"


class TESTDATA:
    USERNAME = "Admin"
    PASSWORD = "admin123"


class HomePage(TinyCore):
    def __init__(self, working_driver):
        super(HomePage, self).__init__()
        self.MAIN_DRIVER = working_driver

    def execute_left_menu_option(self, menu_option):
        if menu_option.lower() == "admin":
            self.do_click(LOCATORS.LEFT_MENU_ADMIN_OPTION)
            return AdminPage(self.MAIN_DRIVER)
