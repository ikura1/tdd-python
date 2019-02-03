from moneys.money import Money


class Franc(Money):
    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
