import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = None
        # self.assertEqual("String1", "String2", "Failed String Comparision.")
        # self.assertNotEqual("String1", "String1", "Failed as Strings are same.")
        # self.assertTrue(5 % 2 == 0, " Failed Assert True")
        self.assertIsNone(driver) # True
        self.assertIsNotNone(driver) # False
        data = ["Java", "Python","Selenium"]
        self.assertIn("Java", data, "Value is not present.") # returns True
        self.assertNotIn("Ruby", data, "Value is present") # returns True as Ruby is not in data list
        self.assertGreater(100, 1) # pass message as thrid param, which will be executed when failed.
        self.assertGreaterEqual(11,11) # True, same we have for AssertLess
        self.assertLess()
        self.assertLessEqual()

if __name__ == '__main__':
    unittest.main()
