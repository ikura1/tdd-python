class Franc:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def __eq__(self, franc):
        return self.__amount == franc.amount
