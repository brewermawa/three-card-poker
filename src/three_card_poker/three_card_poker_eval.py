from cards.card import Card
from cards.hand import Hand

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
    def dealer_qualifies(hand: Hand) -> bool:
        ThreeCardPokerEval._validate_is_hand(hand)
        ThreeCardPokerEval._validate_3_cards(hand)

        ranks = {card.rank for card in hand.cards}
        suits = {card.suit for card in hand.cards}

        if ranks.intersection({"Q", "K", "A"}):
            return True
        
        #STRAIGHT FLUSH 
        if len(suits) == 1:
            
            pass
