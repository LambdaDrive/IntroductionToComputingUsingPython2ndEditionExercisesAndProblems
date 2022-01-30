import random

class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit

class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

class EmptyDeckError(Exception):
    def __str__(self):
        return 'No more cards in deck'

class Hand:

    def __init__(self, playerID):
        self.player = playerID
        self.hand = []
        
    def addCard(self, card):
        self.hand.append(card)

    def showHand(self):
        print('{}: '.format(self.player), end = '')
        for card in self.hand:
            print('{} {}'.format(card.rank, card.suit), end = '')
        print()

def total(mao):
    'returns the value of the blackjack hand'
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    result = 0
    numAces = 0
    
    # add up the values of the cards in the hand
    # also add the number of aces
    for card in mao:
        result += values[card.rank]
        if card == 'A':
            numAces += 1

    # while value of hand is > 21 and there is an ace
    # in the hand with value 11, convert its value to 1
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1

    return result

def compareHands(house, player):
    'compares house and player hands and prints outcome'

    # compute house and player hand total
    houseTotal, playerTotal = total(house), total(player)

    if houseTotal > playerTotal:
        print('You loose.')
    elif houseTotal < playerTotal:
        print('You win.')
    elif houseTotal == 21 and 2 == len(house.hand) < len(player.hand):
        print('You loose.') # house wins with a blackjack
    elif playerTotal == 21 and 2 == len(player) < len(house):
        print('You win.')   # player wins with a blackjack
    else:
        print('A tie.')

def blackjack():
    'simulates the house in a game of blackjack'

    deck = Deck()
    deck.shuffle()
    
    house = Hand('House')  # house hand
    player = Hand('Player') # player hand

    for i in range(2):        # dealing initial hands in 2 rounds
        player.addCard(deck.dealCard())    # deal to player first
        house.addCard(deck.dealCard())    # deal to house second

    # print hands
    house.showHand()
    player.showHand()

    # while user requests an additional card, house deals it
    answer = input('Hit or stand? (default: hit): ')
    while answer in {'', 'h', 'hit'}:
        player.addCard(deck.dealCard())
        card = player.hand[-1]
        print('You got{} {}'.format(card.rank, card.suit))
        
        if total(player.hand) > 21:    # player total is > 21
            print('You went over... You loose.')
            return

        answer = input('Hit or stand? (default: hit): ')

    # house must play the "house rules"
    while total(house.hand) < 17:
        house.addCard(deck.dealCard())
        card = house.hand[-1]        
        print('House got{} {}'.format(card.rank, card.suit))

        if total(house.hand) > 21:     # house total is > 21
            print('House went over... You win.')
            return

    # compare house and player hands abd print result
    compareHands(house.hand, player.hand)

if __name__ == '__main__':
    blackjack()
            
