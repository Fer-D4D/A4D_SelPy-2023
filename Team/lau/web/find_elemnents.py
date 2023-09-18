from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element(By.XPATH,'//a[contains(@href,"login")]')
    els =driver.find_element(By.TAG_NAME, 'a')
    print(f'There were {len(els)} a elements')
    els = driver.find_element(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} foo elements')
finally:
    driver.quit()
