#Create Selenium Script


#Find and Click on the Make Appointment button
#Verify the URL
#On the Next Page
#Find and Enter the details of the username and password ( web_element.send_keys()
#Click on the Submit button (click()
#Verify the URL change.

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
@allure.description("verify to book an appointment on herokuapp ")
@allure.title("Verify the current URL")
def test_task17():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    username_web_element=driver.find_element(By.NAME,"username")
    username_web_element.send_keys("John Doe")
    password_web_element=driver.find_element(By.ID,"txt-password")
    password_web_element.send_keys("ThisIsNotAPassword")
    login_button_element=driver.find_element(By.ID,"btn-login")
    login_button_element.click()
    assert driver.current_url

    time.sleep(10)





