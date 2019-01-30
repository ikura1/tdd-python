# TODO: $5 + 10 CHR = $10
# TODO: amount を private にする
# TODO: Moneyの丸め処理をどうする?
# TODO: hashCode()
# TODO: nullとの等価性比較
# TODO: 他のオブジェクトとの等価性比較
# TODO: DollarとFrancの重複
# TODO: timesの一般化
# TODO: Franc とDollarを比較する
from moneys.money import Money


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
