import random
from typing import Optional


class Card:
    """A Card object consists of a suit and a rank."""
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"""{self.rank} of {self.suit}"""


class FilterCard:
    """A FilterCard object consists of either suit or rank or both."""
    def __init__(self, rank: Optional[str] = None, suit: Optional[str] = None) -> None:
        if not rank and not suit:
            raise ValueError("Need at least one suit or rank")
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        if self.rank and self.suit:
            return f"""{self.rank} of {self.suit}"""
        else:
            if self.rank:
                return f"""{self.rank} of all suits"""
            else:
                return f"""{self.suit} of the remaining deck"""


class Deck:
    """A Deck object is a collection of Cards."""
    def __init__(self) -> None:
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]


class Deal:
    """Given the deck and number of draws, calculates the probability of a
    given card.

    Public Methods:
        shuffle(): shuffle the deck.
        draw(self, draws): counts for number of cards drawn and the resulting hand.
        next_card_prob(self, target_card): calculates the probability of drawing a specific card
    """
    def __init__(self) -> None:
        self.deck = Deck()
        self.hand = list()

    def shuffle(self):
        random.shuffle(self.deck.cards)

    def draw(self, draws: int = 1):
        for i in range(draws):
            card_drawn = self.deck.cards.pop(0)
            self.hand.append(card_drawn)

    def next_card_prob(self, target_card: FilterCard) -> float | int:
        remaining_cards = len(self.deck.cards)

        if target_card.suit and target_card.rank:
            match = sum(1 for c in self.deck.cards if c.rank == target_card.rank and c.suit == target_card.suit)
        else:
            if target_card.suit:
                match = sum(1 for c in self.deck.cards if c.suit == target_card.suit)
            else:
                match = sum(1 for c in self.deck.cards if c.rank == target_card.rank)
        return match / remaining_cards if remaining_cards > 0 else 0







