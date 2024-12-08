from selenium  import webdriver
import allure
import pytest

@allure.title("Verfy the title of the web page app.vwo.com")
def test_sample():
    driver=webdriver.Chrome()
    driver.get("https://sdet.live")


