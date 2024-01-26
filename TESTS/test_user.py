

# unit test case
import unittest
 
class TestUser(unittest.TestCase):
    # test function 
    def test_negative(self):
        testValue = False
        # error message in case if test case got failed
        message = "Test value is not true."
        # assertTrue() to check true of test value
        self.assertTrue( True, message)
 
if __name__ == '__main__':
    unittest.main()
