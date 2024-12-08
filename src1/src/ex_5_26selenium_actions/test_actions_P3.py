from selenium.webdriver.common.by import By
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P3")
@allure.description("Verify click and hold")
def test_verify_action():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #draggable
    element_to_hold=driver.find_element(By.ID,"draggable")
    #click normal driver will find the element and click on it
    #click and hold-Action chains-
    atag= driver.find_element(By.ID,"click")
    atag.click()

    time.sleep(3)

    actions=ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(10)
    driver.quit()

