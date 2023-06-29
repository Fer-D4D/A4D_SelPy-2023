from selenium.webdriver.common.by import By

from Team.Fer.orange_challenge.login_step_by_step.login_iv_a.framework.common_iv import TinyCore


class LOCATORS:
    USERNAME_FIELD = "//*[@name='username']"
    PASSWORD_FIELD = "//*[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"


class TESTDATA:
    USERNAME = "Admin"
    PASSWORD = "admin123"


class LoginPage(TinyCore):
    def __init__(self, working_driver):
        super(LoginPage, self).__init__()
        self.MAIN_DRIVER = working_driver

    def do_login(self):
        self.snore(2)
        self.MAIN_DRIVER.find_element(By.XPATH, LOCATORS.USERNAME_FIELD).send_keys(TESTDATA.USERNAME)
        self.MAIN_DRIVER.find_element(By.XPATH, LOCATORS.PASSWORD_FIELD).send_keys(TESTDATA.PASSWORD)
        self.MAIN_DRIVER.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
