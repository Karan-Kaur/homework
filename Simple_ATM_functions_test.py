import unittest
from Simple_ATM_functions import check_withdraw


class TestExp(unittest.TestCase):
    def test_experimenting(self):
        pass
#takes into account users input pin code- incorrect
class TestPin(unittest.TestCase):
    def test_pincode(self):
        expected = 'Invalid pin code' #assume
        result = pin_code()
        self.assertEqual(expected, result) #assert

#does not need user input- still issues
class TestPin2(unittest.TestCase):
    def test_givenpin(self):
        expected = 'Invalid'  # assume
        result = pin_code2(999)  # #action
        self.assertEqual(expected, result) #assert


if __name__ == '__main__':
    unittest.main()