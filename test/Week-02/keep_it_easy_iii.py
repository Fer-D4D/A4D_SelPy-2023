from core.Common import Common, waste_some_time

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "edge"

# Test Elements
CSS_SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.searchbox_searchButton__F5Bwq.iconButton_button__6x_9C"
HONK_MENU_ICON = "CSS:span.ddgsi.ddgsi-horn"
HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] img"
EXPAND_DESCRIPTION_BUTTON = "CSS:#faq-btn-8"
LEARN_MORE_LINK = "CSS:#faq-btn-8 a"




# Test Actions
letsAutomate = Common(BROWSER, True)

letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)

letsAutomate.do_click(HONK_MENU_ICON)
letsAutomate.do_click(HONK_MENU_TWITTER_ICON)



