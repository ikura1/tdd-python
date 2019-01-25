# TODO: $5 + 10 CHR = $10
# TODO: $5 + 3 = $10
# TODO: amount を private にする
# TODO: Dollarの副作用をどうする?
# TODO: Moneyの丸め処理をどうする?


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount = self.amount * 2
