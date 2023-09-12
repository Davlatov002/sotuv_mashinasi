from beverage import Baverage
from card import Card
from m_toldirish import MToldir
from sotish import Sell
class VedingMachina:

    beverage_list = []
    card_list = []
    s_list = [MToldir(i, Ichimlik_nomi="", Bankalar_soni=0) for i in range(1, 5)]


    def add_beverage(self, name, price):
        beverage: Baverage
        change = False
        for beverage in self.beverage_list:
            if beverage.get_name == name:
                change = True
                beverage.set_price(price)
        if not change:
            self.beverage_list.append(Baverage(name, price))

    def get_price(self, name):
        beverage: Baverage
        for beverage in self.beverage_list:
            if beverage.get_name == name:
                return beverage.get_price()
        return -1.0

    def beverage_LIST(self):
        beverage: Baverage
        for beverage in self.beverage_list:
            print(f"Ichimlik nomi --> {beverage.get_name}, Ichimlik narhi --> {beverage.get_price()}")

    def rechargeCard(self, Id, Creditt):
        card: Card
        e = False
        for card in self.card_list:
            if card.cardID == Id:
                e = True
                card.credit += Creditt
        if not e:
            self.card_list.append(Card(Id, Creditt))

    def getCredit(self, Id):
        card: Card
        e = False
        for card in self.card_list:
            if card.cardID == Id:
                e = True
                return card.credit
        if not e:
            return -1.0

    def getlistCart(self):
        card: Card
        for card in self.card_list:
            print(f"ID -> {card.cardID}, Credit-> {card.credit}")

    def refill_column(self, ustun_raqami, i_nomi, b_soni):
        m_toldirish: MToldir
        i: Baverage
        chek = False
        for m_toldirish in self.s_list:
            if m_toldirish.get_ustun() == ustun_raqami:
                for i in self.beverage_list:
                    if i_nomi == i.get_name:
                        chek = True
                        if m_toldirish.Ichimlik_n == "":
                            m_toldirish.Ichimlik_n += i_nomi
                            m_toldirish.Banka_s += b_soni
                        elif m_toldirish.Ichimlik_n == i_nomi:
                            m_toldirish.Banka_s += b_soni
                        else:
                            print("Bu ustunda bunaqa turdagi ichimlik yo'q")

        if not chek:
            print("Bunaqa ustun yo'q")

    def availableCans(self):
        m_toldirish: MToldir
        for m_toldirish in self.s_list:
            print (f"{m_toldirish.get_ustun()} inchi ustun Ichimlik nomi --> {m_toldirish.Ichimlik_n}, Bankalr soni --> {m_toldirish.Banka_s}")

    def sell(self, cardid, name):
        sell: Sell
        crd: Card
        mtoldir: MToldir
        beverage: Baverage
        a = False
        b = False
        c = False
        for crd in self.card_list:
            if crd.cardID == cardid:
                a = True
                for beverage in self.beverage_list:
                    if beverage.get_name == name:
                        b = True
                        if crd.credit >= beverage.get_price():
                            c = True
                            crd.credit -= beverage.get_price()
                            for mtoldir in self.s_list:
                                if mtoldir.Ichimlik_n == name:
                                    mtoldir.Banka_s -= 1
                                    print(mtoldir.get_ustun())
        if a == False:
            print(-1.0)
        if b == False:
            print(-1.0)
        if c == False:
            print(-1.0)

