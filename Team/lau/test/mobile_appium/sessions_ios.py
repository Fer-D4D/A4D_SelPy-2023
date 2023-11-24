from appium import webdriver
from os import path
from appium.options.ios import XCUITestOptions

CUR_DIR = path.dirname(path.abspath(__file__)) # variable to the field encounter
APP = path.join(CUR_DIR, 'TheApp.app.zip') # get actual path
APPIUM = 'http://localhost:4723/' # location URL to reach the service

# define capabilities
CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': APP
}

capabilities_option = XCUITestOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=capabilities_option
)


#driver = webdriver.Remote(
    #command_executor=APPIUM,
    #options=None)
#driver.quit()


