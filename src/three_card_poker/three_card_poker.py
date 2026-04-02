from cards.deck import Deck
from cards.hand import Hand


class ThreeCardPoker:
    def __init__(self, deck: Deck) -> None:
        if not isinstance(deck, Deck):
            raise TypeError("deck must be an instance of Deck")
        
        if deck.jokers:
            raise ValueError("deck cannot contain jokers")
        
        if deck.decks > 1:
            raise ValueError("only 1 deck permited")
        
        if deck.cards_remaining < 52:
            raise ValueError("Deck must have 52 cards")
        
                
        self.deck = deck
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    