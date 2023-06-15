class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_id = "user-name"
        self.password_testbox_id = "password"
        self.login_button_id = "login-button"

    def enter_username(self, username):
        self.driver.find_element(self.username_testbox_id).clear()
        self.driver.find_element(self.username_testbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_testbox_id).clear()
        self.driver.find_element(self.password_testbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(self.login_button_id).click()