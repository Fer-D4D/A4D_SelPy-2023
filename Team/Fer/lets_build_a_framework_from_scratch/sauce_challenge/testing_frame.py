import time

from Team.Fer.lets_build_a_framework_from_scratch.core.new_common import TinyCore

lets_automate = TinyCore()

print(lets_automate.set_chrome_driver())

LOGIN_BUTTON = "//*[@id='login-button']"
USER_NAME_FORM_FIELD = "//*[@id='user-name']"
lets_automate.launch_site("https://www.saucedemo.com/")

lets_automate.force_text_value(USER_NAME_FORM_FIELD, "standard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_user")
time.sleep(2)
lets_automate.force_text_value(USER_NAME_FORM_FIELD, "clear")
time.sleep(2)
lets_automate.type_in_text_field(USER_NAME_FORM_FIELD, "standard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_userstandard_user")
time.sleep(2)
lets_automate.type_in_text_field(USER_NAME_FORM_FIELD, "clear")
time.sleep(2)

lets_automate.launch_site("http://advantageonlineshopping.com/")
SEARCH_BUTTON = "//*[@id='menuSearch']"
SEARCH_BAR = "//*[@id='autoComplete']"
time.sleep(5)
lets_automate.do_click(SEARCH_BUTTON)
time.sleep(2)
lets_automate.type_in_text_field(SEARCH_BAR, "hp c")
time.sleep(2)
lets_automate.type_in_text_field(SEARCH_BAR, "hp e")
time.sleep(2)
lets_automate.force_text_value(SEARCH_BAR, "hp c")
time.sleep(2)
lets_automate.force_text_value(SEARCH_BAR, "hp e")
time.sleep(2)
