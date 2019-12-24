from blackjack import player, deck
import pytest

class TestPlayer:

	def test_init_player(self):
		p1 = player.Player()
		assert p1.chips == 100
		assert p1.hand_value == 0

		p2 = player.Player(50)
		assert p2.chips == 50
		assert p2.hand_value == 0

	def test_init_dealer(self):
		d = player.Dealer()
		assert d.hand_value == 0

	def test_hit(self):
		p = player.Player()
		assert p.hand_value == 0

		p.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		assert p.hand_value == 2
		assert not p.is_bust()

		p.hit((deck.Suit.HEARTS, deck.Rank.ACE))
		assert p.hand_value == 13
		assert not p.is_bust()

		p.hit((deck.Suit.HEARTS, deck.Rank.ACE))
		assert p.hand_value == 14
		assert not p.is_bust()

		p.hit((deck.Suit.HEARTS, deck.Rank.KING))
		assert p.hand_value == 24
		assert p.is_bust()

	def test_adjust_chips(self):
		p = player.Player(100)

		p.adjust_chips(1, False)
		assert p.chips == 102

		p.adjust_chips(1, True)
		assert p.chips == 101

		with pytest.raises(ValueError):
			p.adjust_chips(102, True)

	def test_str(self):
		p = player.Player()
		p.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		p.hit((deck.Suit.HEARTS, deck.Rank.KING))
		assert str(p) == "(HEARTS:TWO), (HEARTS:TEN)"

		d = player.Dealer()
		d.hit((deck.Suit.HEARTS, deck.Rank.TWO))
		d.hit((deck.Suit.HEARTS, deck.Rank.KING))
		assert str(d) == "(HEARTS:TWO), (***:***)"

		d.hit((deck.Suit.HEARTS, deck.Rank.THREE))
		assert str(d) == "(HEARTS:TWO), (HEARTS:TEN), (HEARTS:THREE)"
