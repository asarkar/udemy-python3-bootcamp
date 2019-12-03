# asarkar:sec-11$ python -m unittest discover

import sys
sys.path.insert(1, "blackjack")

from blackjack import player
from blackjack import deck
import unittest

class TestPlayer(unittest.TestCase):

	def test_init_player(self):
		p1 = player.Player()
		self.assertEqual(p1.chips, 100)
		self.assertEqual(p1.hand_value, 0)

		p2 = player.Player(50)
		self.assertEqual(p2.chips, 50)
		self.assertEqual(p2.hand_value, 0)

	def test_init_dealer(self):
		d = player.Dealer()
		self.assertEqual(d.hand_value, 0)

	def test_hit(self):
		p = player.Player()
		self.assertEqual(p.hand_value, 0)

		p.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		self.assertEqual(p.hand_value, 2)
		self.assertFalse(p.is_bust())

		p.hit((deck.Suit.HEARTS, deck.Rank.ACE))
		self.assertEqual(p.hand_value, 13)
		self.assertFalse(p.is_bust())

		p.hit((deck.Suit.HEARTS, deck.Rank.ACE))
		self.assertEqual(p.hand_value, 14)
		self.assertFalse(p.is_bust())

		p.hit((deck.Suit.HEARTS, deck.Rank.KING))
		self.assertEqual(p.hand_value, 24)
		self.assertTrue(p.is_bust())

	def test_adjust_chips(self):
		p = player.Player(100)

		p.adjust_chips(1, False)
		self.assertEqual(p.chips, 102)

		p.adjust_chips(1, True)
		self.assertEqual(p.chips, 101)

		with self.assertRaises(ValueError):
			p.adjust_chips(102, True)

	def test_str(self):
		p = player.Player()
		p.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		p.hit((deck.Suit.HEARTS, deck.Rank.KING))
		self.assertEqual(str(p), "(HEARTS:TWO), (HEARTS:TEN)")

		d = player.Dealer()
		d.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		d.hit((deck.Suit.HEARTS, deck.Rank.KING))
		self.assertEqual(str(d), "(HEARTS:TWO), (***:***)")

		d.hit((deck.Suit.HEARTS, deck.Rank.THREE))
		self.assertEqual(str(d), "(HEARTS:TWO), (HEARTS:TEN), (HEARTS:THREE)")

if __name__ == "__main__":
	unittest.main()
