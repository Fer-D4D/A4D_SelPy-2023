from Team.Fer.core.Common_II import TinyCore, waste_some_time


class Selectors:
    ACCOUNT_DETAILS_EDIT_LINK = "XPATH://*[text()[contains(.,'Account details')]]/a"
    PREFERRED_PAYMENT_METHOD_EDIT_LINK = "XPATH://*[text()[contains(.,'Preferred payment method')]]/a"

    NOTIFY_ABOUT_PROMOS_CHECK = "XPATH://*[@name='notify_about_promotions']"

    CATEGORY_TABLETS_CHECK = "XPATH://*[@name='category_tablets']"
    CATEGORY_LAPTOPS_CHECK = "XPATH://*[@name='category_laptops']"
    CATEGORY_HEADPHONES_CHECK = "XPATH://*[@name='category_headphones']"
    CATEGORY_SPEAKERS_CHECK = "XPATH://*[@name='category_speakers']"
    CATEGORY_MICE_CHECK = "XPATH://*[@name='category_mice']"

    DELETE_ACCOUNT_BUTTON = "CSS:.deleteMainBtnContainer.a-button.ng-scope"
    POPUP_DELETE_ACCOUNT_YES_BUTTON = "CSS:.deletePopupBtn.deleteRed"
    POPUP_DELETE_ACCOUNT_NO_BUTTON = "CSS:.deletePopupBtn.deleteGreen"
    POPUP_DELETE_ACCOUNT_CLOSE_BUTTON = "XPATH://div[@id='deleteAccountPopup']/div[@class='closeBtn " \
                                        "loginPopUpCloseBtn'] "


class TestData:
    pass


class MyAccountPage(TinyCore):
    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def do_delete_account(self, action):
        self.wait_for_page_safe_load(Selectors.DELETE_ACCOUNT_BUTTON)
        self.do_click(Selectors.DELETE_ACCOUNT_BUTTON)
        waste_some_time(.5)
        if action.lower() == "yes":
            self.do_click(Selectors.POPUP_DELETE_ACCOUNT_YES_BUTTON)
        else:
            self.do_click(Selectors.POPUP_DELETE_ACCOUNT_CLOSE_BUTTON)
