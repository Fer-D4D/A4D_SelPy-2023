from core.Common import Common

# Test Data
TEST_URL = "https://duckduckgo.com/"
BROWSER = "chrome"

# Test Elements
CSS_SEARCH_INPUT_TEXT = "CSS:input[placeholder='Search the web without being tracked']"
CHROME_SEARCH_BUTTON = "CSS:button[type='submit']"
CHROME_HONK_MENU_ICON = "CSS:.legacy-homepage_socialIcons__obCva.social-menu_button__2_gkB"
CHROME_HONK_MENU_TWITTER_ICON = "CSS:a[href='https://twitter.com/duckduckgo'] svg"
CHROME_EXPAND_DESCRIPTION_BUTTON = "CSS:#__next > main > article > section.legacy-homepage_faqSection__464Rq > " \
                                   "div.legacy-homepage_faqSectionBody__qmHgT > div > section:nth-child(9) > div > " \
                                   "div > p > a "
CHROME_LEARN_MORE_LINK = "CSS:a[href='https://spreadprivacy.com/how-does-the-duckduckgo-app-extension-protect-my" \
                         "-privacy/'] "

# Test Actions
# First use below line to initialize our super framework
letsAutomate = Common(BROWSER, True)
# now we can use it to start playing. Let's start by launching out testing site, using line below
# launch_site function accepts to parameters, but just the URL is mandatory, anchor_locator_definition is optional, but
# we suggest you to use it. This las one is used to ensure that the site is ready and ready to be used.
letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)
# Now that the site is ready to be used, we can start performing actions on it, let me explain below example:
# do_click function does exactly as its name imply, it performs a mouse click over the element we pass as parameter.
letsAutomate.do_click(CHROME_HONK_MENU_ICON)
letsAutomate.do_click(CHROME_HONK_MENU_TWITTER_ICON)
# The page_back function emulates the action of pressing Back button in our browser, we need it because previous step
# do click in a link that load new content in our working browser window/tab. No parameters needed for this one.
letsAutomate.page_back()
# Due to the previous action we are back in our initial testing page, and will do a series of click actions,
letsAutomate.do_click(CHROME_EXPAND_DESCRIPTION_BUTTON)
letsAutomate.do_click(CHROME_LEARN_MORE_LINK)
# The last action open a new tab and move the focus to the new content, so we need a way to go back to our starting
# testing page. The switch_browser_tab do that for us, it closes the new window and get us back to the initial page.
letsAutomate.switch_browser_tab()
# Once again in our initial testing page, we can try other function from our superb framework. The fill_input_text
# function allow us to write some text over elements that have that capability, this function requires two parameters,
# locator_definition and the text we want to write.
letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "CSS Selector")
# The rest of the actions are now known by everybody
letsAutomate.do_click(CHROME_SEARCH_BUTTON)
letsAutomate.page_back()
