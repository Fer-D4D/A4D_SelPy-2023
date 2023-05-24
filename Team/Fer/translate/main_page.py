from Team.Fer.core.Common_II import TinyCore


class Selectors:
    TRANSLATE_FIELD = "XPATH://textarea"
    SEARCH_LENS_BUTTON = "ID:search-icon-legacy"
    TRANSLATION_SPAN = "XPATH://span[@class='ryNqvb']"



class TestData:
    DEFAULT_TEXT = "Python para principiantes"
    TEST_URL = "https://translate.google.com/"


class MainPage(TinyCore):

    def __init__(self, browser='chrome', viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_browser(browser)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)
        self.launch_site(TestData.TEST_URL, Selectors.TRANSLATE_FIELD)

    def fill_translate_form(self, translate_term=TestData.DEFAULT_TEXT):
        self.fill_input_text(Selectors.TRANSLATE_FIELD, translate_term)

    def check_expected_translation(self):
        pass

