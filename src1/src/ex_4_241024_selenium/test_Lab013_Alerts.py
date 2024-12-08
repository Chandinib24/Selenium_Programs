import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

@allure.description("verify alerts")
@allure.title("Alerts")
def test_alerts():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    #element_prompt=driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_confirm=driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    #element_prompt.click()
    element_confirm.click()

    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    #alert.accept()
    alert.dismiss()

    result_text=driver.find_element(By.ID,"result").text

    #assert result_text=="You successfully clicked an alert"
    assert result_text=="You clicked: Cancel"

    time.sleep(5)

def test_alerts_Prompt():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_jsprompt=driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_jsprompt.click()


    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.send_keys("Chandini")
    alert.accept()
    #alert.dismiss()

    result_text=driver.find_element(By.ID,"result").text

    #assert result_text=="You successfully clicked an alert"
    assert result_text=="You entered: Chandini"

    time.sleep(5)



