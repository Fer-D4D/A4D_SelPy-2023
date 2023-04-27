from core.Common import Common

# Test Data
TEST_URL = "http://advantageonlineshopping.com/"
BROWSER = "chrome"

# Test Elements
SPECIAL_OFFER_MENU = "XPATH://a[contains(text(),'SPECIAL OFFER')]"
CONTACT_US_MENU = "LINK_TEXT:CONTACT US"
CONTACT_US_MAIN_SELECT = "NAME:categoryListboxContactUs"
CONTACT_US_SUB_SELECT = "NAME:productListboxContactUs"
LAPTOPS_OPTION = "XPATH://*[contains(text(),'Laptops')]"
# Test Actions
letsAutomate = Common(BROWSER, True)

letsAutomate.launch_site(TEST_URL, SPECIAL_OFFER_MENU)

letsAutomate.do_click(CONTACT_US_MENU)
letsAutomate.fill_input_text(SPECIAL_OFFER_MENU, "ASADASDaads")
letsAutomate.select_dropdown_option(CONTACT_US_MAIN_SELECT, "Mice")
letsAutomate.select_dropdown_option(CONTACT_US_SUB_SELECT, "Kensington Orbit 72337 Trackball with Scroll Ring")
letsAutomate.get_text_from_element(CONTACT_US_MENU)
