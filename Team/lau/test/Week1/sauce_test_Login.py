from selenium.webdriver.common.by import By
from Team.lau.test.Week1.sauce_test_methods import Page

class Locators:
    SEARCH_USERNAME_TEXT = "#user-name"
    SEARCH_PASSWORD_TEXT = "#password"
    SEARCH_BUTTON = ".submit-button.btn_action"


class Data:
    search_text_name = "standard_user"
    search_text_password = "secret_sauce"

class Login(Page):

    def __init__(self):
        super().__init__()

    def do_login(self, username=Data.search_text_name, password=Data.search_text_password):
        self.launch_site()
        self.fill_text_to_element(By.CSS_SELECTOR, Locators.SEARCH_USERNAME_TEXT, username)
        self.fill_text_to_element(By.CSS_SELECTOR, Locators.SEARCH_PASSWORD_TEXT, password)
        self.do_click(By.CSS_SELECTOR, Locators.SEARCH_BUTTON)

