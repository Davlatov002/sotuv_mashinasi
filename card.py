class Card:
    def __init__(self, cardId, Credit):
        self._cardId = cardId
        self._Credit = Credit

    @property
    def credit(self):
        return self._Credit

    @credit.setter
    def credit(self, new_credit):
        self._Credit = new_credit

    @property
    def cardID(self):
        return self._cardId

    @cardID.setter
    def cardID(self, new_id):
        self._cardId = new_id
