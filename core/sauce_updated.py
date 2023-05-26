from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

mi_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def delay_time(waiting_time_value):
    time.sleep(waiting_time_value)
    print(f"Waited for {waiting_time_value} seconds. Continuing with additional actions.")