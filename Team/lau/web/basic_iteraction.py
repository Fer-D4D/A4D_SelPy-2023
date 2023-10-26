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
    form_password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))

    form_username.send_keys('tomsmith')
    form_password.send_keys('Password')
    form_password.clear()
    form_password.send_keys('SuperSecretPassword!')

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click() #is not neccesary call it as a
    #variable if you're not going to use it too much.
    flash_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#flash')))
    ## flash message a message with a message example after log out "success logout"
    ##Assertion
    assert 'logged into' in flash_login.text


finally:
    driver.quit()