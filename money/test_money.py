from money.dollar import Dollar
import unittest


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))


if __name__ == "__main__":
    unittest.main()
