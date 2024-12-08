from selenium import webdriver

def test_chrome_current_url_verification():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

def test_edge_current_url_verification():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

















