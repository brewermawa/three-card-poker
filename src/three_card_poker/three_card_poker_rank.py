from enum import Enum


class ThreeCardPokerRank(Enum):
    HIGH_CARD = "high card"
    PAIR = "pair"
    FLUSH = "flush"
    STRAIGHT = "straight"
    THREE_OF_A_KIND = "three of a kind"
    STRAIGHT_FLUSH = "straight flush"