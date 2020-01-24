from card import Card, Color, Suit, Fill


def check_set(c1, c2, c3):
    if ((c1.color == c2.color == c3.color or c1.color != c2.color != c3.color) and
        (c1.suit == c2.suit == c3.suit or c1.suit != c2.suit != c3.suit) and 
        (c1.fill == c2.fill == c3.fill or c1.fill != c2.fill != c3.fill) and
        (c1.value == c2.value == c3.value or c1.value != c2.value != c3.value)):
            return True
    return False
        


def main():
    c1 = Card(Color.red, Suit.diamond, Fill.blank, 1)
    c2 = Card(Color.red, Suit.diamond, Fill.blank, 2)
    c3 = Card(Color.red, Suit.diamond, Fill.blank, 2)
    print(check_set(c1, c2, c3))

if __name__ == "__main__":
    main()