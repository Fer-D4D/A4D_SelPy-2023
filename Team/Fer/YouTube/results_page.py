from Team.Fer.core.Common_II import TinyCore


class Selectors:
    VIDEO_TITLE_LINKS = "XPATH://a[@id='video-title']"
    FILTERS_BUTTON = "CSS:.yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono" \
                     ".yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape" \
                     "-next--align-by-text "


class TestData:
    VIDEO_DESCRIPTION = "Python for Beginners - Learn Python in 1 Hour"


class ResultsPage(TinyCore):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def check_results(self):
        self.wait_for_page_safe_load(Selectors.FILTERS_BUTTON)

    def proceed_to_target_video(self):
        video_links = self.get_elements_list(Selectors.VIDEO_TITLE_LINKS)
        for video_link in video_links:
            if video_link.text.lower() == TestData.VIDEO_DESCRIPTION.lower():
                video_link.click()
