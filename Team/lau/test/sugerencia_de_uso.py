from selenium.webdriver.common.by import By

from Team.lau.test.sauce_updated_class import Laura

# Locators section
SEARCH_USERNAME_TEXT = "#user-name"

my_class = Laura()

mi_driver = my_class.setup_driver()
my_class.launch_site(mi_driver, "https://www.saucedemo.com/")

my_class.fill_text_to_element(mi_driver, By.CSS_SELECTOR, SEARCH_USERNAME_TEXT, "Fer")

my_class.delay_time(2)
