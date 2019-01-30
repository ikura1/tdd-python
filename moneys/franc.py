from moneys.money import Money


class Franc(Money):
    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def __eq__(self, franc):
        return self.amount == franc.amount
