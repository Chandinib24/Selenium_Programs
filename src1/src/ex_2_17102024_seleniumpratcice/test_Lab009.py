import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

@allure.description("verify that user is navigated to free trial page")
@allure.title("sign up button verification")
def test_negative_Project3():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
     #find te element anchor tag
    anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element.click()
    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    ignore_list=[ElementNotVisibleException,ElementNotSelectableException]
    ((WebDriverWait(driver=driver,poll_frequency=1,timeout=5,ignored_exceptions=ignore_list))
     .until(EC.visibility_of_element_located(By.CLASS_NAME,"notification-box-description")))

    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()


    time.sleep(3)
    driver.quit()

