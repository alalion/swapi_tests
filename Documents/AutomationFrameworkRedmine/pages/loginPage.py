from locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.autologin_checkbox_id = Locators.autologin_checkbox_id

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()

    def click_autologin(self):
        self.driver.find_element_by_id(self.autologin_checkbox_id).click()
