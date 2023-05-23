from core.Common import Common, waste_some_time

# Test data
TEST_URL = "https://duckduckgo.com/?t=h_"
BROWSER = "chrome"
INPUT_TEXT1 = "EPAM"

# Test Elements
SEARCH_FORM = "CSS:.js-search-input.search__input--adv"
SEARCH_BOX = "CSS:#search_form_input_homepage"
SEARCH_BUTTON = "CSS:#search_button_homepage"
CSS_SEARCH_BUTTON = "CSS:input[type='submit']"
DROPDOWN_MENU = "CSS:.header__button--menu.js-side-menu-open"
DROPDOWN_INPUT_MENU = "CSS:a[href='#']"
SECTION_NAV = "CSS:.header--aside.js-header-aside"
NAV_MENU = "CSS:.nav-menu__list"
MODULE_TITLE = "CSS:.module__title"
MODULE_STOCK = "CSS:.stocks-module__currentPrice"
BACK_HOME = "CSS:.header__logo.js-logo-ddg"
MENU_ITEM1 = "CSS:span[class='ddgsi ddgsi-horn']"
MENU_LIST1 = "CSS:a[href='https://twitter.com/duckduckgo'] > img"

# Test Actions

letsAutomate = Common(BROWSER)
letsAutomate.launch_site(TEST_URL, SEARCH_BOX)
letsAutomate.fill_input_text(SEARCH_FORM, INPUT_TEXT1)
letsAutomate.do_click(CSS_SEARCH_BUTTON)
print(letsAutomate.get_text_from_element(MODULE_TITLE))
print(letsAutomate.get_text_from_element(MODULE_STOCK))
letsAutomate.do_click(BACK_HOME)
waste_some_time(2)
letsAutomate.do_click(MENU_ITEM1)
letsAutomate.do_click(MENU_LIST1)
# hace emulador de regresar a la pagina anterior
letsAutomate.page_back()

#letsAutomate.switch_browser_tab() # cambia de tab
#letsAutomate.do_click_from_options([CCSLOCATOR1, CCSLOCATOR2, CCSLOCATOR3 ]) #compara diferentes selectores
#letsAutomate.do_click_by_text(LOCATORNAME1, "TWITTER") # BUSCA EN UN LOCATOR NO TAN ACCURATE Y BUSCA POR EL TEXTO
