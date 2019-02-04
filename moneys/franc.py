from moneys.money import Money


class Franc(Money):
    def __init__(self, amount, currency):
        return super().__init__(amount, currency)
