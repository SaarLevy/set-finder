from card import *


def find_sets(cards):
    triplets = combinations(cards, 3)
    sets = []

    for t in triplets:
        if check_set(t):
            sets.push(t)
    return sets

def values_consistent(a, b, c):
    return a == b == c or a != b != c

def check_set(c1, c2, c3):
    return (values_consistent(c1.color, c2.color, c3.color) and
    values_consistent(c1.suit, c2.suit, c3.suit) and
    values_consistent(c1.fill, c2.fill, c3.fill) and
    values_consistent(c1.value, c2.value, c3.value))