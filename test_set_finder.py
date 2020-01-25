import unittest
import set_finder
from card import *

class Test_Set_Finder(unittest.TestCase):

    def test_values_consistent(self):
        self.assertTrue(set_finder.values_consistent(1, 1, 1))
        self.assertTrue(set_finder.values_consistent(1, 2, 3))
        self.assertFalse(set_finder.values_consistent(1, 1, 2))

    def test_check_set(self):
        a1 = Card(Color.red, Suit.diamond, Fill.striped, 1)
        a2 = Card(Color.red, Suit.diamond, Fill.striped, 2)
        a3 = Card(Color.red, Suit.diamond, Fill.striped, 3)
        self.assertTrue(set_finder.check_set(a1, a2, a3))

        b1 = Card(Color.red, Suit.diamond, Fill.striped, 1)
        b2 = Card(Color.green, Suit.wave, Fill.solid, 1)
        b3 = Card(Color.purple, Suit.circle, Fill.blank, 1)
        self.assertTrue(set_finder.check_set(b1, b2, b3))

        c1 = Card(Color.red, Suit.diamond, Fill.striped, 1)
        c2 = Card(Color.red, Suit.diamond, Fill.striped, 2)
        c3 = Card(Color.green, Suit.circle, Fill.solid, 1)
        self.assertFalse(set_finder.check_set(c1, c2, c3))




        