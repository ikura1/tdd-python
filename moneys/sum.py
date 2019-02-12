from moneys.expression import Expression


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        from moneys.money import Money

        amount = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return Money(amount, to)
