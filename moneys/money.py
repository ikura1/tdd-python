# TODO: $5 + $5 がMoneyを返す
# TODO: Expression.times


from moneys.sum import Sum
from moneys.expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def currency(self):
        return self._currency

    @property
    def amount(self):
        return self._amount

    def __eq__(self, money):
        return self.amount == money.amount and self.currency() == money.currency()

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency())

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency(), to)
        return Money(self.amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def __repr__(self):
        return f"{self._currency} {self._amount}"
