# TODO: $5 + 10 CHF = $10 (レートが2:1の場合)
# TODO: Moneyの丸め処理をどうする？
# TODO: $5 + $5 = $10
# TODO: $5 + $5 がMoneyを返す
# TODO: hashCode()
# TODO: nullとの等価性比較
# TODO: 他のオブジェクトとの等価性比較
# TODO: Moneyを変換して換算を行う
# TODO: Reduce(bank, String)
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

    def reduce(self, to):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
