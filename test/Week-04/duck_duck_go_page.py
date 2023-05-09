class SearchPage:
    SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
    FF_SEARCH_INPUT_TEXT = "ID:searchbox_input']"
    SEARCH_BUTTON = "CSS:.search__button.js-search-button"

    def get_search_text_field(self):
        return [self.SEARCH_INPUT_TEXT,
                self.FF_SEARCH_INPUT_TEXT]
