import self as self
from selenium.webdriver.common.by import By
from Team.lau.test.Week1.sauce_test_methods import Page

class Locators:
    ENROLL_NAME = "//input[@id='mui-1']"
    ENROLL_LASTNAME = "//input[@id='mui-2']"
    ENROLL_BIRTHDATE_YEAR = "//div[@id='mui-component-select-birthDate.year']"
    YEAR = "//*[@id='-open']/li[33]"
    ENROLL_BIRTHDATE_MONTH = "//div[@id='mui-component-select-birthDate.month']"
    ENROLL_BIRTHDATE_DAY = "//div[@id='mui-component-select-birthDate.day']"
    ENROLL_COUNTRY = "//div[@id='mui-component-select-nationality']"
    ENROLL_DOC = "//div[@id='mui-component-select-memberDoc.documentType']"
    ENROLL_DOC_NUM = "//input[@id='mui-22']"
    ENROLL_DOC_COUNTRY = "//div[@id='mui-component-select-memberDoc.issuingCountry']"
    ENROLL_DOC_DATE_YEAR = "//div[@id='mui-component-select-memberDoc.validUntil.year']"
    ENROLL_DOC_DATE_MONTH = "//div[@id='mui-component-select-memberDoc.validUntil.month']"
    ENROLL_DOC_DATE_DAY = "//div[@id='mui-component-select-memberDoc.validUntil.day']"
    ENROLL_EMAIL = "//input[@id='mui-3']"
    ENROLL_PASSWORD = "//input[@id='mui-4']"
    ENROLL_PIN = "//input[@id='mui-5']"
    ENROLL_BUTTON = "//*[@id='__next']/div[3]/div/div/form/div[3]/div[6]/button"

class Data:
    FILL_ENROLL_NAME = "Maria"
    FILL_ENROLL_LASTNAME = "Galindo"
    FILL_BIRTHDATE_YEAR = "1990"
    FILL_BIRTHDATE_MONTH = "//div[@id='mui-component-select-birthDate.month']"
    FILL_BIRTHDATE_DAY = "//div[@id='mui-component-select-birthDate.day']"
    FILL_ENROLL_DOC_NUM = "1116778999"
    FILL_ENROLL_EMAIL = "maria_galindo@eppam.com"
    FILL_ENROLL_PASSWORD = "Test12345"
    FILL_ENROLL_PIN = "2938"

class enrollment_form(Page):

    def do_enrollment(self):
        self.launch_site(base_url="https://copacom-qa.copa.s4n.co/es-gs/enrollment/")
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_NAME, Data.FILL_ENROLL_NAME)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_LASTNAME, Data.FILL_ENROLL_LASTNAME)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_BIRTHDATE_YEAR,
                                    By.XPATH, Locators.YEAR, Data.FILL_BIRTHDATE_YEAR,
                                    By.XPATH, Locators.YEAR)
