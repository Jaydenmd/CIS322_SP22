from testing_base import *

def compare_shuffled_deck():
    ordered_deck = Deck()                                                       #This seems pretty nice! I guess if you want for more efficiency, you could assign both of the variabes to Deck() on one line
    shuffled_deck = Deck()
    shuffled_deck.shuffle()

    dealer = Dealer()

    num_matches = 0
    for idx, card in enumerate(ordered_deck.cards):
        if card == shuffled_deck.cards[idx]: num_matches += 1                   #It might also be beneficial to try an else that makes it reshuffle if you want to

    return num_matches

def test_shuffle():
    assert compare_shuffled_deck() == 0

