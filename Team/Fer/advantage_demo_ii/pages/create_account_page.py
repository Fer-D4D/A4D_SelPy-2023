from Team.Fer.core.Common_II import TinyCore, waste_some_time


class Selectors:
    USER_NAME_FORM_FIELD = "XPATH://*[@name='usernameRegisterPage']"
    PASSWORD_FORM_FIELD = "XPATH://*[@name='passwordRegisterPage']"
    EMAIL_FORM_FIELD = "XPATH://*[@name='emailRegisterPage']"
    CONFIRM_PASSWORD_FORM_FIELD = "XPATH://*[@name='confirm_passwordRegisterPage']"

    FIRST_NAME_FORM_FIELD = "XPATH://*[@name='first_nameRegisterPage']"
    LAST_NAME_FORM_FIELD = "XPATH://*[@name='last_nameRegisterPage']"
    PHONE_NUMBER_FORM_FIELD = "XPATH://*[@name='phone_numberRegisterPage']"

    COUNTRY_FORM_SELECT = "XPATH://*[@name='countryListboxRegisterPage']"
    CITY_FORM_FIELD = "XPATH://*[@name='cityRegisterPage']"
    ADDRESS_FORM_FIELD = "XPATH://*[@name='addressRegisterPage']"
    STATE_PROVINCE_FORM_FIELD = "XPATH://*[@name='state_/_province_/_regionRegisterPage']"
    POSTAL_CODE_FORM_FIELD = "XPATH://*[@name='postal_codeRegisterPage']"

    RECEIVE_EXCLUSIVE_OFFERS_FORM_CHECK = "XPATH://*[@name='allowOffersPromotion']"
    RECEIVE_EXCLUSIVE_OFFERS_FORM_LABEL = "CSS:.roboto-light.ng-scope"

    I_AGREE_FORM_CHECK = "XPATH://*[@name='i_agree']"
    I_AGREE_FORM_LABEL = "CSS:.checkboxText.roboto-light.animated"

    REGISTER_BUTTON = "ID:register_btnundefined"
    ALREADY_HAVE_AN_ACCOUNT_MESSAGE = "CSS:.ALREADY_HAVE_AN_ACCOUNT.roboto-medium a"
    USER_NAME_ERROR_MESSAGE = "CSS:.center.block.smollMargin.invalid"


class TestData:
    USER_NAME = "DonFer"
    PASSWORD = "AAbb77"
    EMAIL = "elfer@nowhere.net"

    FIRST_NAME = "Fer"
    LAST_NAME = "Mtz"
    PHONE_NUMBER = "33770909"

    COUNTRY = "Mexico"
    CITY = "Zapopan"
    ADDRESS = "Av Siempre Viva 123"
    STATE_PROVINCE = "Jalisco"
    POSTAL_CODE = "44080"

    RECEIVE_EXCLUSIVE_OFFERS_FORM_CHECK = True
    I_AGREE_FORM_CHECK = False


class CreateAccountPage(TinyCore):
    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def fill_form_generic_values(self, user_name=TestData.USER_NAME):
        self.wait_for_page_safe_load(Selectors.USER_NAME_FORM_FIELD)
        self.fill_input_text(Selectors.USER_NAME_FORM_FIELD, user_name)
        self.fill_input_text(Selectors.PASSWORD_FORM_FIELD, TestData.PASSWORD)
        self.fill_input_text(Selectors.CONFIRM_PASSWORD_FORM_FIELD, TestData.PASSWORD)
        self.fill_input_text(Selectors.EMAIL_FORM_FIELD, TestData.EMAIL)
        self.fill_input_text(Selectors.FIRST_NAME_FORM_FIELD, TestData.FIRST_NAME)
        self.fill_input_text(Selectors.LAST_NAME_FORM_FIELD, TestData.LAST_NAME)
        self.fill_input_text(Selectors.PHONE_NUMBER_FORM_FIELD, TestData.PHONE_NUMBER)
        self.select_value_from_dropdown(Selectors.COUNTRY_FORM_SELECT, TestData.COUNTRY)
        self.fill_input_text(Selectors.CITY_FORM_FIELD, TestData.CITY)
        self.fill_input_text(Selectors.STATE_PROVINCE_FORM_FIELD, TestData.STATE_PROVINCE)
        self.fill_input_text(Selectors.ADDRESS_FORM_FIELD, TestData.ADDRESS)
        self.fill_input_text(Selectors.POSTAL_CODE_FORM_FIELD, TestData.POSTAL_CODE)
        self.uncheck_checkbox(Selectors.RECEIVE_EXCLUSIVE_OFFERS_FORM_CHECK)
        self.check_checkbox(Selectors.I_AGREE_FORM_CHECK)

    def proceed_and_register_account(self):
        self.do_click(Selectors.REGISTER_BUTTON)

    def check_create_account_attempt_result(self):
        waste_some_time()
        return not (self.get_number_of_elements(Selectors.USER_NAME_ERROR_MESSAGE) > 0)
