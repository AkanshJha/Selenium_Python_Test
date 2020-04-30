import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_search_1(self):
        print("Search 1.")

    @unittest.SkipTest # decorator, this will skip this test execution with any reason on console.
    def test_search_2(self):
        print("Search 2.")

    @unittest.skip("on purpose as it is not ready.") # this will be skipped and given reason will be displayed on console.
    def test_search_3(self):
        print("search 3.")

# skipping test on certain conditions.
    @unittest.skipIf(True, "Skipped, as condition is true.")
    def test_search_4(self):
        print("search 4.")

    def test_search_5(self):
        print("search 5.")

    def test_search_6(self):
        print("search 6.")

if __name__ == '__main__':
    unittest.main()
