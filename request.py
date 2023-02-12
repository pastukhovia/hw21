class Request:
    def __init__(self, from_where, to, amount, product):
        self._from_where = from_where
        self._to = to
        self._amount = amount
        self._product = product

    @property
    def from_where(self):
        return self._from_where

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    def __repr__(self):
        return f'{self._amount} {self._product} доставляются из {self._from_where} в {self._to}'
