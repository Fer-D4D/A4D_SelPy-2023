import time

from Team.Fer.core.common_iv import TinyCore


class LOCATORS:
    GENERIC_INPUT_FORM = "XPATH://label[text()='$%$']/parent::div/following-sibling::div//input"
    GENERIC_FAKE_DROPDOWN = "XPATH://label[text()='$%$']/parent::div/following-sibling::div"
    GENERIC_FAKE_DROPDOWN_OPTIONS = "XPATH://div[contains(@class, 'oxd-select-option')]/span"
    GENERIC_AUTOCOMPLETE_FIELD_RESULT = "XPATH://label[text()='$%$']/parent::div/following-sibling::div//span"
    GENERIC_SEARCH_RESULTS_CHECKBOX = "XPATH://div[contains(text(), '$%$')]/parent::div//preceding-sibling::div//label"
    SEARCH_BUTTON = "XPATH://button[@type='submit']"
    ADD_BUTTON = "XPATH://button[text()=' Add ']"


class TESTDATA:
    USERNAME = "Charlie"
    USER_ROLE = "Admin"


class AdminPage(TinyCore):
    def __init__(self, working_driver):
        super(AdminPage, self).__init__()
        self.MAIN_DRIVER = working_driver

    def search_user(self):
        self.fill_field(LOCATORS.GENERIC_INPUT_FORM, TESTDATA.USERNAME, "Username")
        self.do_click(LOCATORS.GENERIC_FAKE_DROPDOWN, "User Role")
        self.set_fake_dropdown_value(LOCATORS.GENERIC_FAKE_DROPDOWN_OPTIONS, "Admin")

        self.do_click(LOCATORS.SEARCH_BUTTON)

    def search_user_autocomplete(self):
        self.fill_field(LOCATORS.GENERIC_INPUT_FORM, TESTDATA.USERNAME, "Employee Name")
        self.do_click(LOCATORS.GENERIC_AUTOCOMPLETE_FIELD_RESULT, "Employee Name")
        self.do_click(LOCATORS.GENERIC_FAKE_DROPDOWN, "Status")
        self.set_fake_dropdown_value(LOCATORS.GENERIC_FAKE_DROPDOWN_OPTIONS, "Enabled")
        self.do_click(LOCATORS.SEARCH_BUTTON)
        self.do_click(LOCATORS.GENERIC_SEARCH_RESULTS_CHECKBOX, TESTDATA.USERNAME)

    def select_record_from_found_table(self):
        self.do_click("XPATH://div[text()='Username']/parent::div//label")
        #self.do_click(LOCATORS.GENERIC_SEARCH_RESULTS_CHECKBOX, "David.Morris")