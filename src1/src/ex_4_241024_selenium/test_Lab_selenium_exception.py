import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
@allure.description("verify exception")
@allure.title("exception handling")
def test_select():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    try:
        element=driver.find_element(By.ID, "This id doesn't exist")
    except NoSuchElementException as nse:
        print(nse.msg)

        time.sleep(5)

