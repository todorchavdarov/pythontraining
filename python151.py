import random
from datetime import datetime
from enum import Enum

# define list of const values for card ranks
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class SUIT(str, Enum):
    Club = "Club"
    Diamond = "Diamond"
    Heart = "Heart"
    Spade = "Spade"


class BlackJackCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.soft = 1
        self.hard = 11


class Deck:

    def __init__(self):
        self._cardDeck = [BlackJackCard(suit, rank) for suit in SUIT for rank in RANKS]
        self.shuffle()

    def pop(self):
        return self._cardDeck.pop()

    def shuffle(self):
        random.shuffle(self._cardDeck)


class Hand:
    def __init__(self, dealer_card: BlackJackCard, *cards: BlackJackCard) -> None:
        self.dealer_card = dealer_card
        self._cards = list(cards)

    def __str__(self) -> str:
        return ".".join.map(str, self.card)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"{self.dealer_card!r}"
            f"{','.join(map(repr, self.card))}"
        )

    def __str__(self):
        return ", ".join(map(str, self.card))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(__class__=self.__class__,
                                                                            _cards_str=", ".join(map(repr, self.card)),
                                                                            **self.__dict__)


class HandLazy(Hand):

    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)

    @property
    def total(self):
        delta_soft = max(c.soft - c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total + delta_soft <= 21:
            return hard_total + delta_soft
        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, single_card):
        self._cards.append(single_card)

    @card.deleter
    def card(self):
        self._cards.pop(-1)


d = Deck()
h = HandLazy(d.pop(), d.pop(), d.pop())
print(h.total)
