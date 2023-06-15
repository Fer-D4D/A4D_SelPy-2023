from Team.Fer.Sauce.Sauce_Common_iii.Pages.home_page import HomePage
from Team.Fer.Sauce.Sauce_Common_iii.Pages.login_page import LoginPage
from Team.Fer.core.common_iii import TinyCore


class Setup:
    TEST_URL = "https://www.saucedemo.com/"
    BROWSER = "firefox"
    VIEWER_MODE = "OFF"
    VERBOSE_MODE = "OFF"
    HIGHLIGHT_MODE = "OFF"


lets_automate = TinyCore(Setup.TEST_URL,
                         Setup.BROWSER,
                         Setup.VIEWER_MODE,
                         Setup.VERBOSE_MODE,
                         Setup.HIGHLIGHT_MODE)

lets_automate.start_driver()

login_page = LoginPage(lets_automate)


print(f"Fill form result -> {login_page.fill_login_form()}")

home_page = HomePage(lets_automate)

print(f"Login attempt result -> {login_page.send_login_request(home_page.get_trusted_selector())}")

print(f"Add Sauce Labs Backpack -> {home_page.add_item_to_shopping_cart('Sauce Labs Backpack')}")

lets_automate.waste_some_time(2)

