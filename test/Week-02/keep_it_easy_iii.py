from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "chrome"

# Test Elements
CSS_SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"
HONK_MENU_ICON = "CSS:span.ddgsi.ddgsi-horn"
HONK_MENU_ICON_BAD = "CSS:span.ddgsi.ddgsi-horm"
HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] img"
EXPAND_DESCRIPTION_BUTTON = "CSS:#faq-btn-8"
LEARN_MORE_LINK = "CSS:#faq-answer-8 a"

# Test Actions
letsAutomate = Common(BROWSER, True)

letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)

# letsAutomate.do_click(HONK_MENU_ICON)
letsAutomate.do_click_from_options([HONK_MENU_ICON_BAD, HONK_MENU_ICON])
letsAutomate.do_click(HONK_MENU_TWITTER_ICON)
letsAutomate.page_back()

letsAutomate.do_click(EXPAND_DESCRIPTION_BUTTON)
letsAutomate.do_click(LEARN_MORE_LINK)
letsAutomate.switch_browser_tab()

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "CSS Selector")
letsAutomate.do_click(SEARCH_BUTTON)
letsAutomate.page_back()
