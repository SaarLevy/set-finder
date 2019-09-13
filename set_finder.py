from card import *

c = Card(Color.red, Suit.diamond, Fill.solid, 3)

def find_sets(cards):
    triplets = combinations(cards, 3)
    sets = []

    for t in triplets:
        if is_set(t):
            sets.push(t)
    return sets

def is_set(card1, card2, card3):
  return (
      values_consistent(card1.color, card2.color, card3.color) and
      values_consistent(card1.suit, card2.suit, card3.suit) and 
      values_consistent(card1.fill, card2.fill, card3.fill) and
      values_consistent(card1.value, card2.value, card3.value)
  )

def values_consistent(a, b, c):
  return a == b == c or a != b != c
