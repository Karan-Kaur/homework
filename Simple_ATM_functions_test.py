import unittest
#ideas for unit tests:
# check withdrawal calculation
# check for valid pin- between 1000 and 9999, 4 digits
# check balance is positive
# check for raised errors:
#  -make sure positive number given for withdrawal
#  -make sure integer given for pin, not character

from Simple_ATM_functions import check_withdraw
from Simple_ATM_functions import check_int
from Simple_ATM_functions import pin
from Simple_ATM_functions import check_pos
from Simple_ATM_functions import check_remaining

#seeing what output looks like
class TestExp(unittest.TestCase):
    def test_experimenting(self):
        pass

#test to check pin is valid- Boolean
class TestValidPin(unittest.TestCase):
    def test_pin(self):
        result = pin(num=1123)
        self.assertEqual(result, True)

#test to check pin is an integer- raise error
class TestCheckInt(unittest.TestCase):
    def test_check_int(self):
        self.assertRaises(TypeError, check_int, 'abc')
        self.assertRaises(TypeError, check_int, 'lomx')

#test to check withdrawal amount is positive- raise error
class TestCheckPos(unittest.TestCase):
    def test_check_pos(self):
        self.assertRaises(ValueError, check_pos, -19)
        self.assertRaises(ValueError, check_pos, -1)

#test to check remaining balance is positive- Boolean
class TestRemaining(unittest.TestCase):
    def test_check_remaining(self):
        result = pin(num4= 12)
        self.assertEqual(result, True)
#assert greater equal, lesser equal?

#test to check withdrawal calculation
class TestWithdraw(unittest.TestCase):
    def test_check_withdraw(self):
        self.assertEqual(check_withdraw(30), 70)
        self.assertEqual(check_withdraw(49), 51)

#OR
class TestWithdraw(unittest.TestCase):
    def test_check_withdraw(self):
        expected = 70
        result = check_withdraw(num3= 30)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
