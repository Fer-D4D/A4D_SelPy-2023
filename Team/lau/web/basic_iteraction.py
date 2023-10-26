from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
    form_auto = driver.find_element(By.XPATH, '//a[contains(@href,"login")]') ## or By.LINK_TEXT, 'Form Authentication'
    form_auto.click()  #or tap in a element on mobile devices
    title_page = driver.find_element(By.TAG_NAME, 'h2').text
    print(f'There were {title_page} element')
    form_username = driver.find_element(By.ID, 'username')
    form_password = driver.find_element(By.CSS_SELECTOR, '#password')
    form_username.send_keys('Laura')
    form_password.send_keys('Password')
    form_password.clear()
    form_password.send_keys('New password')


finally:
    driver.quit()