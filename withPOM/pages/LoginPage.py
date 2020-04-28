class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.userName_textbox_ID = "txtUsername"
        self.password_textbox_ID = "txtPassword"
        self.login_button_ID = "btnLogin"
        self.homepage_Dashboard_link_id = "menu_dashboard_index"

    def login_into_application(self, username, password):
        try:
            self.driver.find_element_by_id(self.userName_textbox_ID).clear()
            self.driver.find_element_by_id(self.userName_textbox_ID).send_keys(username)
            self.driver.find_element_by_id(self.password_textbox_ID).send_keys(password)
            self.driver.find_element_by_id(self.login_button_ID).click()
            if self.driver.find_element_by_id(self.homepage_Dashboard_link_id).is_displayed():
                print("Logged in into the application with credentials {}/{}".format(username, password))
            else:
                raise Exception
        except:
            print("Error occurred while trying to login with given credentials..")

    def set_username(self, username):
        self.driver.find_element_by_id(self.userName_textbox_ID).clear()
        self.driver.find_element_by_id(self.userName_textbox_ID).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_ID).clear()
        self.driver.find_element_by_id(self.password_textbox_ID).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element_by_id(self.login_button_ID).click()
        if self.driver.find_element_by_id(self.homepage_Dashboard_link_id).is_displayed():
            print("Logged in into the application with given credentials.")
        else:
            raise Exception
