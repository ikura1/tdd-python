from moneys.money import Money


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount)
        self._currency = currency

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
