from Team.Fer.orange_challenge.login_step_by_step.login_iv_a.framework.common_iv import TinyCore
from Team.Fer.orange_challenge.login_step_by_step.login_iv_a.pages.login_page import LoginPage


class TESTDATA:
    TEST_URL = "https://opensource-demo.orangehrmlive.com/"


lets_automate = TinyCore()
lets_automate.init_web_driver()
lets_automate.launch_site(TESTDATA.TEST_URL)

WORKING_DRIVER = lets_automate.get_web_driver()
WORKING_DRIVER.implicitly_wait(4)

login_page = LoginPage(WORKING_DRIVER)
login_page.do_login()

lets_automate.tear_down()
