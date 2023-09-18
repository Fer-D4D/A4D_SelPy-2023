#statring sessions
from selenium import webdriver

driver = webdriver.Firefox()
#webdriver.Chrome()
#webdriver.Safari()
#webdriver.Edge()
#options = webdriver.EdgeOptions()
#options.use_chromium = True
#driver=webdriver.Edge(options=options)
driver.quit()