from appium import webdriver
from os import path
from appium.options.ios import XCUITestOptions

CUR_DIR = path.dirname(path.abspath(__file__)) # variable to the field encounter
APP = path.join(CUR_DIR, 'TheApp.app.zip') # get actual path
APPIUM = 'http://localhost:4723/' # location URL to reach the service

# define capabilities
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "automationName": "XCUITest",
        "platformVersion": "16.0",
        "app": APP,
        "deviceName": "iPhone 12",
        "noReset": True
    }
}
driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

driver.quit()


