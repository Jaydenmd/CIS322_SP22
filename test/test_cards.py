from testing_base import *

def compare_shuffled_deck():                                                    
    ordered_deck = Deck()
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    dealer = Dealer()

    num_matches = 0
    for idx, card in enumerate(ordered_deck.cards):
        if card == shuffled_deck.cards[idx]: num_matches += 1           #It looks like you have a good approach for your code bro!

    return num_matches

def test_shuffle():
    assert compare_shuffled_deck() == 0

