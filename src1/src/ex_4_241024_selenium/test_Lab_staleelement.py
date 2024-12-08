import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
@allure.description("verify exception")
@allure.title("exception handling")
def test_select():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        text_area=driver.find_element(By.NAME, "q")
        driver.refresh()

        text_area.sendkeys("The testing academy")
    except StaleElementReferenceException as see:
        print(see)
        print("stale element reference")

        time.sleep(5)

