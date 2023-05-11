import pytest_check as check

from core.Common_II import TinyCore

"""
Scenario:
As a standard user, I can log in to the Sauce website and see the Sauce home screen.
"""


def test_sauce_login():
    # Test Data
    TEST_URL = "https://www.saucedemo.com/"
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used

    # Test Elements
    # Login Page
    USER_NAME_FORM_TEXT = "ID:user-name"
    PASSWORD_FORM_TEXT = "ID:password"
    LOGIN_BUTTON = "ID:login-button"

    # Landing/Home Page
    TITLE_TEXT = "XPATH://div[text()='Swag Labs']"

    # Test actions
    lets_automate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
    lets_automate.launch_site(TEST_URL, LOGIN_BUTTON)

    lets_automate.fill_input_text(USER_NAME_FORM_TEXT, "standard_user")
    lets_automate.fill_input_text(PASSWORD_FORM_TEXT, "secret_sauce")
    lets_automate.do_click(LOGIN_BUTTON)

    check.equal(lets_automate.get_element_inner_text(TITLE_TEXT), "Swag Labs")
    check.is_true(lets_automate.get_element_inner_text(TITLE_TEXT) == "Swag Labs")

