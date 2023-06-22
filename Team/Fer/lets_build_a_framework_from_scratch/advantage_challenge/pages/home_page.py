from Team.Fer.core.common_iv import TinyCore
from Team.Fer.lets_build_a_framework_from_scratch.advantage_challenge.pages.create_new_account import CreateAccount


class LOCATORS:
    USER_MENU_ICON = "CSS:#menuUser"
    SIGN_IN_FORM_USERNAME_FIELD = "XPATH://*[@name='username']"
    SIGN_IN_FORM_CREATE_NEW_ACCOUNT_BUTTON = "CSS:.create-new-account.ng-scope"
    CREATE_NEW_ACCOUNT_HEADER = "XPATH://h3[text()='CREATE ACCOUNT']"
    FOLLOW_US = "ID:follow"


class TESTDATA:
    pass


class HomePage(TinyCore):

    def __init__(self, working_driver):
        super(HomePage, self).__init__()
        self.MAIN_DRIVER = working_driver
        self.check_for_page_readiness(LOCATORS.FOLLOW_US)

    def get_sign_in_form(self):
        return self.do_click_and_check(LOCATORS.USER_MENU_ICON,
                                       LOCATORS.SIGN_IN_FORM_USERNAME_FIELD)

    def go_create_new_account_page(self):
        if self.do_click_and_check(LOCATORS.USER_MENU_ICON,
                                   LOCATORS.SIGN_IN_FORM_USERNAME_FIELD) and \
                self.do_click_and_check(LOCATORS.SIGN_IN_FORM_CREATE_NEW_ACCOUNT_BUTTON,
                                        LOCATORS.CREATE_NEW_ACCOUNT_HEADER):
            return CreateAccount(self.MAIN_DRIVER)
