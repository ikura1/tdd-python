class Pair:
    def __init__(self, from_, to):
        self.__from = from_
        self.__to = to

    @property
    def from_(self):
        return self.__from

    @property
    def to(self):
        return self.__to

    def __eq__(self, value):
        return self.__from == value.from_ and self.__to == value.to

    def __hash__(self):
        return 0
