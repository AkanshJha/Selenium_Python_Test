from selenium import webdriver
import pytest


class TestPyTest:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("Execution Finished..")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        text = driver.title
        assert text == 'OrangeHRM'

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Execution completed")
