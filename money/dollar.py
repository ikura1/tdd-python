# TODO: $5 + 10 CHR = $10
# TODO: amount を private にする
# TODO: Moneyの丸め処理をどうする?
# TODO: equals()
# TODO: hashCode()


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, object_):
        return True
