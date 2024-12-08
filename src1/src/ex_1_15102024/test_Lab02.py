from selenium  import webdriver
import allure
import pytest

@allure.title("Verfy the title of the web page app.vwo.com")
def test_open_vwo_login():
    driver=webdriver.Chrome
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title=="Login-VWO"