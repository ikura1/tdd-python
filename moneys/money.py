from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount
        self._currency = None

    @property
    def amount(self):
        return self._amount

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    @abstractmethod
    def times(self, multiplier):
        pass

    @staticmethod
    def dollar(amount):
        from moneys.dollar import Dollar

        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from moneys.franc import Franc

        return Franc(amount)
