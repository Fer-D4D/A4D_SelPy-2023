from selenium.webdriver import ActionChains

from Team.Fer.core.Common_II import TinyCore, waste_some_time


class Selectors:
    PAGE_TITLE = "XPATH://h3[text()[contains(.,'%$%')]]"
    GENERIC_FILTER_BY_VISIBLE_TEXT_LOCATOR = "XPATH://h4[text()[contains(.,'%$%')]]"
    PRICE_LEFT_SLIDER_BUTTON = "CSS:.noUi-handle.noUi-handle-lower"
    PRICE_RIGHT_SLIDER_BUTTON = "CSS:.noUi-handle.noUi-handle-upper"


class TestData:
    PAGE_TITLE = "SPEAKERS"


class SpeakersPage(TinyCore):
    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__()
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def expand_filter_by_visible_text(self, filter_name):
        self.wait_for_page_safe_load(self.token_replace(Selectors.PAGE_TITLE, TestData.PAGE_TITLE))
        if self.get_number_of_elements(
                Selectors.GENERIC_FILTER_BY_VISIBLE_TEXT_LOCATOR.replace("%$%", filter_name)) > 0:
            self.do_click(Selectors.GENERIC_FILTER_BY_VISIBLE_TEXT_LOCATOR.replace("%$%", filter_name))

    def set_price_filter(self):
        left_element = self.get_element(Selectors.PRICE_LEFT_SLIDER_BUTTON)
        right_element = self.get_element(Selectors.PRICE_RIGHT_SLIDER_BUTTON)
        left_xy = left_element.location
        right_xy = right_element.location
        print(left_xy)
        print(right_xy)
        action = ActionChains(self.DRIVER)
        print(left_xy["x"])
        print(left_element.location)
        action.click_and_hold(on_element=right_element)
        action.perform()
