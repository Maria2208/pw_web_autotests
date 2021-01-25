from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_length_of_menu():
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
        links_in_the_sidebar = browser.find_elements(By.CSS_SELECTOR, '[routerlinkactive="menu__item__active"]')

        assert len(links_in_the_sidebar) == 4

    finally:
        #time.sleep(5)
        browser.quit()
