from cards.card import Card
from cards.hand import Hand

from three_card_poker.three_card_poker_rank import ThreeCardPokerRank

class ThreeCardPokerEval:
    @staticmethod
    def _validate_is_hand(hand: Hand) -> None:
        if not isinstance(hand, Hand):
            raise TypeError("hand must be an instance of the Hand class")
        
    @staticmethod
    def _validate_3_cards(hand: Hand) -> None:
        if hand.cards_in_hand != 3:
            raise ValueError("hand must have exactly 3 cards")
        
    
    @staticmethod
    def _ranks_to_values(ranks: list) -> list:
        if len(set(ranks).intersection({"A", "2", "3"})) == 3:
            return[1, 2, 3]
        
        faces = {"J": 11, "Q": 12, "K": 13, "A": 14}
        values = [faces[rank] if rank in ["J", "Q", "K", "A"] else int(rank) for rank in ranks]

        return values


    @staticmethod
    def _rank_eval(hand: Hand) -> ThreeCardPokerRank:
        values = ThreeCardPokerEval._ranks_to_values([card.rank for card in hand.cards])

        print()
        print(values)

        
    @staticmethod
    def dealer_qualifies(hand: Hand) -> bool:
        ThreeCardPokerEval._validate_is_hand(hand)
        ThreeCardPokerEval._validate_3_cards(hand)

        ranks = {card.rank for card in hand.cards}

        if ranks.intersection({"Q", "K", "A"}):
            return True
        
        if ThreeCardPokerEval._rank_eval(hand) == ThreeCardPokerRank.HIGH_CARD:
            return False
        
        return True
