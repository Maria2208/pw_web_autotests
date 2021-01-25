from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_login():
    try:
        link = "https://market.proleum.pro/auth/by-login"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        login = browser.find_element(By.CSS_SELECTOR, "input#login")
        login.send_keys("tkachenko.mm")
        password = browser.find_element(By.ID, "password")
        password.send_keys("test123")
        button = browser.find_element(By.CSS_SELECTOR, "button.ui-black")
        button.click()
        #all_deals_header = browser.find_element(By.CSS_SELECTOR, "a.all-deals-link span")
        time.sleep(5)
        url_opinfo = browser.current_url

        assert url_opinfo == "https://market.proleum.pro/opinfo"

    finally:
        #time.sleep(5)
        browser.quit()
