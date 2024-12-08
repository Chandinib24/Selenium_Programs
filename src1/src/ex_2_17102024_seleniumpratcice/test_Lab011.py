import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
@allure.description("verify the registration page ")
@allure.title("Find the xpath for registration")
def test_Project5():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
     #find te element anchor tag
    first_name_tag=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name_tag.send_keys("Hello")

    time.sleep(10)