class Sell:
    def __init__(self, Ichimlik_nomi, Card_Id):
        self.Ichimlik_nomi = Ichimlik_nomi
        self.Card_Id = Card_Id

    def get_ichimlik(self):
        return self.Ichimlik_nomi

    def get_cardId(self):
        return self.Card_Id