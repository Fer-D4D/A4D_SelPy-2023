from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

time.sleep(2)

driver.find_element(By.ID, "login-button").click()

time.sleep(3)

driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.LINK_TEXT, "Logout").click()

time.sleep(2)

driver.close()
driver.quit()
print("Test Completed!")





