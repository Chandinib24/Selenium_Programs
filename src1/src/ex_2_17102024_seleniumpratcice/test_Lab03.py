from selenium import webdriver

def test_open_vwo_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    page_sorece_data=driver.page_source
    print(page_sorece_data)