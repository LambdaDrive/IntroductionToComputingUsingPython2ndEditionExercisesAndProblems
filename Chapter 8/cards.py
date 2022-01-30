from random import shuffle


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

#    Solution to Practice Problem 8.6 
#    def __repr__(self):
#        'return formal representation'
#        return "Card('{}', '{}')".format(self.rank, self.suit)
#
#    def __eq__(self, other):
#        'self == other if rank and suit are the same'
#        return self.rank == other.rank and self.suit == other.suit



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

#    Solution to Practice Problem 8.5
#    def __init__(self, cardList=None):
#        '''initialize deck of cards,
#           either using an input list of cards or
#           by generating a standard deck of 52 cards'''
#        
#        if cardList != None:     # input deck provided
#            self.deck = cardList
#        else:                    # no input deck
#            # self.deck is a list of 52 standard playing cards
#            self.deck = []
#            # generate every combination of rank and suit
#            for suit in Deck.suits:
#                for rank in Deck.ranks:
#                    # create Card with rank and suit
#                    # and add to deck
#                    self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        shuffle(self.deck)

#    Solution to Practice Problem 8.7
#    def __len__(self):
#        'returns size of deck'
#        return len(self.deck)
#
#    def __repr__(self):
#        'returns canonical string representation'
#        return 'Deck({})'.format(self.deck)
#
#    def __eq__(self, other):
#        '''returns True if decks have the same cards
#           in the same order'''
#        return self.deck == other.deck



class EmptyDeckError(Exception):
    def __str__(self):
        return 'No more cards in deck'
