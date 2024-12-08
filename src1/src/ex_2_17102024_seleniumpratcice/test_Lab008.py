import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.Negative
@allure.title("Negative test case for app.vw.com for wrong email/pass")
@allure.description("verify that if email/pass is wrong we will get error message")
def test_negative_Project2():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")



     #find te element anchor tag
    email_web_element=driver.find_element(By.ID,"login_username")
    email_web_element.send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.NAME, "password")
    email_web_element.send_keys("Password@123")
    submit_button_element=driver.find_element(By.ID,"js-login-btn")
    submit_button_element.click()
    time.sleep(3)
    WebDriverWait(driver=driver,timeout=5) .until(EC.visibility_of_element_located
                 (By.CLASS_NAME, "notification-box-description"))

    error_message_web_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element)
    assert error_message_web_element.text=="Your email, password, IP address or location did not match"


    time.sleep(3)
    driver.quit()

