import time
from web.locators.locators import LogInLocators, OpInfoLocators, ProfileTooltipLocators
from web.pages.login_page import LogInPage
from config import Credentials


def test_login_with_valid_data(browser):
    log_in_page = LogInPage(browser)
    log_in_page.go_to_site()
    log_in_page.set_user_inputs(Credentials.LOGIN, Credentials.PASSWORD)
    time.sleep(5)
    assert browser.current_url == "https://market.proleum.pro/opinfo"

