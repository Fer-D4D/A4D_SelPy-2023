from Team.Fer.core.Common_II import TinyCore


class Selectors:
    SEARCH_FORM_FIELD = "XPATH://input[@id='search']"
    SEARCH_LENS_BUTTON = "ID:search-icon-legacy"


class TestData:
    VIDEO_DESCRIPTION = "Python for Beginners - Learn Python in 1 Hour"
    TEST_URL = "https://www.youtube.com/"


class MainPage(TinyCore):

    def __init__(self, browser='chrome', viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_browser(browser)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)
        self.launch_site(TestData.TEST_URL, Selectors.SEARCH_FORM_FIELD)

    def do_search(self, search_term=TestData.VIDEO_DESCRIPTION):
        self.fill_search_form()
        self.proceed_to_search()

    def fill_search_form(self, search_term=TestData.VIDEO_DESCRIPTION):
        print("HEY")
        self.fill_input_text(Selectors.SEARCH_FORM_FIELD, search_term)

    def proceed_to_search(self):
        self.do_click(Selectors.SEARCH_LENS_BUTTON)
