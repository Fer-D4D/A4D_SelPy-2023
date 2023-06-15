from Team.Fer.core.common_iii import TinyCore


class Selectors:
    USER_MENU_ICON = "ID:menuUser"
    SIGNED_USER_MENU_ICON = "CSS:#menuUserLink span"
    LOGIN_POPUP_FACEBOOK_SIGN_IN_SPAN = "CSS:.facebook.ng-scope"
    LOGIN_POPUP_USER_NAME_FORM_FIELD = "XPATH://*[@name='username']"
    LOGIN_POPUP_PASSWORD_FORM_FIELD = "XPATH://*[@name='password']"
    LOGIN_POPUP_LOGIN_BUTTON = "ID:sign_in_btnundefined"
    LOGIN_POPUP_ERROR_MESSAGE = "ID:signInResultMessage"
    LOGIN_POPUP_CLOSE_BUTTON = "CSS:.closeBtn.loginPopUpCloseBtn"
    LOGIN_POPUP_CREATE_NEW_ACCOUNT_BUTTON = "CSS:.create-new-account.ng-scope"
    SIGNED_USER_MENU_OPTIONS = "XPATH://*[@id='loginMiniTitle']/label"

    GENERIC_BY_TOP_MENU_OPTIONS_LOCATOR = "XPATH://a[text()[contains(.,'%$%')]]"
    GENERIC_BY_TEXT_OUR_PRODUCTS_LOCATOR = "XPATH://span[text()[contains(.,'%$%')]]"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"


class HomePage(TinyCore):

    def __init__(self, browser='chrome', viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.define_browser(browser)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def fill_login_popup_form(self, username=TestData.STANDARD_USER_NAME, password=TestData.GENERIC_PASSWORD):
        return self.do_click_and_check(Selectors.USER_MENU_ICON, Selectors.LOGIN_POPUP_USER_NAME_FORM_FIELD) \
               and self.fill_form_element_and_check(Selectors.LOGIN_POPUP_USER_NAME_FORM_FIELD, username) \
               and self.fill_form_element_and_check(Selectors.LOGIN_POPUP_PASSWORD_FORM_FIELD, password)

    def proceed_to_login(self):
        return self.do_click(Selectors.LOGIN_POPUP_LOGIN_BUTTON)

    def do_login(self):
        self.fill_login_popup_form()
        self.proceed_to_login()



    def check_login_attempt_result(self, username=TestData.STANDARD_USER_NAME):
        waste_some_time(.2)
        return (self.get_number_of_elements(Selectors.SIGNED_USER_MENU_ICON) > 0 and
                self.get_element_inner_text(Selectors.SIGNED_USER_MENU_ICON) == username)

    def close_login_popup(self):
        self.do_click(Selectors.LOGIN_POPUP_CLOSE_BUTTON)

    def start_new_account_creation(self):
        self.do_click(Selectors.LOGIN_POPUP_CREATE_NEW_ACCOUNT_BUTTON)

    def select_user_menu_option(self, option):
        self.do_click(Selectors.USER_MENU_ICON)
        menu_options = self.get_elements_list(Selectors.SIGNED_USER_MENU_OPTIONS)
        waste_some_time(.4)
        for menu_option in menu_options:
            if self.compare_string_against_web_element_text(menu_option, option):
                menu_option.click()

    def use_top_menu_option(self, menu_option):
        if self.get_number_of_elements(Selectors.GENERIC_BY_TOP_MENU_OPTIONS_LOCATOR.replace("%$%", menu_option)) > 0:
            self.do_click(Selectors.GENERIC_BY_TOP_MENU_OPTIONS_LOCATOR.replace("%$%", menu_option))

    def go_to_product_category(self, product_category):
        if self.get_number_of_elements(
                Selectors.GENERIC_BY_TEXT_OUR_PRODUCTS_LOCATOR.replace("%$%", product_category)) > 0:
            self.do_click(Selectors.GENERIC_BY_TEXT_OUR_PRODUCTS_LOCATOR.replace("%$%", product_category))
