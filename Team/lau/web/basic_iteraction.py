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

    #OTHER ITERATION
    # other iteration with the browser driver.back(), driver.forward(),driver.refresh()
    ## get the html source as a string source= driver.page_source
    ### execute javascript in the context od the page and get the result
    ### res = driver.execute_script('return 2+2;')
    #### screenshot driver.save_screenshot('evidence.png')

    #WINDOWS,FRAMES AND ALERT
    #windows has his own id, it shows the list of strings for all the windows
    # name_list = driver.windows_handles
    ## switch to a given window by its handle driver.switch_to.window(handle)
    ### get the handle of the currently active window handle= driver.current_window_handle
    #### Maximize and minimize driver.maximize_window() or driver.minimize_window()
    ##### get windows size driver.get_window_rect()
    ###### set windows size driver.set_window_rect(x=50, y=50, height=100, width=200)
    #FRAME AND IFRAMES : PAGE IN THE MIDLE OF WEB PAGE WE USUALLY USE IFRAMES
    #driver.switch_to.frame(frame)  name of frame, number,
    ## driver.switch_to.parent_frame()  or driver.switch_to.default_content()
    #ALERTS
    #alert = driver.switch_to.alert
    ## acept alert alert.accept() to dissmiss the not accept option alert.dismiss()
    ### text displayed in the alert text=alert.text
    #### send keysstrokes alert.send_keys('name key')