from locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.login_link_class_name = Locators.login_link_class_name
        self.logout_link_class_name = Locators.logout_link_class_name
        self.myaccount_link_xpath = Locators.myaccount_link_xpath

    def click_login_link(self):
        self.driver.find_element_by_class_name(self.login_link_class_name).click()

    def click_logout_link(self):
        self.driver.find_element_by_class_name(self.logout_link_class_name).click()

    def click_myaccount_link(self):
        self.driver.find_element_by_xpath(self.myaccount_link_xpath).click()

    def click_prolects_link(self):
        self.driver.find_element_by_class_name(self.projects_link_class_name).click()
