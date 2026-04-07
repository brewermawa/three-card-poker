from cards.deck import Deck
from cards.card import Card

#["♣", "♦", "♠", "♥"]
class FixedDeck(Deck):
    _TEST_SUIT = "♦"

    def shuffle(self):
        super()._build_deck()

    def _take_one_by_rank(self, rank: str) -> Card:
        """
        Remove and return one existing card from the deck with the given rank.
        Suit is not constrained. Raises ValueError if not found.
        """
        for c in self._deck:
            if c.rank == rank:
                self._deck.remove(c)
                return c
        raise ValueError(f"No card with rank {rank} found in deck")

    def _program_ranks_top(self, ranks_in_draw_order: list[str]) -> None:
        """
        Arrange the deck so that successive draws (pop from end) return the given
        ranks in this exact order. Supports repeated ranks.
        """
        # Take actual cards (preserves multiplicity correctly)
        taken: list[Card] = [self._take_one_by_rank(r) for r in ranks_in_draw_order]

        # Append in reverse so the last appended is drawn first
        for c in reversed(taken):
            self._deck.append(c)


    def deck_for_bj(self):
        self._program_ranks_top(["A", "8", "K", "J"])

    