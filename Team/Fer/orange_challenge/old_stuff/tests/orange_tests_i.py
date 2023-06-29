from Team.Fer.core.common_iv import TinyCore
from Team.Fer.orange_challenge.old_stuff.pages import LoginPage


class TESTDATA:
    TEST_URL = "https://opensource-demo.orangehrmlive.com/"


lets_automate = TinyCore()
lets_automate.init_web_driver()

lets_automate.launch_site(TESTDATA.TEST_URL)

login_page = LoginPage(lets_automate.MAIN_DRIVER)

home_page = login_page.do_simple_login()

admin_page = home_page.execute_left_menu_option("Admin")

admin_page.search_user()
#admin_page.search_user_autocomplete()
#admin_page.select_record_from_found_table()

