from . import player, deck


def main():
    play = "y"
    chips = 100

    while play == "y":
        pl = player.Player(chips)
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
                bet = int(input(f"Please place your bet (available {pl.chips} chips): "))
                pl.adjust_chips(bet, True)
            except ValueError:
                print("Bad input. Please try again")
                bet = -1

        print(f"Player hand: {pl}")
        print(f"Dealer hand: {dealer}")

        # is blackjack?
        if pl.hand_value == 21:
            print("Blackjack, player wins!")
            pl.adjust_chips(bet)
        else:
            print(f"Player hand value: {pl.hand_value}")
            hit = input("Would you like to hit? [y/n]: ")

            # hit
            while hit == "y" and pl.hand_value < 21:
                pl.hit(d.deal()[0])
                print(f"Player hand: {pl}")
                print(f"Player hand value: {pl.hand_value}")
                if pl.hand_value < 21:
                    hit = input("Would you like to hit? [y/n]: ")

            if pl.is_bust():
                print("Player is bust, dealer wins!")
            elif pl.hand_value == 21:
                print("Blackjack, player wins!")
                pl.adjust_chips(bet)
            else:
                print(f"Player chose to stand, value of hand: {pl.hand_value}")

            if pl.hand_value < 21:
                # hit
                while dealer.hand_value < 17:
                    dealer.hit(d.deal()[0])
                    print(f"Dealer hand: {dealer}")
                    print(f"Dealer hand value: {dealer.hand_value}")

                if dealer.is_bust():
                    print("Dealer is bust, player wins!")
                    pl.adjust_chips(bet)
                elif dealer.hand_value <= pl.hand_value:
                    print(f"Player wins, value of dealer's hand: {dealer.hand_value}")
                    pl.adjust_chips(bet)
                else:
                    print("Dealer wins")

        chips = pl.chips
        if chips > 0:
            play = input("\nWould you like to play again? [y/n]: ")
        else:
            print("Sorry, you have run out of funds and cannot play again")
            play = "n"


# sec-11$ python -m blackjack.game
main()
