from Team.lau.test.Week1.sauce_test_methods import Page
from Team.lau.test.Week1.sauce_test_Login import Login

# Clases

my_page = Page()
login = Login()
# locator = Locators()
# data = Data()

#Driver
#my_page.get_set_driver()

# Launch site and Login
login.do_login()
my_page.delay_time(2)

#Add products


