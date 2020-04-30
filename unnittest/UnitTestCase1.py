import unittest

#use of setUp() and tearDown() method

class UnitTestCase1(unittest.TestCase):

    def setUp(self): #This executes before each method.
        print("         Login method")

    def tearDown(self): #This executed after execution of each test method.
        print("      Logout method.")

    def test_testcase1(self):
        print("This is the first test case.")

    def test_testcase2(self):
        print("This is the second test case.")

    def test_testcase3(self):
        print("this is the third test case.")


if __name__ == '__main__':
    unittest.main()