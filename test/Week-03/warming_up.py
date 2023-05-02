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
letsAutomate = Common(BROWSER)  # hey brainy why don't you change that True for a word that makes more sense.
letsAutomate.launch_site(TEST_URL, CSS_SEARCH_INPUT_TEXT)

# Imagine you need to perform three searches instead of one, then maybe you try something like this:

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "First Search")
letsAutomate.do_click(CHROME_SEARCH_BUTTON)
letsAutomate.page_back()

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "Second Search")
letsAutomate.do_click(CHROME_SEARCH_BUTTON)
letsAutomate.page_back()

letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, "Third Search")
letsAutomate.do_click(CHROME_SEARCH_BUTTON)
letsAutomate.page_back()


# That kinda worked, right? but imagine that you need to do 100 searches! Well it is time to warm up

def do_search(text_to_search):
    letsAutomate.fill_input_text(CSS_SEARCH_INPUT_TEXT, text_to_search)
    letsAutomate.do_click(CHROME_SEARCH_BUTTON)
    letsAutomate.page_back()


# Now you can repeat previous 3 searches using three lines instead of 9, let's see that in action

do_search("First Search")
do_search("Second Search")
do_search("Third Search")


# Good improvement but still a lot of work using above approach for our 100 searches, right?
# lest warm up again

def do_searches(list_of_texts_to_search):
    for text_to_search in list_of_texts_to_search:
        do_search(text_to_search)


# Let's see how to do our three searches in a single line

do_searches(["First Second", "Second Search", "Third Search"])

# Impressed? no? wait I know what the heck is that weird angular parenthesis? Python is cool, and let us
# create a list just list this:

my_list_of_texts_to_search = ["Why", "Learning", "backwards", "it is", "so cool", "etc..."]

# so, now you can use your list in our do_searches test action.

do_searches(my_list_of_texts_to_search)
