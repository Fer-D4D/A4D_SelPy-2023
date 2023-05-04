from core.Common_II import TinyCore

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "firefox"
VIEWER_MODE = "ON"
VERBOSE_MODE = "ON"
HIGHLIGHT_MODE = "ON"

# Test Elements
SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"

# Test Actions
# First use below line to initialize our super framework
letsAutomate = TinyCore(BROWSER, VIEWER_MODE, VERBOSE_MODE, HIGHLIGHT_MODE)
letsAutomate.launch_site(TEST_URL, SEARCH_INPUT_TEXT)

letsAutomate.fill_input_text(SEARCH_INPUT_TEXT, "HEll-o")
letsAutomate.do_click(SEARCH_BUTTON)
