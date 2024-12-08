import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
@allure.description("verify to fetch product titles and prices  ")
@allure.title("Verify the desktop ebay site ")
def test_task17():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    search_input_element=driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    search_input_element.send_keys("macmini")
    search_box_Button=driver.find_element(By.CSS_SELECTOR,"input[value='Search']")
    search_box_Button.click()


    list_of_items=driver.find_elements(By.CSS_SELECTOR,".s-item_title")
    list_of_items_price=driver.find_elements(By.CSS_SELECTOR,".s-item_price")
    len_items=len(list_of_items)
    len_item_price=len(list_of_items_price)
    min_items=min(list_of_items,list_of_items_price)
    print(min_items)


    for i in (range,min_items):
        print (i)


    time.sleep(10)
    driver.quit()