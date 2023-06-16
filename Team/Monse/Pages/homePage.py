import time
from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.home_page_items = "All Items"
        self.burger_menu_id = "react-burger-menu-btn"
        self.logout_link = "Logout"

    def click_mainpage(self):
        self.driver.find_element(By.ID, self.burger_menu_id).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.home_page_items).click()
        time.sleep(2)

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link).click()
        time.sleep(2)
