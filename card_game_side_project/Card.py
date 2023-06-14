"""
Name: Card.py
Author: Luke Sears
Purpose: represents a card in a card game.
"""
RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
SUITS = ("Clubs", "Hearts", "Spades", "Diamonds")

class Card:
    """A card in a card game (can serve as a base class for other types
    of card games).
    
    this is a card from a Bicycle/hoyle type card deck like you would 
    use in a Blackjack, Poker type card game.
    
    Attributes:
        RANKS (tuple): off possible card ranks (str)
        SUITS (tuple): of card SUITs (str)
        rank (str): represents the current card's rank
        suit (str): the current card's suit
        is_showing (bool): can we see the rank and suit of a card
        """
    

    # Constructor
    def __init__(self, rank: str, suit: str) -> None:
            self.rank = rank
            self.suit = suit
            self.is_showing = False

    def flip(self):
         self.is_showing = not self.is_showing

    # When displaying a card
    def __str__(self):
         representation = ""
         if self.is_showing:
            representation = self.rank + " of " + self.suit
         else:
            representation = "[]"
         return representation

if __name__ == "__main__":
    card1 = Card("Ace", "Spades")
    print(card1.rank)
    print(card1.suit)
    card1.flip()
    print(card1)
    card1.flip()
    print(card1)