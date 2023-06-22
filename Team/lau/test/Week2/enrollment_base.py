import self as self
from selenium.webdriver.common.by import By
from Team.lau.test.Week1.sauce_test_methods import Page


class Locators:
    ENROLL_NAME = "//input[@id='mui-1']"
    ENROLL_LASTNAME = "//input[@id='mui-2']"
    ENROLL_BIRTHDATE_YEAR = "//div[@id='mui-component-select-birthDate.year']"
    ENROLL_BIRTHDATE_MONTH = "//div[@id='mui-component-select-birthDate.month']"
    ENROLL_BIRTHDATE_DAY = "//div[@id='mui-component-select-birthDate.day']"
    ENROLL_YEAR = "//*[@id='-open']/li[33]"
    ENROLL_MONTH = "//*[@id='-open']/li[3]"
    ENROLL_DAY = "//*[@id='-open']/li[10]"
    ENROLL_COUNTRY = "//div[@id='mui-component-select-nationality']"
    ENROLL_COUNTRY_OPTION = "//*[@id='-open']/li[51]"
    ENROLL_NUM_CONNECT = "//input[@id='mui-395']"
    ENROLL_DOC = "//div[@id='mui-component-select-memberDoc.documentType']"
    ENROLL_DOC_OPTION = "//*[@id='-open']/li[3]"
    ENROLL_DOC_NUMERO = "/html/body/div[1]/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/input"
    ENROLL_DOC_COUNTRY = "//div[@id='mui-component-select-memberDoc.issuingCountry']"
    ENROLL_DOC_DATE_YEAR = "//div[@id='mui-component-select-memberDoc.validUntil.year']"
    DOC_YEAR = "//*[@id='-open']/li[4]"
    ENROLL_DOC_DATE_MONTH = "//div[@id='mui-component-select-memberDoc.validUntil.month']"
    ENROLL_DOC_DATE_DAY = "//div[@id='mui-component-select-memberDoc.validUntil.day']"
    ENROLL_EMAIL = "//input[@id='mui-3']"
    ENROLL_PASSWORD = "//input[@id='mui-4']"
    ENROLL_PIN = "//input[@id='mui-5']"
    ENROLL_BUTTON = "/html/body/div[1]/div[3]/div/div/form/div[3]/div[6]/button"
    ACCEPT_MODAL_BUTTON = "/html/body/div[5]/div[3]/div[2]/button[2]"

class Data:
    FILL_ENROLL_NAME = "Maria"
    FILL_ENROLL_LASTNAME = "Galindo"
    Fill_ENROLL_YEAR = "1990"
    Fill_ENROLL_MONTH = "3"
    Fill_ENROLL_DAY = "10"
    Fill_ENROLL_COUNTRY = "colombia"
    Fill_ENROLL_DOC = "Cédula de identidad"
    FILL_ENROLL_DOC_NUM = "AG12451"
    FILL_YEAR_DOC = "2025"
    FILL_ENROLL_EMAIL = "maria_galindo@eppam.com"
    FILL_ENROLL_PASSWORD = "Test12345"
    FILL_ENROLL_PIN = "2938"

class Errors_labels:

    NAME_ERROR_REQ = "//span[text()='El campo es requerido']"
    NAME_ERROR_MIN = "//span[text()='Se requieren mínimo 2 caracteres']"
    NAME_ERROR_FILL_MIN = "M"
    NAME_ERROR_MAX = "//span[text()='El nombre incluido es muy largo']"
    NAME_ERROR_FILL_MAX = "asfjahsncksjhsnsjeusjanshrjaksnejsnahrjdnshajrmjalrjajrkamdrk"

