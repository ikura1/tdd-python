from abc import abstractmethod


class Money:
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
        pass

    @staticmethod
    def dollar(amount):
        from moneys.dollar import Dollar

        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        from moneys.franc import Franc

        return Franc(amount, "CHF")
