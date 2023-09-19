from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    form_locator_auto = By.XPATH, '//a[contains(@href,"login")]'
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')
    #driver.find_element(By.XPATH, '//a[contains(@href,"login")]') find element is not needed when use expected conditions
    #wait.until(EC.presence_of_element_located(By.XPATH, '//a[contains(@href,"login")]')) it only accept 1 value need to rename
    #wait.until(EC.presence_of_element_located(By.LINK_TEXT, 'Form Authentication')) it only accept 1 value need to rename
    wait.until(EC.presence_of_element_located(form_locator_auto))
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
    #els = driver.find_element(By.TAG_NAME, 'a')
    #print(f'There were {len(els)} a elements')
finally:
    driver.quit()