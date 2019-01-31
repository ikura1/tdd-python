from moneys.dollar import Dollar
from moneys.franc import Franc
import unittest


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(6)))
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))
        self.assertFalse(Franc(5).__eq__(Dollar(5)))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))


if __name__ == "__main__":
    unittest.main()
