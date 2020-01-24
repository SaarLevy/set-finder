from card import Card, Color, Suit, Fill
from set_finder import check_set
        

def main():
    c1 = Card(Color.red, Suit.diamond, Fill.striped, 1)
    c2 = Card(Color.red, Suit.diamond, Fill.solid, 2)
    c3 = Card(Color.red, Suit.diamond, Fill.blank, 3)
    print(check_set(c1, c2, c3))
    

if __name__ == "__main__":
    main()