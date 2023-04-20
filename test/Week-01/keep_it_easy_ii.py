from core.Common import Common, waste_some_time

# Test Data
TEST_URL = "http://advantageonlineshopping.com/"
BROWSER = "chrome"

# Test Elements
SPECIAL_OFFER_MENU = "XPATH://a[contains(text(),'SPECIAL OFFER')]"
CONTACT_US_MENU = "LINK_TEXT:CONTACT US"
CONTACT_US_MAIN_SELECT = "NAME:categoryListboxContactUs"
CONTACT_US_SUB_SELECT = "NAME:productListboxContactUs"

# Test Actions
letsAutomate = Common(BROWSER)
letsAutomate.launch_site(TEST_URL, SPECIAL_OFFER_MENU)
waste_some_time(2)
letsAutomate.do_click(CONTACT_US_MENU)
waste_some_time(2)
letsAutomate.select_dropdown_option(CONTACT_US_MAIN_SELECT, "Mice")
letsAutomate.select_dropdown_option(CONTACT_US_SUB_SELECT, "Kensington Orbit 72337 Trackball with Scroll Ring")
waste_some_time(2)

