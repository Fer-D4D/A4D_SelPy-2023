# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element_by_id("login_credentials").click()
        driver.find_element_by_id("login_credentials").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=login_credentials | ]]
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_id("user-name").clear()
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[2]/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[2]/div/div[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//div[@id='root']/div/div[2]/div[2]/div/div[2] | ]]
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a/span").click()
        driver.find_element_by_id("checkout").click()
        driver.find_element_by_id("first-name").click()
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("a")
        driver.find_element_by_id("last-name").click()
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("a")
        driver.find_element_by_id("postal-code").click()
        driver.find_element_by_id("postal-code").clear()
        driver.find_element_by_id("postal-code").send_keys("3")
        driver.find_element_by_id("continue").click()
        driver.find_element_by_id("finish").click()
        driver.find_element_by_id("back-to-products").click()
        driver.find_element_by_id("react-burger-menu-btn").click()
        driver.find_element_by_id("logout_sidebar_link").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
