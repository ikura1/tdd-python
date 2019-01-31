from moneys.dollar import Dollar
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

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
        return Dollar(amount)
