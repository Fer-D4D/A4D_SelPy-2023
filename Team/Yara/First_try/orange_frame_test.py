import time
from asyncio import wait

from Team.Yara.First_try.orange import TinyCore

lets_automate = TinyCore()


print(lets_automate.browsers())


lets_automate.set_page()

time.sleep(5)

class_login = ".oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"

lets_automate.login_first_try(class_login)
print(test)