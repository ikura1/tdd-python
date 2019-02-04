from moneys.money import Money


class Franc(Money):
    def __init__(self, amount, currency):
        return super().__init__(amount, currency)

    def times(self, multiplier):
        return Franc(self.amount * multiplier, self.currency())
