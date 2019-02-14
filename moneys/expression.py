class Expression:
    @staticmethod
    def times(multiplier):
        pass

    def plus(self, addend):
        from moneys.sum import Sum

        return Sum(self, addend)

    @staticmethod
    def reduce(bank, to):
        pass
