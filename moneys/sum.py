from moneys.expression import Expression


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        from moneys.money import Money

        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
