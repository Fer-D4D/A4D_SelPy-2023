from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get('https://copacom-qa.copa.s4n.co/es-gs/')
finally:
    driver.quit()