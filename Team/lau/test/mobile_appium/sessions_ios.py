from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__)) #variable to the field incounter
APP = path.join(CUR_DIR, 'TheApp.app.zip') #get actual path
APPIUM = 'http://localhost:4723' #location url to research the service
#define capabilities

CAPS = {
    'platformName':'IOS',
    'platformVersion':'13.6',
    'deviceName':'iPhone 14 PRO',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

driver.quit()


