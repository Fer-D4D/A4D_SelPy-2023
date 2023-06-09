from core.Common_II import TinyCore

# Test Data
TEST_URL = "http://advantageonlineshopping.com/"
BROWSER = "edge"
TEST_USER_NAME = "A4DUser-FER"
TEST_EMAIL = "fer@a4d.tv"
GENERIC_PASSWORD = "aaBB22"
VIEWER_MODE = "ON"
VERBOSE_MODE = "ON"
HIGHLIGHT_MODE = "ON"

# Test Web Elements

MENU_USER_ICON_LOCATOR = "CSS:#menuUser"
XPATH_CREATE_NEW_ACCOUNT_LINK_SING_IN_LOCATOR = "XPATH://*/a[contains(., 'CREATE NEW ACCOUNT')]"
USERNAME_INPUT_CREATE_ACCOUNT_LOCATOR = "CSS:input[name='usernameRegisterPage']"
EMAIL_INPUT_CREATE_ACCOUNT_LOCATOR = "CSS:input[name='emailRegisterPage']"
PASSWORD_INPUT_CREATE_ACCOUNT_LOCATOR = "XPATH://*/input[@name='passwordRegisterPage']"
CONFIRM_PASSWORD_INPUT_CREATE_ACCOUNT_LOCATOR = "XPATH://*/input[@name='confirm_passwordRegisterPage']"
I_AGREE_CONDITIONS_CREATE_ACCOUNT_LOCATOR = "CSS:input[name='i_agree']"
REGISTER_BUTTON_CREATE_ACCOUNT_LOCATOR = "ID:register_btnundefined"
ALREADY_REGISTERED_MSG_CREATE_ACCOUNT_LOCATOR = "CSS:label[class='invalid center block smollMargin']"


# Test Actions
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, MENU_USER_ICON_LOCATOR)

letsAutomate.do_click(MENU_USER_ICON_LOCATOR)
