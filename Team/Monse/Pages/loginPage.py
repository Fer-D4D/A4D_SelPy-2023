import time
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_id = "user-name"
        self.password_testbox_id = "password"
        self.login_button_id = "login-button"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_testbox_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.username_testbox_id).send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_testbox_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self.password_testbox_id).send_keys(password)
        time.sleep(2)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()
        time.sleep(2)