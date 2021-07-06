import unittest
from Simple_ATM_functions import check_withdraw

#seeing what output looks like
class TestExp(unittest.TestCase):
    def test_experimenting(self):
        pass

#checking withdrawal calculation
class TestWithdraw(unittest.TestCase):
    def test_check_withdraw(self):
        self.assertEqual(check_withdraw(30), 70)
        self.assertEqual(check_withdraw(49), 51)
        self.assertEqual(check_withdraw(90), 10)


if __name__ == '__main__':
    unittest.main()
