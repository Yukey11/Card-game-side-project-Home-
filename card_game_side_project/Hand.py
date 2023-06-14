"""A Hand of playing Card objects"""

class Hand():
    """A hand of playing cards
    
    you cna do the following: add a card, give a card, or clear the hand
    
    Attributes:
        cards (list): a list of card objects"""
    
    # constructor
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def dealcard(self, otherhand):
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            otherhand.add(card)
            return True
        else:
            return False

    def clear(self):
        self.cards = []

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def __str__(self):
        """print the cards, but only if the hand is not empty"""
        if self.cards:
            representation = ""
            for card in self.cards:
                if not card.is_showing:
                    card.flip()
                representation += str(card) + " | "
        else:
            representation = "<empty>"
        return representation
        
if __name__ == "__main__":
    import Card
    

    #create a hand
    deck = Hand()
    for rank in Card.RANKS:
        for suit in Card.SUITS:
            card = Card.Card(rank, suit)
            deck.add(card)        
    print(deck)
    print("shuffling the deck")
    deck.shuffle()
    print(deck)
    print("Dealing cards")
    player1 = Hand()
    player2 = Hand()
    givetoplayer1 = True
    cardsleft = True
    while cardsleft:
        if givetoplayer1:
            cardsleft = deck.dealcard(player1)
            givetoplayer1 = False
        else:
            cardsleft = deck.dealcard(player2)
            givetoplayer1 = True
    print("Player 1 Cards")
    print(player1)
    print("Player 2 Cards")
    print(player2)