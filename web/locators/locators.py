from selenium.webdriver.common.by import By


class LogInLocators:
    login_input = (By.CSS_SELECTOR, "input#login")
    sign_in_button = (By.CSS_SELECTOR, "button.ui-black")
    password_input = (By.ID, "password")
    invalid_data_msg = (By.CSS_SELECTOR, "small.ng-star-inserted")
    password_recovery_button = (By.CSS_SELECTOR, "[routerlink='/auth/password-recovery']")
    login_with_phone_button = (By.CSS_SELECTOR, "[routerlink='/auth/by-phone'']")
    registration_button = (By.CSS_SELECTOR, "[routerlink='/registration']")
    show_password_button = (By.CSS_SELECTOR, "svg.auth__main-form-icon")
    invalid_data_message = (By.CSS_SELECTOR, "div.auth__main-form__validation small")


class OpInfoLocators:
    header_title_opinfo = (By.CSS_SELECTOR, "h2.header__title")
    header_section_all_deals = (By.CSS_SELECTOR, "[routerlink='/deals]")
    header_section_timer = (By.CSS_SELECTOR, "div.header-section.header-section--status")
    icon_feedback = (By.CSS_SELECTOR, "ui-icon-feedback.ui-icon-feedback")
    icon_profile = (By.CSS_SELECTOR, "ui-icon-customer.ui-icon-customer")
    add_products_button = (By.CSS_SELECTOR, "button.oi-sel-products__add")
    add_station_button = (By.CSS_SELECTOR, "button.oi-sel-stations__add")
    add_basis_button = (By.CSS_SELECTOR, "button.oi-tbl__select-basics")


class AllDealsLocators:
    pagination = (By.CSS_SELECTOR, "div.pages")


class ProfileTooltipLocators:
    profile_data_name = (By.CSS_SELECTOR, "div.profile-data__name")
    profile_data_avatar = (By.CSS_SELECTOR, "div.profile-data__avatar")
    profile_data_info = (By.CSS_SELECTOR, "profile-data__info")
    profile_button = (By.CSS_SELECTOR, "ui-icon-profile-setting.ui-icon")
    logout_button = (By.CSS_SELECTOR, "ui-icon-logout.ui-icon")

