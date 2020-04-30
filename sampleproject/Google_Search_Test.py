from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set Up Class Method")
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_on_google(self):
        print("Search on Google")
        self.driver.get("https:\\www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("searching on google")
        # self.driver.find_element_by_name("btnk").click()

    def test_search_on_google_my_name(self):
        print("Search your name on Google..")
        self.driver.get("https:\\www.google.co.in")
        self.driver.find_element_by_name("q").send_keys("Akansh Jha")
        # self.driver.find_element_by_name("btnk").click()

    @classmethod
    def tearDownClass(cls):
        print("Closing the  browser instance..")
        cls.driver.quit()
        print("Test case executed successfully..")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"))
