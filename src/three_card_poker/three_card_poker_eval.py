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
    def _is_flush(suits: list) -> bool:
        return len(set(suits)) == 1

    
    @staticmethod
    def _is_straight(values: list) -> bool:
        sorted_values = sorted(values)
        return all([(second_value - first_value) == 1 for first_value, second_value in zip(sorted_values, sorted_values[1:])])
    
    
    @staticmethod
    def _is_three_of_a_kind(values: list) -> bool:
        return len(set(values)) == 1
    

    @staticmethod
    def _is_pair(values: list) -> bool:
        return len(set(values)) == 2
    

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
        suits = [card.suit for card in hand.cards]

        if ThreeCardPokerEval._is_flush(suits) and ThreeCardPokerEval._is_straight(values):
            return ThreeCardPokerRank.STRAIGHT_FLUSH

        if ThreeCardPokerEval._is_flush(suits):
            return ThreeCardPokerRank.FLUSH
        
        if ThreeCardPokerEval._is_straight(values):
            return ThreeCardPokerRank.STRAIGHT

        if ThreeCardPokerEval._is_three_of_a_kind(values):
            return ThreeCardPokerRank.THREE_OF_A_KIND
        
        if ThreeCardPokerEval._is_pair(values):
            return ThreeCardPokerRank.PAIR
        
        return ThreeCardPokerRank.HIGH_CARD

        
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


    @staticmethod
    def eval(hand: Hand) -> dict:
        ThreeCardPokerEval._validate_is_hand(hand)
        ThreeCardPokerEval._validate_3_cards(hand)

        values = ThreeCardPokerEval._ranks_to_values([card.rank for card in hand.cards])
        sorted_values = sorted(values, reverse=True)
        rank = ThreeCardPokerEval._rank_eval(hand)

        if rank == ThreeCardPokerRank.PAIR:
            #after sorting the list of values, the second member of the list will always be the value of the pair
            pair_of = sorted_values[1]
            third_card = sorted_values[2] if pair_of == sorted_values[0] else sorted_values[0]
            sorted_values = [pair_of, pair_of, third_card]


        return {"rank": rank, "sorted_hand": sorted_values}


    @staticmethod
    def pair_plus(hand: Hand) -> int:
        ThreeCardPokerEval._validate_is_hand(hand)
        ThreeCardPokerEval._validate_3_cards(hand)

        BET_MULTIPLIER ={
            ThreeCardPokerRank.HIGH_CARD: 0,
            ThreeCardPokerRank.PAIR: 1,
            ThreeCardPokerRank.FLUSH: 3,
            ThreeCardPokerRank.STRAIGHT: 6, 
            ThreeCardPokerRank.THREE_OF_A_KIND: 30,
            ThreeCardPokerRank.STRAIGHT_FLUSH: 40
        }

        return BET_MULTIPLIER[ThreeCardPokerEval._rank_eval(hand)]

