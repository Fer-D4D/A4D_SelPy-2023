import time
from asyncio import wait

from Team.Yara.First_try.orange import TinyCore

lets_automate = TinyCore()
ADMIN_USER = "Admin"
ADMIN_PASS = "admin123"
locator_user = "username"
locator_pass = "password"
locator_login = "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"



print(lets_automate.browsers())



lets_automate.set_page()

time.sleep(5)

class_login = "Username"

lets_automate.login_success(locator_user,ADMIN_USER,locator_pass,ADMIN_PASS,locator_login)
time.sleep(10)
print("test")
