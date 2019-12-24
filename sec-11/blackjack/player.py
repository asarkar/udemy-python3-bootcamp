from . import deck

class AbstractPlayer:
	def __init__(self):
		self.hand = []
		self.hand_value = 0

	def __str__(self):
		return ", ".join(list(map(lambda c: f"({c[0].name}:{c[1].name})", self.hand)))

	def hit(self, card):
		self.hand.append(card)
		if card[1].name == deck.Rank.ACE.name:
			if self.hand_value + 11 > 21:
				self.hand_value += 1
			else:
				self.hand_value += 11
		else:
			self.hand_value += card[1].value

	def is_bust(self):
		return self.hand_value > 21

class Player(AbstractPlayer):
	def __init__(self, chips = 100):
		super().__init__()
		self.chips = chips

	def adjust_chips(self, chips, bet = False):
		if bet:
			if chips > self.chips:
				raise ValueError("Insufficient funds")
			self.chips -= chips
		else:
			self.chips += (2 * chips)
			print(f"Congratulations, you now have {self.chips} chips")

class Dealer(AbstractPlayer):
	def __str__(self):
		if len(self.hand) == 2:
			first = self.hand[0]
			return f"({first[0].name}:{first[1].name}), (***:***)"
		else:
			return super().__str__()
