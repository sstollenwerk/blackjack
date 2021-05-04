from dataclasses import dataclass
from typing import Literal, get_args, ClassVar
import itertools
import random

Suit = Literal["Heart", "Diamond", "Club", "Spade"]

Rank = Literal[2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King", "Ace"]


@dataclass
class Card:
    suit: Suit
    rank: Rank


sing_deck = [Card(*c) for c in itertools.product(get_args(Suit), get_args(Rank))]
Deck = list[Card]


@dataclass
class Hand:
    hand: list[Card]
    bid: int = 0




    @property
    def score(self) -> int:
        posses = itertools.product(*map(base_score, self.hand))
        scores = set(map(sum, posses))
        return max((i for i in scores if i < 22))
        # will likely be knowledge duplication and need refactoring later


def base_score(card: Card) -> list[int]:
    if card.rank in {"Jack", "Queen", "King"}:
        return [10]
    elif card.rank == "Ace":
        return [1, 11]
    else:
        assert isinstance(card.rank, int)
        return [card.rank]

@dataclass
class BasePlayer:
    hand:Hand = None
    start_cards:ClassVar[int] = 2

class Dealer (BasePlayer):
    start_cards:ClassVar[int] = 1
