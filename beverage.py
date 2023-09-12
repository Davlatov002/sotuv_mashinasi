class Baverage:

    def __init__(self, name, price):
        self._neme = name
        self._price = price

    @property
    def get_name(self):
        return self._neme

    @get_name.setter
    def get_name(self, new_name):
        self._neme = new_name

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price
