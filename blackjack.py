import sys
from player import Dealer
import doctest

class BlackJack():

    def __init__(self,num_decks):
        self.the_dealer = Dealer(num_decks)

    def winner(self,num_decks):
        """check for winner

        >>> b = BlackJack(1)
        >>> b.winner(9)
        1

        """
        if self.the_dealer.player_score(num_decks) == 21:
            return 1
        elif self.the_dealer.dealer_score(num_decks) == 21:
            return -1
        elif self.the_dealer.dealer_score(num_decks) == 21 and self.the_dealer.player_score(num_decks) == 21:
            return 0
        elif (21-self.the_dealer.dealer_score(num_decks)) < 0:
            return 1
        elif (21-self.the_dealer.player_score(num_decks)) < 0:
            return -1
        elif (21-self.the_dealer.dealer_score(num_decks)) < (21-self.the_dealer.player_score(num_decks)):
            return -1
        elif (21-self.the_dealer.dealer_score(num_decks)) > (21-self.the_dealer.player_score(num_decks)):
            return 1
        elif (21-self.the_dealer.dealer_score(num_decks)) == (21-self.the_dealer.player_score(num_decks)):
            return 0
        else:
            pass

    def play(self,num_decks):
        self.the_turn = 0
        while self.the_turn < 6:
            self.the_dealer.player_card(num_decks)
            self.the_turn +=1
            self.the_dealer.dealer_card(num_decks)
            self.the_turn += 1
        if self.winner(num_decks) == 1:
            print("Congrats Player! You have won.")
        elif self.winner(num_decks) == -1:
            print("Sorry Player. You have lost.")
        else:
            print("The game has ended in a tie")

b = BlackJack(int(sys.argv[1]))
b.play(int(sys.argv[1]))


