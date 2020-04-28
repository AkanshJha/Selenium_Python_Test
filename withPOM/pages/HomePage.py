import time

from withPOM.pages.LoginPage import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcomeAdmin_link_class = "panelTrigger"
        self.logout_link_xpath = "//a[text()='Logout']"

    def logout_from_application(self):
        self.driver.find_element_by_class_name(self.welcomeAdmin_link_class).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
        if self.driver.find_element_by_id(LoginPage(self.driver).userName_textbox_ID).is_displayed():
            print("Logged out successfully.")
        else:
            raise Exception
