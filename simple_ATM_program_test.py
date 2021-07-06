import unittest

#ideas for testing ATM program
#- check pin is within range 1000 and 9999. possibly check only 4 digits entered
#- check subtraction from account balance works
#- check error raised for following situations:
#  - value error raised if user inputs characters, not integers
#  - error raised if user gives negative number to withdraw

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

#ATM functions- testing
import unittest
