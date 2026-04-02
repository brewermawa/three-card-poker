import pytest

from cards.card import Card
from cards.hand import Hand

from three_card_poker.three_card_poker_eval import ThreeCardPokerEval
from three_card_poker.three_card_poker_rank import ThreeCardPokerRank

class TestThreeCardPokerEval:
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

    hand_A23 = Hand()
    hand_A23.add_card(Card("A", "♣"))
    hand_A23.add_card(Card("2", "♦"))
    hand_A23.add_card(Card("3", "♥"))

    hand_A23_straigth_flush = Hand()
    hand_A23_straigth_flush.add_card(Card("A", "♥"))
    hand_A23_straigth_flush.add_card(Card("2", "♥"))
    hand_A23_straigth_flush.add_card(Card("3", "♥"))

    hand_AKQ = Hand()
    hand_AKQ.add_card(Card("A", "♣"))
    hand_AKQ.add_card(Card("K", "♦"))
    hand_AKQ.add_card(Card("Q", "♥"))

    hand_668 = Hand()
    hand_668.add_card(Card("6", "♣"))
    hand_668.add_card(Card("6", "♦"))
    hand_668.add_card(Card("8", "♥"))

    hand_662 = Hand()
    hand_662.add_card(Card("6", "♣"))
    hand_662.add_card(Card("6", "♦"))
    hand_662.add_card(Card("2", "♥"))


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
        [
            hand_Q62, hand_KJ3, hand_A84, hand_straight_flush,
            hand_flush, hand_234, hand_888, hand_223, hand_A23
        ]
    )
    def test_dealer_qualifies_returns_true_with_qualifying_hands(self, qualified_hand):
        assert ThreeCardPokerEval.dealer_qualifies(qualified_hand) is True


    @pytest.mark.parametrize(
        "nonqualified_hand",
        [hand_J108, hand_246]
    )
    def test_dealer_qualifies_returns_false_with_nonqualifying_hands(self, nonqualified_hand):
        assert ThreeCardPokerEval.dealer_qualifies(nonqualified_hand) is False


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
    def test_eval_raises_typeerror_if_hand_is_not_instance_of_hand(self, invalid_hand):
        with pytest.raises(TypeError):
            ThreeCardPokerEval.eval(invalid_hand)


    @pytest.mark.parametrize(
        "invalid_hand",
        [hand_zero_cards, hand_one_card, hand_two_cards, hand_four_cards]
    )
    def test_eval_raises_valueerror_if_hand_does_not_have_3_cards(self, invalid_hand):
        with pytest.raises(ValueError):
            ThreeCardPokerEval.eval (invalid_hand)


    @pytest.mark.parametrize(
        "hand, expected_rank, sorted_hand",
        [
            (hand_A84, ThreeCardPokerRank.HIGH_CARD, [14, 8, 4]),
            (hand_246, ThreeCardPokerRank.HIGH_CARD, [6, 4, 2]),
            (hand_A23, ThreeCardPokerRank.STRAIGHT, [3, 2, 1]),
            (hand_A23_straigth_flush, ThreeCardPokerRank.STRAIGHT_FLUSH, [3, 2, 1]),
            (hand_straight_flush, ThreeCardPokerRank.STRAIGHT_FLUSH, [8, 7, 6]),
            (hand_flush, ThreeCardPokerRank.FLUSH, [8, 6, 2]),
            (hand_888, ThreeCardPokerRank.THREE_OF_A_KIND, [8, 8, 8]),
            (hand_234, ThreeCardPokerRank.STRAIGHT, [4, 3, 2]),
            (hand_AKQ, ThreeCardPokerRank.STRAIGHT, [14, 13, 12]),
            (hand_223, ThreeCardPokerRank.PAIR, [2, 2, 3]),
            (hand_668, ThreeCardPokerRank.PAIR, [6, 6, 8]),
            (hand_662, ThreeCardPokerRank.PAIR, [6, 6, 2]),
        ]
    )
    def test_eval_returs_correct_hand_rank_and_sorted_list(self, hand, expected_rank, sorted_hand):
        result = ThreeCardPokerEval.eval(hand)
        assert result["rank"] == expected_rank
        assert result["sorted_hand"] == sorted_hand


#-----------------------------------------------------

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
    def test_pair_plus_raises_typeerror_if_hand_is_not_instance_of_hand(self, invalid_hand):
        with pytest.raises(TypeError):
            ThreeCardPokerEval.pair_plus(invalid_hand)


    @pytest.mark.parametrize(
        "invalid_hand",
        [hand_zero_cards, hand_one_card, hand_two_cards, hand_four_cards]
    )
    def test_pair_plus_raises_valueerror_if_hand_does_not_have_3_cards(self, invalid_hand):
        with pytest.raises(ValueError):
            ThreeCardPokerEval.pair_plus(invalid_hand)


    @pytest.mark.parametrize(
        "hand, bet_multiplier",
        [
            (hand_A84, 0),
            (hand_246, 0),
            (hand_A23, 6),
            (hand_A23_straigth_flush, 40),
            (hand_straight_flush, 40),
            (hand_flush, 3),
            (hand_888, 30),
            (hand_234, 6),
            (hand_AKQ, 6),
            (hand_223, 1),
            (hand_668, 1),
            (hand_662, 1),
        ]
    )
    def test_pair_plus_returs_correct_bet_multiplier(self, hand, bet_multiplier):
        assert ThreeCardPokerEval.pair_plus(hand) == bet_multiplier