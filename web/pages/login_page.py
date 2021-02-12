from web.pages.base_page import BasePage
from web.locators.locators import LogInLocators, OpInfoLocators, ProfileTooltipLocators


class LogInPage(BasePage):

    def set_user_inputs(self, login, password):
        login_input = self.find_element(LogInLocators.login_input)
        login_input.click()
        login_input.send_keys(login)
        password_input = self.find_element(LogInLocators.password_input)
        password_input.click()
        password_input.send_keys(password)
        sign_in_button = self.find_element(LogInLocators.sign_in_button)
        sign_in_button.click()

    def check_page_after_passed_autorization(self):
        header_title_opinfo = self.find_element(OpInfoLocators.header_title_opinfo)
        return header_title_opinfo.text




