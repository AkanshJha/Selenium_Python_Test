class NewToursLoginPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__username_textbox_name = "userName"
        self.__password_textbox_name = "password"
        self.__signin_button_name = "login"
        self.__home_tablink_linktext = "Home"

    def set_username(self, username):
        self.__driver.find_element_by_name(self.__username_textbox_name).send_keys(username)
        print("Username '{}' is set successfully.".format(username))

    def set_password(self, password):
        self.__driver.find_element_by_name(self.__password_textbox_name).send_keys(password)
        print("Password '{}' is set successfully.".format(password))

    def click_signin(self):
        self.__driver.find_element_by_name(self.__signin_button_name).click()
        print("Sign in button is clicked successfully.")

    def click_home(self):
        self.__driver.find_element_by_link_text(self.__home_tablink_linktext).click()
        print("Home tab is clicked successfully")
