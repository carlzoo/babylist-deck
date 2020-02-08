from deck import Deck
from card import Card

def test_deck_init():
    d = Deck()
    assert len(d.cards) == 52

def test_deck_deal():
    d = Deck()
    assert len(d.cards) == 52
    assert d.cards[-1] == Card("Spades","King")
    d.deal()
    assert len(d.cards) == 51
    assert d.cards[-1] == Card("Spades","Queen")
    d.deal()
    assert len(d.cards) == 50
    assert d.cards[-1] == Card("Spades","Jack")

def test_deck_shuffle():
    d = Deck()
    assert d.cards[-1] == Card("Spades","King")
    assert d.cards[-2] == Card("Spades","Queen")
    assert d.cards[-3] == Card("Spades","Jack")
    assert d.cards[-4] == Card("Spades","10")
    d.shuffle()
    assert d.cards[-1] == Card("Hearts","Ace")
    assert d.cards[-2] == Card("Clubs","Ace")
    assert d.cards[-3] == Card("Hearts","2")
    assert d.cards[-4] == Card("Clubs","2")
    
