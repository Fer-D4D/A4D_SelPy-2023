from selenium import webdriver

#pythondictionarytoset keys and values
caps = {
    'browserName': 'firefox'
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    desired_capabilities=caps
)

driver.quit() #End sessions it's important to clean the code session