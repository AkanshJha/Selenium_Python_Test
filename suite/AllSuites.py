import unittest
from sampleproject.Google_Search_Test import GoogleSearch
from withPOM.tests.Login import LogIn
from unnittest.UnitTestCase1 import UnitTestCase1

# Loa ding the test methods from the imported Test Classes
tc_1 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(LogIn)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(UnitTestCase1)

# creating Test Suites
sanity_suite = unittest.TestSuite([tc_1])

# unittest.TextTestRunner().run(sanity_suite)
unittest.TextTestRunner(verbosity=2).run(sanity_suite) # for detailed logs


# class MyTestSuite(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
# if __name__ == '__main__':
#     unittest.main()
