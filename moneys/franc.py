from moneys.money import Money


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = "CHF"

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
