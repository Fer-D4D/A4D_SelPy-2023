from Team.Fer.core.Common_II import TinyCore


class Selectors:
    USER_NAME_FORM_FIELD = "ID:user-name"
    PASSWORD_FORM_FIELD = "ID:password"
    LOGIN_BUTTON = "ID:login-button"
    LANDING_PAGE_HEADER = "XPATH://div[text()='Swag Labs']"
    SHOPPING_CART_ICON = "XPATH://div[@id='shopping_cart_container']/a"
    SHOPPING_CART_COUNTER = "XPATH://div[@id='shopping_cart_container']//span"
    DYNAMIC_ITEM_BUTTON = "XPATH://*[@id='$%$']"
    DYNAMIC_ITEM_IMG = "XPATH://img[@alt='$%$']"
    GENERIC_ITEM_DEFINITION = "CSS:.inventory_item_name"
    BURGER_BUTTON = "ID:react-burger-menu-btn"
    LOGOUT_LINK = "ID:logout_sidebar_link"


class TestData:
    STANDARD_USER_NAME = "standard_user"
    GENERIC_PASSWORD = "secret_sauce"
    TEST_URL = "https://www.saucedemo.com/"


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


class LandingPage(TinyCore):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def check_for_login_granted(self):
        return self.wait_for_page_safe_load(Selectors.SHOPPING_CART_ICON) and \
               self.compare_element_inner_text(Selectors.LANDING_PAGE_HEADER, Selectors.LANDING_PAGE_HEADER)


mi_login_page = LoginPage()


driver_global = mi_login_page.launch_site(TestData.TEST_URL)

mi_landing_page = LandingPage(driver_global)

mi_login_page.do_login()

mi_landing_page.check_for_login_granted()
