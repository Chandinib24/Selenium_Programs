from selenium.webdriver.common.by import By
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P2")
@allure.description("Verify Mouse back")
def test_verify_action():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    atag= driver.find_element(By.ID,"click")
    atag.click()

    time.sleep(3)

    action_builders=ActionBuilder(driver=driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    time.sleep(10)
    driver.quit()

