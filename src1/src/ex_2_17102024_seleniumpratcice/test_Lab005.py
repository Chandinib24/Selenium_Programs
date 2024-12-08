

from selenium.webdriver.chrome.options import Options


def test_chrome_options():

    chrome_options= Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start_maximized")
    chrome_options.add_argument("--window-size=900,600")


    driver=webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert True==False


