from beverage import Baverage

class MToldir:
    def __init__(self, ustun_raqami, Ichimlik_nomi, Bankalar_soni):
        self._Ichimlik_nomi = Ichimlik_nomi
        self._Bankalar_soni = Bankalar_soni
        self._ustun_raqami = ustun_raqami

    def get_ustun(self):
        return self._ustun_raqami

    @property
    def Ichimlik_n(self):
        return self._Ichimlik_nomi

    @Ichimlik_n.setter
    def Ichimlik_n(self, new):
        self._Ichimlik_nomi = new

    @property
    def Banka_s(self):
        return self._Bankalar_soni

    @Banka_s.setter
    def Banka_s(self, new_b):
        self._Bankalar_soni = new_b


