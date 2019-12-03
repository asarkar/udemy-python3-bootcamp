# asarkar:sec-11$ python -m unittest discover

import sys
sys.path.insert(1, "blackjack")

from blackjack import player
from blackjack import deck
import unittest

class TestDeck(unittest.TestCase):

	def test_init_deck(self):
		d = deck.Deck()
		self.assertEqual(len(d.cards), 52)

	def test_rank(self):
		ranks = [r[0] for r in deck.Rank.__members__.items()]
		self.assertEqual(len(ranks), 13)

	def test_suit(self):
		suits = [s[0] for s in deck.Suit.__members__.items()]
		self.assertEqual(len(suits), 4)

	def test_shuffle(self):
		d = deck.Deck()
		cards = d.cards.copy()
		d.shuffle()
		self.assertNotEqual(cards, d.cards)

	def test_deal(self):
		d = deck.Deck()
		dealt = d.deal()
		self.assertEqual(len(dealt), 1)
		self.assertEqual(len(d.cards), 51)

		dealt = d.deal(2)
		self.assertEqual(len(dealt), 2)
		self.assertEqual(len(d.cards), 49)

		with self.assertRaises(ValueError):
			d.deal(50)

	def test_str(self):
		d = deck.Deck()
		self.assertEqual(str(d), """(HEARTS:TWO), (HEARTS:THREE), (HEARTS:FOUR), (HEARTS:FIVE), (HEARTS:SIX), (HEARTS:SEVEN), (HEARTS:EIGHT), (HEARTS:NINE), (HEARTS:TEN), (HEARTS:TEN), (HEARTS:TEN), (HEARTS:TEN), (HEARTS:ACE), (DIAMONDS:TWO), (DIAMONDS:THREE), (DIAMONDS:FOUR), (DIAMONDS:FIVE), (DIAMONDS:SIX), (DIAMONDS:SEVEN), (DIAMONDS:EIGHT), (DIAMONDS:NINE), (DIAMONDS:TEN), (DIAMONDS:TEN), (DIAMONDS:TEN), (DIAMONDS:TEN), (DIAMONDS:ACE), (SPADES:TWO), (SPADES:THREE), (SPADES:FOUR), (SPADES:FIVE), (SPADES:SIX), (SPADES:SEVEN), (SPADES:EIGHT), (SPADES:NINE), (SPADES:TEN), (SPADES:TEN), (SPADES:TEN), (SPADES:TEN), (SPADES:ACE), (CLUBS:TWO), (CLUBS:THREE), (CLUBS:FOUR), (CLUBS:FIVE), (CLUBS:SIX), (CLUBS:SEVEN), (CLUBS:EIGHT), (CLUBS:NINE), (CLUBS:TEN), (CLUBS:TEN), (CLUBS:TEN), (CLUBS:TEN), (CLUBS:ACE)""")

if __name__ == "__main__":
	unittest.main()
