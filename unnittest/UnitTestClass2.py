import unittest

#use of setUPClass() and tearDownClass()


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This method executed once before the very first test case of the class.")

    @classmethod
    def tearDownClass(cls):
        print("This method is executed once after all the test cases of the class are executed.")

    def test_testcase1(self):
        print("This is the first test case.")

    def test_testcase2(self):
        print("This is the second test case.")

    def test_testcase3(self):
        print("this is the third test case.")


if __name__ == '__main__':
    unittest.main()
