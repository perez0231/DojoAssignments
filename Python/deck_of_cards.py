import random

class Deck(object):
    def __init__(self):
        self.deck =[]


    def createdeck(self):
        suits = ["Heart", "Diamond", "Club", "Spade"]
        values = ["Ace", "2", "3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for suit in suits:
            for val in values:
                card = Card(suit, val)
                self.deck.append(card)


        print self.deck
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        print self.deck
        return self.deck

    def dealCards(self):
        print"dealtcards"
        return(self.deck.pop(), self.deck.pop())

    def resetDeck(self):
        self.deck =[]
        print self.deck
        self.createdeck()
        return self.deck

class Card(object):
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "Card(suit %r, Value %r)" % (self.suit, self.value)

deck1 = Deck() #creating
print "non shuffled"
deck1.createdeck()
print "shuffled"
deck1.shuffle()
print "Deal 2"
print deck1.dealCards()
print "new deck"
deck1.resetDeck()


# deck1 = Deck() #creating
# print "shuffled"
# deck1.shuffle()
