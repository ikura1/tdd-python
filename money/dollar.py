# TODO: $5 + 10 CHR = $10
# TODO: amount を private にする
# TODO: Moneyの丸め処理をどうする?
# TODO: hashCode()
# TODO: nullとの等価性比較
# TODO: 他のオブジェクトとの等価性比較


class Dollar:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def equals(self, dollar):
        return self.__amount == dollar.amount
