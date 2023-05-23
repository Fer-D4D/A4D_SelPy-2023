from Team.Fer.core.Common_II import TinyCore


class Selectors:
    VIDEO_TITLE_LINKS = "XPATH://div[@id='title']/H1"


class TestData:
    VIDEO_DESCRIPTION = "Python for Beginners - Learn Python in 1 Hour"


class VideoPage(TinyCore):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def check_page(self):
        self.wait_for_page_safe_load(Selectors.VIDEO_TITLE_LINKS)
