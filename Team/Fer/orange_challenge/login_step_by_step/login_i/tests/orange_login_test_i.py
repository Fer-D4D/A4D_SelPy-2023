from Team.Fer.orange_challenge.login_step_by_step.login_i.framework.common_i import TinyCore


class TESTDATA:
    TEST_URL = "https://opensource-demo.orangehrmlive.com/"


lets_automate = TinyCore()
lets_automate.init_web_driver("firefox")
lets_automate.launch_site(TESTDATA.TEST_URL)

