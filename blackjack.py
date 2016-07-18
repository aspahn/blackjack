#! /usr/bin/env python

import sys, os
from dealer_player import Dealer
from dealer_player import Player


class BlackJack():
    def __init__(self, num_decks, betting_unit, bet_max):
        self.the_dealer = Dealer(num_decks)
        self.the_player = Player(betting_unit, bet_max, num_decks)
        self.num_decks = num_decks
        self.betting_unit = betting_unit
        self.bet_max = bet_max
        self.player_winnings = 0
        self.player_losings = 0
        self.the_turn = 0
        self.num_win = 0
        self.num_lose = 0
        self.num_tie = 0
        self.stdoutTemp = sys.stdout

    def winner(self, num_decks):
        if self.the_dealer.player_score(num_decks) == 21 and len(self.the_dealer.total_player) == 2 and \
                        self.the_dealer.dealer_score(num_decks) == 21 and len(self.the_dealer.total_dealer) == 2:
            return 0
        elif self.the_dealer.player_score(num_decks) == 21 and len(self.the_dealer.total_player) == 2:
            return 2
        elif (21 - self.the_dealer.dealer_score(num_decks)) == (21 - self.the_dealer.player_score(num_decks)):
            return 0
        elif self.the_dealer.player_score(num_decks) == 21:
            return 1
        elif (21 - self.the_dealer.dealer_score(num_decks)) < 0:
            return 1
        elif (21 - self.the_dealer.player_score(num_decks)) < 0:
            return -1
        elif (21 - self.the_dealer.dealer_score(num_decks)) < (21 - self.the_dealer.player_score(num_decks)):
            return -1
        elif (21 - self.the_dealer.dealer_score(num_decks)) > (21 - self.the_dealer.player_score(num_decks)):
            return 1
        else:
            pass

    def play(self):
        'Turn off output'
        sys.stdout = open('/dev/null', 'w')

        print('')
        print("     "'*' * 5 + " Welcome to Blackjack!" + "     "'*' * 5)
        print('')
        print('')
        print(" " * 10 + "The game is very simple, but here are a few rules to get you started: ")
        print('')
        print(
        "The goal is to closer to 21 than the dealer. \nYou will be dealt two cards and then asked if you want to hit(get another card) or if you want to stand (stay with the cards you have). \nThe dealer than will take cards until his score is at least 17. Whoever is closer to 21 wins! \nBut be careful if you go over 21, you lose!")
        print('')
        print(
        "You will start with $100,000 in you bank and your winnings and bets will be subtracted or added to it. \nGood luck!")
        print('')
        num_hands = 0
        auto = True
        self.the_dealer.the_deck.shuffle_deck()
        while self.the_player.bank > 0 and num_hands < 10:
            self.the_dealer.new_hand()
            print('')
            print("This is currently how much money you have in your bank account: " + str(self.the_player.bank))
            print('')
            self.the_player.player_bet(auto, self.the_dealer.cards_used)
            print('')
            while self.the_turn < 6:
                self.the_dealer.player_card(self.num_decks, self.the_player, auto)
                self.the_turn += 1
                self.the_dealer.dealer_card(self.num_decks)
                self.the_turn += 1
            if self.winner(self.num_decks) == 1:
                print("Congrats Player! You have won.")
                self.num_win += 1
                self.the_player.bank += self.the_player.bet * 2
                self.player_winnings += self.the_player.bet
            elif self.winner(self.num_decks) == 2:
                print("Congrats you have gotten blackjack!")
                self.num_win += 1
                self.the_player.bank += self.the_player.bet * (2.5)
                self.player_winnings += self.the_player.bet * (1.5)
            elif self.winner(self.num_decks) == -1:
                print("Sorry Player. You have lost.")
                self.num_lose += 1
                self.player_losings += self.the_player.bet
            else:
                print("The game has ended in a tie")
                self.the_player.bank += self.the_player.bet
                self.num_tie += 1
            self.display_player_money()
            print('')
            print("This was your bet: " + str(self.the_player.bet))
            print("This is how many games you have won: " + str(self.num_win))
            print("This is how many games you lost: " + str(self.num_lose))
            print("This is how many games you tied: " + str(self.num_tie))
            if self.the_player.bank <= 0:
                print("Sorry you are broke. You can't play anymore")
                break
            elif auto == False:
                play_again = raw_input("Would you like to play again? Please enter Y or N?: ").upper()
                if play_again != 'Y':
                    break
            else:
                pass

            # reset hand state
            self.the_turn = 0
            num_hands += 1
        self.leave_game()

    def leave_game(self):
        sys.stdout = self.stdoutTemp
        x = self.the_dealer.deck_shuffles
        print('')*2
        print("This is how many times the deck has been reshuffled: " + str(x))
        print("This is the total number of  games you  won: " + str(self.num_win))
        print("This is the total number of  games you lost: " + str(self.num_lose))
        print("This is the total number of games  you tied: " + str(self.num_tie))
        print("This is how much money you have left in your bank: " + str(self.the_player.bank))
        sys.exit()

    def display_player_money(self):
        print("This is how much money you have in your bank: " + str(self.the_player.bank))
        print('')
        print("This is how much money you have won: " + str(self.player_winnings))
        print('')
        print("This is how much money you have lost: " + str(self.player_losings))


b = BlackJack(6, 25, 250)
b.play()
