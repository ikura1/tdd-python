class Money:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount
