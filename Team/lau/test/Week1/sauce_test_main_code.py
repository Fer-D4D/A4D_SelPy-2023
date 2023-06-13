from Team.lau.test.Week1.sauce_test_methods import Page
from Team.lau.test.Week1.sauce_test_Login import Login
from Team.lau.test.Week1.sauce_test_products import AddProducts

# Clases

#my_page = Page()
login = Login()
addproduct = AddProducts(login.get_driver())
# locator = Locators()
# data = Data()

#Driver
login.create_driver()

# Launch site and Login
login.do_login()
login.delay_time(2)

#Add products

addproduct.adding_to_cart()
