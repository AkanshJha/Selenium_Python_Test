import time
from selenium import webdriver
import unittest
import HtmlTestRunner
from withPOM.pages.LoginPage import LoginPage
from withPOM.pages.HomePage import HomePage


class LogIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_into_application(self):
        driver = self.driver
        login = LoginPage(driver)
        self.open_url(driver)
        login.set_username("admin")
        login.set_password("admin123")
        login.click_on_login_button()

    def test_logout_from_application(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.logout_from_application()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Execution Finished..")

    @staticmethod
    def open_url(drivers):
        url = "https://opensource-demo.orangehrmlive.com/"
        print("Opening URL : '{}'".format(url))
        drivers.get(url)


if __name__ == "__main__":
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"))
