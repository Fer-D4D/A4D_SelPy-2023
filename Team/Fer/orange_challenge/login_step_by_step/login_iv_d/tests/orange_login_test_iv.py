from Team.Fer.orange_challenge.login_step_by_step.login_iv_d.framework.common_iv import TinyCore
from Team.Fer.orange_challenge.login_step_by_step.login_iv_d.pages.login_page import LoginPage


class TESTDATA:
    TEST_URL = "https://opensource-demo.orangehrmlive.com/"


lets_automate = TinyCore()
lets_automate.init_web_driver()
lets_automate.launch_site(TESTDATA.TEST_URL)

login_page = LoginPage(lets_automate.get_web_driver())
login_page.do_login()

lets_automate.tear_down()
