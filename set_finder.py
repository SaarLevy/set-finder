from card import Card, Color, Suit, Fill


def find_sets(cards):
    triplets = combinations(cards, 3)
    sets = []

    for t in triplets:
        if check_set(t):
            sets.push(t)
    return sets

def check_set(c1, c2, c3):
    if ((c1.color == c2.color == c3.color or c1.color != c2.color != c3.color) and
        (c1.suit == c2.suit == c3.suit or c1.suit != c2.suit != c3.suit) and 
        (c1.fill == c2.fill == c3.fill or c1.fill != c2.fill != c3.fill) and
        (c1.value == c2.value == c3.value or c1.value != c2.value != c3.value)):
            return True
    return False