from moneys.money import Money


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = "CHF"

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
