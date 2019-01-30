from moneys.money import Money


class Franc(Money):
    def times(self, multiplier):
        return Franc(self.amount * multiplier)
