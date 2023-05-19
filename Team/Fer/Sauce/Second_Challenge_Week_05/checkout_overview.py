from Team.Fer.Sauce.Second_Challenge_Week_05.landing_page import LandingPage


class Selectors:
    ITEM_PRICE = "CSS:.inventory_item_price"
    TAX = "CSS:.summary_tax_label"
    ITEM_TOTAL = "CSS:.summary_subtotal_label"
    TOTAL_LABEL = "CSS:.summary_info_label.summary_total_label"
    FINISH_BUTTON = "ID:finish"


class CheckoutOverview(LandingPage):

    def __init__(self, driver, viewer_mode="Viewer-Mode-OFF", verbose_mode="Verbose-Mode-OFF",
                 highlight_mode="Highlight-Mode-OFF"):
        super().__init__(driver)
        self.set_driver(driver)
        self.set_viewer_mode(viewer_mode)
        self.set_verbose_mode(verbose_mode)
        self.set_highlight_mode(highlight_mode)

    def get_item_totals_without_tax(self):
        totals = 0.0
        for price in self.get_elements_list(Selectors.ITEM_PRICE):
            totals = totals + float(price.text.replace("$", ""))
        return totals

    def check_totals(self):
        return round(self.get_item_totals_without_tax() + float(
            self.get_element_inner_text(Selectors.TAX).replace("Tax: $", "")), 2) == float(
            self.get_element_inner_text(Selectors.TOTAL_LABEL).replace("Total: $", ""))

    def place_order(self):
        if self.safe_to_proceed(Selectors.FINISH_BUTTON):
            self.do_click(Selectors.FINISH_BUTTON)
