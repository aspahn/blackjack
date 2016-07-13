#! /usr/bin/env python

import sys
from player import Dealer
from player import Player

class BlackJack():

    def __init__(self,num_decks):
        self.the_dealer = Dealer(num_decks)
        self.the_player = Player()
        self.player_bank = 1000
        self.player_winnings = 0
        self.player_bets = 0
        self.bet = 0
        self.the_turn = 0

    def winner(self,num_decks):
        if self.the_dealer.player_score(num_decks) == 21:
            return 2
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
        print('')
        print("     "'*' * 5 + " Welcome to Blackjack!" + "     "'*' * 5)
        print('')
        print('')
        print(" "*10 + "The game is very simple, but here are a few rules to get you started: ")
        print('')
        print("The goal is to closer to 21 than the dealer. \nYou will be dealt two cards and then asked if you want to hit(get another card) or if you want to stand (stay with the cards you have). \nThe dealer than will take cards until his score is at least 17. Whoever is closer to 21 wins! \nBut be careful if you go over 21, you lose!")
        print('')
        print("You will start with $1000 in you bank and your winnings and bets will be subtracted or added to it. \nGood luck!")
        print('')
        while self.player_bank > 0:
            print('')
            print("This is currently how much money you have in your bank account: " + str(self.player_bank))
            print('')
            self.bet = int(raw_input("How much would you like to bet: "))
            print('')
            while self.the_turn < 6:
                self.the_dealer.player_card(num_decks)
                self.the_turn +=1
                self.the_dealer.dealer_card(num_decks)
                self.the_turn += 1
            if self.winner(num_decks) == 1 or self.winner(num_decks) == 2:
                print("Congrats Player! You have won.")
            elif self.winner(num_decks) == -1:
                print("Sorry Player. You have lost.")
            else:
                print("The game has ended in a tie")
            self.player_money(num_decks)
            print('')
            play_again = raw_input("Would you like to play again? Please enter Y or N?: ").upper()
            if play_again != 'Y':
                sys.exit()

            # Need to reset all hand state
            self.the_turn = 0

    def player_money(self,num_decks):
        self.player_bets +=  self.bet
        self.player_bank -= self.bet
        if self.winner(num_decks)== 2:
            win = self.bet + (1.5*self.bet)
        elif self.winner(num_decks) == 1:
            win = 2*self.bet
        else:
            win = 0
        self.player_winnings += win
        self.player_bank += win
        print('')*2
        print("This is how much money you have in your bank: " + str(self.player_bank))
        print('')
        print("This is how much money you have won: " + str(self.player_winnings))
        print('')
        print("This is how much money you have bet: " + str(self.player_bets))


b = BlackJack(int(sys.argv[1]))
b.play(int(sys.argv[1]))


