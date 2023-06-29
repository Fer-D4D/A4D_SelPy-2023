from Team.Fer.orange_challenge.login_step_by_step.login_ii.framework.common_ii import TinyCore


class TESTDATA:
    TEST_URL = "https://opensource-demo.orangehrmlive.com/"


lets_automate = TinyCore()
lets_automate.init_web_driver("firefox")
lets_automate.launch_site(TESTDATA.TEST_URL)
lets_automate.tear_down()
