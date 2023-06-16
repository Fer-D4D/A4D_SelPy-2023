from Team.lau.test.Week1.sauce_test_Login import Login
from Team.lau.test.Week1.sauce_test_products import AddProducts

# Clases

#my_page = Page()
login = Login()
login.create_driver()
print(login.get_driver())
addproduct = AddProducts(login.get_driver())

#Driver

# Launch site and Login
#login.do_login()

#Validate login
login.validate_login()
login.delay_time(3)
#Add products

addproduct.adding_to_cart()
addproduct.summary_cart()
login.delay_time(3)
addproduct.set_checkout()
login.back_to_page()