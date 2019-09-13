from enum import Enum

class Card:
    def __init__(self, color, suit, fill, value):
        self.color = color
        self.suit = suit
        self.fill = fill
        self.value = value

    def __str__(self):
        return ("Color: {c}, Suit:{s}, Fill:{f}, Value:{v}"
        .format(c= self.color, s= self.suit, f= self.fill, v= str(self.value)))

class Color(Enum):
    red = 1
    green = 2
    purple = 3

class Suit(Enum):
    diamond = 1
    circle = 2
    wave = 3

class Fill(Enum):
    solid = 1
    striped = 2
    blank = 3
