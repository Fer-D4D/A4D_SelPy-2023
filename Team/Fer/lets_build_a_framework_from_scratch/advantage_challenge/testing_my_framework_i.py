from Team.Fer.core.common_iv import TinyCore
from Team.Fer.lets_build_a_framework_from_scratch.advantage_challenge.pages.home_page import HomePage

TEST_URL = "http://advantageonlineshopping.com/"
for i in range(3):
    hey_fer_lets_automate = TinyCore()

    hey_fer_lets_automate.init_web_driver()
    hey_fer_lets_automate.launch_site(TEST_URL)

    home_page = HomePage(hey_fer_lets_automate.get_web_driver())
    create_account_page = home_page.go_create_new_account_page()

    hey_fer_lets_automate.tear_down()



