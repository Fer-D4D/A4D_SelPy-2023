from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "chrome"

# Test Elements
CSS_SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
SEARCH_BUTTON = "CSS:.search__button.js-search-button"
CHROME_SEARCH_BUTTON = "CSS:button[type='submit']"
EDGE_HONK_MENU_ICON = "CSS:span.ddgsi.ddgsi-horn"
CHROME_HONK_MENU_ICON = "CSS:.legacy-homepage_socialIcons__obCva.social-menu_button__2_gkB"
HONK_MENU_ICON_BAD = "CSS:span.ddgsi.ddgsi-horm["
EDGE_HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] img"
CHROME_HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] svg"
EXPAND_DESCRIPTION_BUTTON = "CSS:#faq-btn-8"
CHROME_EXPAND_DESCRIPTION_BUTTON = "CSS:.legacy-homepage_legacyButton__oUMB9.legacy-homepage_faqButton__maJxW span"
LEARN_MORE_LINK = "CSS:#faq-answer-8 a"
CHROME_LEARN_MORE_LINK = "CSS:a[href='https://spreadprivacy.com/how-does-the-duckduckgo-app-extension-protect-my" \
                         "-privacy/'] "

# Test Actions
letsAutomate = Common(BROWSER, True)

letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)

# letsAutomate.do_click(HONK_MENU_ICON)
letsAutomate.do_click_from_options([EDGE_HONK_MENU_ICON, HONK_MENU_ICON_BAD, CHROME_HONK_MENU_ICON])
letsAutomate.do_click_from_options([EDGE_HONK_MENU_TWITTER_ICON, CHROME_HONK_MENU_TWITTER_ICON])
letsAutomate.page_back()

letsAutomate.do_click_by_text(CHROME_EXPAND_DESCRIPTION_BUTTON, "How does the DuckDuckGo app & extension work?")
letsAutomate.do_click_from_options([LEARN_MORE_LINK, CHROME_LEARN_MORE_LINK])
letsAutomate.switch_browser_tab()

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "CSS Selector")
letsAutomate.do_click_from_options([SEARCH_BUTTON, CHROME_SEARCH_BUTTON])
letsAutomate.page_back()
