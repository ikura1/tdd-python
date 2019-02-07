from moneys.money import Money
from moneys.bank import Bank
from moneys.sum import Sum
import unittest


class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5).__eq__(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).__eq__(Money.dollar(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_ = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        sum_ = result
        self.assertEqual(five, sum_.augend)
        self.assertEqual(five, sum_.addend)

    def test_reduce_sum(self):
        sum_ = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)


if __name__ == "__main__":
    unittest.main()
