from Team.Fer.core.common_iii import TinyCore


class Selectors:
    USER_MENU_ICON = "ID:menuUser"
    SIGNED_USER_MENU_ICON = "CSS:#menuUserLink span"
    GENERIC_BY_TEXT_OUR_PRODUCTS_LOCATOR = "XPATH://span[text()[contains(.,'%$%')]]"
    LOGIN_POPUP_USER_NAME_FORM_FIELD = "XPATH://*[@name='username']"


class Setup:
    TEST_URL = "http://advantageonlineshopping.com/"
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used


lets_automate = TinyCore()


lets_automate.start_driver()
