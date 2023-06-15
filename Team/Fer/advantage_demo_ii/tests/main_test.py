import time

from Team.Fer.advantage_demo.pages.create_account_page import CreateAccountPage
from Team.Fer.advantage_demo.pages.home_page import HomePage
from Team.Fer.advantage_demo.pages.my_account_page import MyAccountPage
from Team.Fer.advantage_demo.pages.speakers_page import SpeakersPage


class Setup:
    TEST_URL = "http://advantageonlineshopping.com/"
    BROWSER = "chrome"
    VIEWER_MODE = "OFF"  # Turning this ON add a small pause in between each test step
    VERBOSE_MODE = "OFF"  # By turning this ON you will get some useful information about the test run
    HIGHLIGHT_MODE = "OFF"  # Turning this ON will highlight the element being used


home_page = HomePage(Setup.BROWSER,
                     Setup.VIEWER_MODE,
                     Setup.VERBOSE_MODE,
                     Setup.HIGHLIGHT_MODE)

test_driver = home_page.launch_site(Setup.TEST_URL)

create_account_page = CreateAccountPage(test_driver,
                                        Setup.VIEWER_MODE,
                                        Setup.VERBOSE_MODE,
                                        Setup.HIGHLIGHT_MODE)

my_account_page = MyAccountPage(test_driver,
                                Setup.VIEWER_MODE,
                                Setup.VERBOSE_MODE,
                                Setup.HIGHLIGHT_MODE)

speakers_page = SpeakersPage(test_driver,
                             Setup.VIEWER_MODE,
                             Setup.VERBOSE_MODE,
                             Setup.HIGHLIGHT_MODE)

# home_page.do_login()
#
# print(f"Test login invalid credentials: {not home_page.check_login_attempt_result()}")
#
# home_page.start_new_account_creation()
# create_account_page.fill_form_generic_values()
# create_account_page.proceed_and_register_account()
#
# print(f"Test create new account with already registered username: "
#       f"{create_account_page.check_create_account_attempt_result()}")

# home_page.fill_login_popup_form("DonFer", "AAbb77")
# home_page.proceed_to_login()
#
# print(f"Test login valid credentials: {home_page.check_login_attempt_result('DonFer')}")

# home_page.select_user_menu_option("My account")
#
# my_account_page.do_delete_account("No")
time.sleep(8)
home_page.use_top_menu_option("OUR PRODUCTS")
home_page.go_to_product_category("SPEAKERS")

speakers_page.expand_filter_by_visible_text("PRICE")
speakers_page.set_price_filter()
time.sleep(8)
