import pytest

from cards.card import Card
from cards.hand import Hand

from three_card_poker.three_card_poker_eval import ThreeCardPokerEval

class TestThreeCardPokerEvalDealerQualifies:
    hand_zero_cards = Hand()

    hand_one_card = Hand()
    hand_one_card.add_card(Card("A", "♣"))

    hand_two_cards = Hand()
    hand_two_cards.add_card(Card("A", "♣"))
    hand_two_cards.add_card(Card("J", "♦"))

    hand_four_cards = Hand()
    hand_four_cards.add_card(Card("A", "♣"))
    hand_four_cards.add_card(Card("J", "♦"))
    hand_four_cards.add_card(Card("8", "♣"))
    hand_four_cards.add_card(Card("9", "♦"))

    hand_Q62 = Hand()
    hand_Q62.add_card(Card("Q", "♣"))
    hand_Q62.add_card(Card("6", "♣"))
    hand_Q62.add_card(Card("2", "♦"))

    hand_KJ3 = Hand()
    hand_KJ3.add_card(Card("K", "♣"))
    hand_KJ3.add_card(Card("J", "♣"))
    hand_KJ3.add_card(Card("3", "♦"))

    hand_A84 = Hand()
    hand_A84.add_card(Card("A", "♣"))
    hand_A84.add_card(Card("8", "♣"))
    hand_A84.add_card(Card("4", "♦"))

    hand_223 = Hand()
    hand_223.add_card(Card("2", "♣"))
    hand_223.add_card(Card("2", "♦"))
    hand_223.add_card(Card("3", "♦"))

    hand_234 = Hand()
    hand_234.add_card(Card("2", "♣"))
    hand_234.add_card(Card("3", "♦"))
    hand_234.add_card(Card("4", "♦"))

    hand_888 = Hand()
    hand_888.add_card(Card("8", "♣"))
    hand_888.add_card(Card("8", "♦"))
    hand_888.add_card(Card("8", "♥"))

    hand_flush = Hand()
    hand_flush.add_card(Card("2", "♦"))
    hand_flush.add_card(Card("6", "♦"))
    hand_flush.add_card(Card("8", "♦"))

    hand_straight_flush = Hand()
    hand_straight_flush.add_card(Card("7", "♦"))
    hand_straight_flush.add_card(Card("6", "♦"))
    hand_straight_flush.add_card(Card("8", "♦"))

    hand_J108 = Hand()
    hand_J108.add_card(Card("J", "♣"))
    hand_J108.add_card(Card("10", "♦"))
    hand_J108.add_card(Card("8", "♥"))

    hand_246 = Hand()
    hand_246.add_card(Card("2", "♣"))
    hand_246.add_card(Card("4", "♦"))
    hand_246.add_card(Card("6", "♥"))


    @pytest.mark.parametrize(
        "invalid_hand",
        [
            {"card1": Card("A", "♣"), "card2": Card("J", "♦")},
            Card("J", "♦"),
            (("A", "♣"), ("J", "♦")),
            None,
            True
        ],
    )
    def test_dealer_qualifies_raises_typeerror_if_hand_is_not_instance_of_hand(self, invalid_hand):
        with pytest.raises(TypeError):
            ThreeCardPokerEval.dealer_qualifies(invalid_hand)


    @pytest.mark.parametrize(
        "invalid_hand",
        [hand_zero_cards, hand_one_card, hand_two_cards, hand_four_cards]
    )
    def test_dealer_qualifies_raises_valueerror_if_hand_does_not_have_3_cards(self, invalid_hand):
        with pytest.raises(ValueError):
            ThreeCardPokerEval.dealer_qualifies(invalid_hand)


    @pytest.mark.parametrize(
        "qualified_hand",
        [hand_Q62, hand_KJ3, hand_A84, hand_straight_flush]
        #[hand_Q62, hand_KJ3, hand_A84, hand_223, hand_234, hand_888, hand_flush]
    )
    def test_dealer_qualifies_returns_true_with_qualifying_hands(self, qualified_hand):
        assert ThreeCardPokerEval.dealer_qualifies(qualified_hand) is True

"""
    @pytest.mark.parametrize(
        "nonqualified_hand",
        [hand_J108, hand_246]
    )
    def test_dealer_qualifies_returns_false_with_nonqualifying_hands(self, nonqualified_hand):
        assert ThreeCardPokerEval.dealer_qualifies(nonqualified_hand) is False
"""