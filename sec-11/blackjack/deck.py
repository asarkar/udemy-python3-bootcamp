from enum import Enum, auto
import random

class Suit(Enum):
	HEARTS = auto()
	DIAMONDS = auto()
	SPADES = auto()
	CLUBS = auto()

class Rank(Enum):
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 10
	QUEEN = 10
	KING = 10
	ACE = auto()

class Deck:
	def __init__(self):
		self.cards = []

		# Simply iterating over the members of an enum does not provide the aliases
		for _,suit in Suit.__members__.items():
			for _,rank in Rank.__members__.items():
				self.cards.append((suit, rank))

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self, num = 1):
		remaining = len(self.cards)
		if num > remaining:
			raise ValueError(f"Cannot deal {num} cards from a desk of {remaining}")
		dealt = self.cards[:num]
		self.cards = self.cards[num:]
		return dealt

	def __str__(self):
		return ", ".join(list(map(lambda c: f"({c[0].name}:{c[1].name})", self.cards)))
