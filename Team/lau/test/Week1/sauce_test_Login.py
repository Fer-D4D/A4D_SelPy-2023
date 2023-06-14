from selenium.webdriver.common.by import By
from Team.lau.test.Week1.sauce_test_methods import Page

class Locators:
    SEARCH_USERNAME_TEXT = "#user-name"
    SEARCH_PASSWORD_TEXT = "#password"
    SEARCH_BUTTON = ".submit-button.btn_action"
    ERROR_LOGIN = "//div[@class='error-message-container error']//h3"
    ERROR_BUTTON = ".error-button"


class Data:
    search_text_name = "standard_user"
    search_text_password = "secret_sauce"
    search_error_name = "user"

class Login(Page):

    def do_login(self, username=Data.search_text_name, password=Data.search_text_password):
        self.launch_site()
        self.fill_text_to_element(By.CSS_SELECTOR, Locators.SEARCH_USERNAME_TEXT, username)
        self.fill_text_to_element(By.CSS_SELECTOR, Locators.SEARCH_PASSWORD_TEXT, password)
        self.do_click(By.CSS_SELECTOR, Locators.SEARCH_BUTTON)

    def validate_login(self):
        self.do_login(username=Data.search_error_name)
        errormessage = self.get_text_to_element(By.XPATH, Locators.ERROR_LOGIN)
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        if errormessage == expected_error_message:
            print("Your account is not valid, Try Again")
            self.do_click(By.CSS_SELECTOR, Locators.ERROR_BUTTON)
            self.delay_time(2)
            self.do_login()
            print("You are in all set")
        else:
            self.refresh_to_page()