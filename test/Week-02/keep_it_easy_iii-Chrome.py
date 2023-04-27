from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "chrome"

# Test Elements
CSS_SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
CHROME_SEARCH_BUTTON = "CSS:button[type='submit']"
CHROME_HONK_MENU_ICON = "CSS:.legacy-homepage_socialIcons__obCva.social-menu_button__2_gkB"
CHROME_HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] svg"
CHROME_EXPAND_DESCRIPTION_BUTTON = "CSS:#__next > main > article > section.legacy-homepage_faqSection__464Rq > div.legacy-homepage_faqSectionBody__qmHgT > div > section:nth-child(9) > div > div > p > a"
CHROME_LEARN_MORE_LINK = "CSS:a[href='https://spreadprivacy.com/how-does-the-duckduckgo-app-extension-protect-my" \
                         "-privacy/'] "

# Test Actions
letsAutomate = Common(BROWSER, True)

letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)

letsAutomate.do_click(CHROME_HONK_MENU_ICON)
letsAutomate.do_click(CHROME_HONK_MENU_TWITTER_ICON)
letsAutomate.page_back()

letsAutomate.do_click(CHROME_EXPAND_DESCRIPTION_BUTTON)
letsAutomate.do_click(CHROME_LEARN_MORE_LINK)
letsAutomate.switch_browser_tab()

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "CSS Selector")
letsAutomate.do_click(CHROME_SEARCH_BUTTON)
letsAutomate.page_back()

