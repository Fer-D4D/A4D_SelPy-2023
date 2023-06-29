from Team.Fer.orange_challenge.login_step_by_step.login_iv_a.framework.utils import Utils, Using


class TinyCore(Utils):
    MAIN_DRIVER = None

    def init_web_driver(self, browser=Using.Chrome):
        self.MAIN_DRIVER = self.define_webdriver(browser)

    def get_web_driver(self):
        return self.MAIN_DRIVER

    def launch_site(self, target_url):
        self.MAIN_DRIVER.get(target_url)
        self.MAIN_DRIVER.maximize_window()

    def tear_down(self):
        self.snore(2)
        self.MAIN_DRIVER.quit()
