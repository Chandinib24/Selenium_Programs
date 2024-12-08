from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_chrome_current_url_verification():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
     #find te element anchor tag
    make_appointment_element=driver.find_element(By.ID,value="btn-make-appointment")
    make_appointment_element.click()




     # we need to find unique attribute which can find the web element
    #click on it
    #find the URL changes
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

   # < a
   # id = "btn-make-appointment"
   # href = "./profile.php#login"

    #class ="btn btn-dark btn-lg" > Make Appointment < / a >