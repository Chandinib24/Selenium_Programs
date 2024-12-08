import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
@allure.description("verify thae buttons in page")
@allure.title("Find all the buttons by tag name")
def test_negative_Project4():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
     #find te element anchor tag
    buttons=driver.find_elements(By.TAG_NAME,"button")
    print(len(buttons))
    for i in buttons:
        print(i.text)

    all_links_in_page=driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_in_page))
    for i in all_links_in_page:
        print(i.text)