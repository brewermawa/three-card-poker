# 3cp

A Three Card Poker evaluation library. Built on top of `card-deck-hand`.

This library has no knowledge of bets, game flow, or simulation logic. That belongs to the DES handlers.

---

# class ThreeCardPokerRank

An Enum representing the rank of a Three Card Poker hand, ordered from lowest to highest.

```python
class ThreeCardPokerRank(Enum):
    HIGH_CARD = "high card"
    PAIR = "pair"
    FLUSH = "flush"
    STRAIGHT = "straight"
    THREE_OF_A_KIND = "three of a kind"
    STRAIGHT_FLUSH = "straight flush"
```

---

# class ThreeCardPokerEval

Evaluates a three card hand. Has no knowledge of bets, dealer rules, or game flow.

## Methods

### eval
- Receives a three card `Hand` instance
- Raises TypeError if the hand received is no instance of Hand
- Raises `ValueError` if the hand does not contain exactly 3 cards
- Returns a dict with the following structure:
  - `rank`: a `ThreeCardPokerRank` value
  - `sorted_hand`: a list of 3 integers representing card values sorted high to low

**Rank to integer mapping:**

| Rank | Value |
|---|---|
| A | 14 |
| K | 13 |
| Q | 12 |
| J | 11 |
| 10–2 | face value |

**Edge case:** In an A-2-3 straight, the A takes a value of 1. The returned `sorted_hand` for this case is `[3, 2, 1]`.

**Sorting rules:**
- Cards are sorted high to low by integer value
- Suits are not considered in sorting
- Exception: when the hand contains a pair, the pair appears first in `sorted_hand` to ensure correct comparison between two hands of the same rank. Example: `{"rank": ThreeCardPokerRank.PAIR, "sorted_hand": [6, 6, 13]}`

### dealer_qualifies
- Receives a three card `Hand` instance
- Raises TypeError if the hand received is no instance of Hand
- Raises `ValueError` if the hand does not contain exactly 3 cards
- Returns `True` if the hand contains a Queen or higher, `False` otherwise

---

# class PairPlus

Evaluates the player's hand against the PairPlus pay table. Has no knowledge of the dealer's hand, the ante bet, or game flow.

## Methods

### eval
- Receives a three card `Hand` instance
- Raises TypeError if the hand received is no instance of Hand
- Raises `ValueError` if the hand does not contain exactly 3 cards
- Internally calls `ThreeCardPokerEval.eval()` to determine the hand rank
- Returns an `int` representing the payout multiplier based on the following pay table:

| Hand | Multiplier |
|---|---|
| HIGH_CARD | 0 |
| PAIR | 1 |
| FLUSH | 3 |
| STRAIGHT | 6 |
| THREE_OF_A_KIND | 30 |
| STRAIGHT_FLUSH | 40 |

- A return value of `0` means the bet does not pay.

---

# class ThreeCardPoker

Initializes the components needed for a round of Three Card Poker.

## Parameters
- `deck`: a `Deck` instance. Raises `TypeError` if not a `Deck`. Raises `ValueError` if the deck contains jokers.

## Attributes
- `self.deck`: the `Deck` instance
- `self.player_hand`: an empty `Hand` instance
- `self.dealer_hand`: an empty `Hand` instance

---

## Comments
- `SixCardBonus` is intentionally out of scope for v1. It requires a 5-card traditional poker evaluator, which is a separate project.
- Game flow, handler logic, and bet resolution belong in the DES layer, not here.
