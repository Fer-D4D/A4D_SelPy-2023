from Team.Fer.core.common_iii import TinyCore


class Selectors:
    USER_NAME_FORM_FIELD = "ID:user-name"
    PASSWORD_FORM_FIELD = "ID:password"
    LOGIN_BUTTON = "ID:login-button"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"


class LoginPage(TinyCore):

    def __init__(self, tiny_core_object):
        super().__init__(tiny_core_object.TEST_URL)
        self.DRIVER = tiny_core_object.DRIVER
        self.VIEWER_MODE = tiny_core_object.VIEWER_MODE
        self.VERBOSE_MODE = tiny_core_object.VERBOSE_MODE
        self.HIGHLIGHT_MODE = tiny_core_object.HIGHLIGHT_MODE
        self.FLOW_CONTROL_FLAG = tiny_core_object.FLOW_CONTROL_FLAG
        self.TEST_URL = tiny_core_object.TEST_URL

    def do_login_and_check(self, target_selector_definition,
                           user_name=TestData.STANDARD_USER_NAME,
                           password=TestData.GENERIC_PASSWORD):
        return self.fill_login_form(user_name, password) \
               and self.send_login_request(target_selector_definition)

    def fill_login_form(self, user_name=TestData.STANDARD_USER_NAME, password=TestData.GENERIC_PASSWORD):
        return self.launch_site(self.TEST_URL, Selectors.LOGIN_BUTTON) \
               and self.fill_form_element_and_check(Selectors.USER_NAME_FORM_FIELD, user_name) \
               and self.fill_form_element_and_check(Selectors.PASSWORD_FORM_FIELD, password)

    def send_login_request(self, target_selector_definition):
        return self.do_click_and_check(Selectors.LOGIN_BUTTON, target_selector_definition)

