# TODO: $5 + 10 CHR = $10
# TODO: amount を private にする
# TODO: Moneyの丸め処理をどうする?


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
