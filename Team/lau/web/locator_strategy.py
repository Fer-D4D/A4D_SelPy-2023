#foundelement=locatorstrategy + selector
#Locatorstragtegies: By.css_selector(#loginField, .ad-wrapper, .ad-wrapper ul > li)
# By.tag_name (a, input, button, ul)
# By.Link_text (click me)
# By.partial_link_text (me)
# and By.xpath ( //a[contains(@href,"site.com")] or //div[@class="menu"]/ul/li[3]
#selectors: Strings
# it's better to use css
from selenium.webdriver.common.by import By

login_button = driver.find_element(By.CSS_SELECTOR, '#loginField') # to find one element
#if the element is not founded, it will raise an exception called No.suchElmentException
login_button = driver.find_elements(By.CSS_SELECTOR, '#loginField') # to find more than one element and return a list of elements
#if the element is not founded, it will show an empty list

#to search an locator from the inspector go to console and write document.querySelector('#username')

#WAITING STRATEGIES
#STATICWAIT: time.sleep(x)
#IMPLICIT: timeout, retry, driver.implicity_wait(10)
#Recommended EXPLICIT: expected condition, selenium.webdriver.support.wait.WebDriverWait
#class called WebDriver wait imported from selenium.webdriver.support.wait
#after imported the class you can call method until() and set a condition
#export Expected condition from selenium.webdriver.support.expected_conditions
#ejemplos: expected_condition.title_is('some title'), expected_condition.url_to_be('https//copa.com'),
#expected_condition.presence_of_element_located((By.CSS_SELECTOR, '#login'))
