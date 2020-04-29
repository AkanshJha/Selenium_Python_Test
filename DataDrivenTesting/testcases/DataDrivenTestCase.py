from DataDrivenTesting.excelutility.ExcelUtils import ExcelUtils
from DataDrivenTesting.pages.NewToursLogin import NewToursLoginPage
from selenium import webdriver
import time
import unittest
import sys


class DDT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_case1(self):
        read_excel = ExcelUtils("../../TestFiles - Excel/InputData.xlsx")
        login_obj = NewToursLoginPage(self.driver)
        expected_title = "Find a Flight: Mercury Tours:"
        num_of_rows = read_excel.get_number_of_rows()
        num_of_columns = read_excel.get_number_of_columns()
        print(num_of_rows, num_of_columns)
        self.driver.get("http://newtours.demoaut.com/")

        time.sleep(3)
        for r in range(2,num_of_rows+1):
            for c in range(1, num_of_columns):
                #print(read_excel.read_xl_data(r,c), end=" | ")
                if c == 1:
                    login_obj.set_username(read_excel.read_xl_data(r,c))
                elif c == 2:
                    login_obj.set_password(read_excel.read_xl_data(r,c))
                    login_obj.click_signin()
                    time.sleep(5)
                    actual_title = self.driver.title
                    print(actual_title)
                    if actual_title == expected_title:
                        try:
                            read_excel.update_xl_data(r, c + 1, "Logged in Successfully.")
                        except PermissionError:
                            print("""Please make sure, the file you are trying to make changes in, is not opened.
                            Please close the file.""")
                            #sys.exit("Close Files")
                        except:
                            print("some error occurred. Please verify.")
                            sys.exit()
                    else:
                        try:
                            read_excel.update_xl_data(r, c + 1, "Could not login.")
                        except PermissionError:
                            print("""Please make sure, the file you are trying to make changes in, is not opened.
                            Please close the file.""")
            #self.driver.get("http://newtours.demoaut.com/")
            login_obj.click_home()

        read_excel.save_xl_data()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Execution Finished..")


if __name__ == '__main__':
    unittest.main()