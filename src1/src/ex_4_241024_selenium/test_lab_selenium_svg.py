import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
@allure.description("verify svg")
@allure.title("svg")
def test_select():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("macmini")

    list_svg_elements=driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_svg_elements[0].click()

    time.sleep(5)

