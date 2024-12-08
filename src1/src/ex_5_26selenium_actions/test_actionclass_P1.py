from selenium.webdriver.common.by import By
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("Actions PA")
@allure.description("Verify actions P1")
def test_verify_action():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name= driver.find_element(By.XPATH,"//input[@name='firstname']")

    actions=ActionChains(driver=driver)
    (actions.key_down(Keys.SHIFT).
     send_keys_to_element(first_name,"the testing academy")
     .key_up(Keys.SHIFT).perform())

    time.sleep(10)

