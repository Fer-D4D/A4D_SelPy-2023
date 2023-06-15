import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Function: Validate the functionality to make a purchase on the Sauce site.

Given the user is already registered on the Sauce website.
Given that the user is able to log in to the Sauce site.
Given that the user has added a backpack and a jacket to the shopping cart.
Given that the user checks the contents of his shopping cart.
And the user clicks on the Checkout button
Then the "Checkout: Your information" screen is displayed.
And the user will be able to enter his data
And the user can proceed to the "Checkout: Summary" by clicking on the Continue button
And the user validates that the total of the purchase, taxes included, is correct.
Finally, the user must place the order by clicking the Finish button.
"""

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

mi_driver.get("https://www.copaair.com/es-gs/")
mi_driver.maximize_window()

COPA_CONNECT_MILES_LINK = "//div[@class='MuiBox-root css-4tt2hh']/a/p[text()[contains(.,'ConnectMiles')]]"
time.sleep(5)
mi_driver.find_element(By.XPATH, COPA_CONNECT_MILES_LINK).click()
time.sleep(200)
UNETE_AQUI_BUTTON = "//button[text()[contains(.,'Únete aquí')]]"

mi_driver.find_element(By.XPATH, UNETE_AQUI_BUTTON).click()

FECHA_NACIMIENTO_YEAR = "//*[@id='mui-component-select-birthDate.year']"
FECHA_NACIMIENTO_MONTH = "//*[@id='mui-component-select-birthDate.month']"
FECHA_NACIMIENTO_DAY = "//*[@id='mui-component-select-birthDate.day']"

GENERIC_N_FAKE_LIST_DROPDOWN = "//*[@id='-open']"
time.sleep(1)

mi_driver.find_element(By.XPATH, FECHA_NACIMIENTO_YEAR).click()
mi_driver.find_element(By.XPATH, GENERIC_N_FAKE_LIST_DROPDOWN).send_keys("2018")

time.sleep(70)