class enrollment_form(Page):

    def launch_enroll_site(self):
        self.launch_site(base_url="https://copacom-qa.copa.s4n.co/es-gs/enrollment/")

    def do_enrollment(self):
        self.launch_enroll_site()
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_NAME, Data.FILL_ENROLL_NAME)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_LASTNAME, Data.FILL_ENROLL_LASTNAME)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_BIRTHDATE_YEAR,
                                    By.XPATH, Locators.ENROLL_YEAR, Data.Fill_ENROLL_YEAR,
                                    By.XPATH, Locators.ENROLL_YEAR)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_BIRTHDATE_MONTH,
                                    By.XPATH, Locators.ENROLL_MONTH, Data.Fill_ENROLL_MONTH,
                                    By.XPATH, Locators.ENROLL_MONTH)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_BIRTHDATE_DAY,
                                    By.XPATH, Locators.ENROLL_DAY, Data.Fill_ENROLL_DAY,
                                    By.XPATH, Locators.ENROLL_DAY)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_COUNTRY,
                                    By.XPATH, Locators.ENROLL_COUNTRY_OPTION, Data.Fill_ENROLL_COUNTRY,
                                    By.XPATH, Locators.ENROLL_COUNTRY_OPTION)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_DOC,
                                    By.XPATH, Locators.ENROLL_DOC_OPTION, Data.Fill_ENROLL_DOC,
                                    By.XPATH, Locators.ENROLL_DOC_OPTION)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_DOC_COUNTRY,
                                    By.XPATH, Locators.ENROLL_COUNTRY_OPTION, Data.Fill_ENROLL_COUNTRY,
                                    By.XPATH, Locators.ENROLL_COUNTRY_OPTION)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_DOC_DATE_YEAR,
                                    By.XPATH, Locators.DOC_YEAR, Data.FILL_YEAR_DOC,
                                    By.XPATH, Locators.DOC_YEAR)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_DOC_DATE_MONTH,
                                    By.XPATH, Locators.ENROLL_MONTH, Data.Fill_ENROLL_MONTH,
                                    By.XPATH, Locators.ENROLL_MONTH)
        self.choose_dropdown_option(By.XPATH, Locators.ENROLL_DOC_DATE_DAY,
                                    By.XPATH, Locators.ENROLL_DAY, Data.Fill_ENROLL_DAY,
                                    By.XPATH, Locators.ENROLL_DAY)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_DOC_NUMERO, Data.FILL_ENROLL_DOC_NUM)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_EMAIL, Data.FILL_ENROLL_EMAIL)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_PASSWORD, Data.FILL_ENROLL_PASSWORD)
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_PIN, Data.FILL_ENROLL_PIN)
        self.do_click(By.XPATH, Locators.ENROLL_BUTTON)

    def validate_name_error(self):
        self.launch_enroll_site()
        self.find_text_to_element(By.XPATH, Locators.ENROLL_NAME).clear()
        self.do_click(By.XPATH, Locators.ENROLL_NAME)
        self.do_click(By.XPATH, Locators.ENROLL_LASTNAME)
        errormessagerequired = self.get_text_to_element(By.XPATH, Errors_labels.NAME_ERROR_REQ)
        expected_error_message = "El campo es requerido"
        if errormessagerequired == expected_error_message:
            print("Character validation failed, this field is required please enter a valid name")
        else:
            print("Character validation ok")
        self.delay_time(2)
        self.find_text_to_element(By.XPATH, Locators.ENROLL_NAME).clear()
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_NAME, Errors_labels.NAME_ERROR_FILL_MIN)
        min_name_length = self.get_text_to_element(By.XPATH, Locators.ENROLL_NAME)
        min_name_length = len(min_name_length)
        errormessagerequired = self.get_text_to_element(By.XPATH, Errors_labels.NAME_ERROR_MIN)
        expected_error_message = "Se requieren mínimo 2 caracteres"
        if min_name_length <= 1 and errormessagerequired == expected_error_message:
            print("Character validation failed, you need more than 1 letter please enter a valid name")
        else:
            print("Character validation ok")
        self.delay_time(2)
        self.find_text_to_element(By.XPATH, Locators.ENROLL_NAME).clear()
        self.fill_text_to_element(By.XPATH, Locators.ENROLL_NAME, Errors_labels.NAME_ERROR_FILL_MAX)
        max_name_length = (By.XPATH, Locators.ENROLL_NAME)
        max_name_length = len(max_name_length)
        errormessagerequired = self.get_text_to_element(By.XPATH, Errors_labels.NAME_ERROR_MAX)
        expected_error_message = "El nombre incluido es muy largo"
        if max_name_length >= 60 or errormessagerequired == expected_error_message:
            print("Character validation failed, max lenght is 60 characters please enter a valid name")
        else:
            print("Character validation ok")




