class Hand:

    def __init__(self, playerID):
        self.player = playerID
        self.hand = []
        
    def addCard(self, card):
        self.hand.append(card)

    def showHand(self):
        print('{}: '.format(player), end = '')
        for card in self.hand:
            print('{} '.format(card), end = '')
        print()
