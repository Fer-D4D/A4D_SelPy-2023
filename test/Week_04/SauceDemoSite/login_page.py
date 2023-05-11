from core.Common_II import TinyCore


class LoginPage:
    driver = None

    __selectors_dic = {"User Name": "ID:user-name",
                       "Password": "ID:password",
                       "Login Button": "ID:login-button"}

    def __init__(self, driver):
        self.driver = driver

    def get_selector(self, desired_selector):
        return self.__selectors_dic[desired_selector]

    def do_login(self, viewer_mode="Viewer-Mode-OFF"):
        local = TinyCore()
        local.set_driver(self.driver)
        local.set_viewer_mode(viewer_mode)
        local.fill_input_text(self.get_selector("User Name"), "standard_user")
        local.fill_input_text(self.get_selector("Password"), "secret_sauce")
        local.do_click(self.get_selector("Login Button"))
