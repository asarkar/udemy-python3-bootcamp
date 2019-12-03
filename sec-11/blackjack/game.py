import player
import deck

def main():
	play = "y"

	while play == "y":
		pl = player.Player()
		dealer = player.Dealer()

		d = deck.Deck()
		d.shuffle()

		# shuffle 2 cards each
		for card in d.deal(2):
			pl.hit(card)
		for card in d.deal(2):
			dealer.hit(card)

		# take bet
		bet = -1

		while bet < 0:
			try:
				bet = int(input("Please place your bet: "))
				pl.adjust_chips(bet, True)
			except ValueError:
				print("Bad input. Please try again")

		print(f"Player hand: {pl}")
		print(f"Dealer hand: {dealer}")

		# is blackjack?
		if pl.hand_value == 21:
			print("Blackjack, player wins!")
			pl.adjust_chips(bet, False)
			play = False

		if play:
			print(f"Player hand value: {pl.hand_value}")
			hit = input("Would you like to hit? [y/n]: ")

			# hit
			while hit == "y" and not pl.is_bust():
				pl.hit(d.deal()[0])
				print(f"Player hand: {pl}")
				print(f"Player hand value: {pl.hand_value}")
				if not pl.is_bust():
					hit = input("Would you like to hit? [y/n]: ")

			if pl.is_bust():
				print("Player is bust, dealer wins!")
				play = False
			else:
				print(f"Player chose to stand, value of hand: {pl.hand_value}")

			# hit
			while dealer.hand_value < 17:
				dealer.hit(d.deal()[0])
				print(f"Dealer hand: {dealer}")
				print(f"Dealer hand value: {dealer.hand_value}")

			if dealer.is_bust():
				print("Dealer is bust, player wins!")
				pl.adjust_chips(bet, False)
			elif dealer.hand_value <= pl.hand_value:
				print(f"Player wins, value of dealer's hand: {dealer.hand_value}")
				pl.adjust_chips(bet, False)
			else:
				print("Dealer wins")

		play = input("Would you like to play again? [y/n]: ")

if __name__== "__main__":
  main()
