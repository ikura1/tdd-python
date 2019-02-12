from moneys.expression import Expression


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def plus(self, addend):
        return None

    def reduce(self, bank, to):
        from moneys.money import Money

        amount = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return Money(amount, to)
