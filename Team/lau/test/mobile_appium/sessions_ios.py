from appium import webdriver
from os import path
CUR_DIR = path.dirname(path.abspath(__file__)) # variable to the field encounter
APP = path.join(CUR_DIR, 'TheApp.app.zip') # get actual path
APPIUM = 'http://127.0.0.1:4723/' # location URL to reach the service
# define capabilities
CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=None
)
driver.quit()


