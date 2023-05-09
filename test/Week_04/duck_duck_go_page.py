class SearchPage:
    SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
    FF_SEARCH_INPUT_TEXT = "ID:searchbox_input']"
    SEARCH_BUTTON = "CSS:.search__button.js-search-button"

    def get_search_text_field(self):
        return self.SEARCH_INPUT_TEXT

    def get_search_button(self):
        return self.SEARCH_BUTTON

    def get_ff_search_test_field(self):
        return self.FF_SEARCH_INPUT_TEXT


class ResultsPage:
    FIRST_RESULT_TITTLE_SPAN = "XPATH://div[@id='links']/child::div[1]//child::div[2]//span"

    def get_result_text(self):
        return self.FIRST_RESULT_TITTLE_SPAN
