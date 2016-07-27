
#! /usr/bin/env python

import sys, os
from dealer_player import Dealer
from dealer_player import Player


class BlackJack():
    def __init__(self):
        self.the_dealer = Dealer(self.num_decks)
        self.the_player = Player(self.betting_unit, self.bet_max, self.num_decks)
        self.player_winnings = 0
        self.player_losings = 0
        self.the_turn = 0
        self.num_win = 0
        self.num_lose = 0
        self.num_tie = 0
        self.betting_unit = str(sys.argv[7])
        self.bet_max = str(sys.argv[6])
        self.repition = str(sys.argv[2])
        self.auto = str(sys.argv[3])
        self.card_count = str(argv[4])
        self.num_decks = str(sys.argv[1])
        self.ouput = str(sys.argv[5])
        self.stdoutTemp = sys.stdout

    def winner(self):
        if self.the_dealer.player_score(self.num_decks) == 21 and len(self.the_dealer.total_player) == 2 and \
                        self.the_dealer.dealer_score(self.num_decks) == 21 and len(self.the_dealer.total_dealer) == 2:
            return 0
        elif self.the_dealer.player_score(self.num_decks) == 21 and len(self.the_dealer.total_player) == 2:
            return 2
        elif (21 - self.the_dealer.player_score(self.num_decks)) < 0:
            return -1
        elif (21 - self.the_dealer.dealer_score(self.num_decks)) < 0:
            return 1
        elif (21 - self.the_dealer.dealer_score(self.num_decks)) == (21 - self.the_dealer.player_score(self.num_decks)):
            return 0
        elif (21 - self.the_dealer.dealer_score(self.num_decks)) < (21 - self.the_dealer.player_score(self.num_decks)):
            return -1
        elif (21 - self.the_dealer.dealer_score(self.num_decks)) > (21 - self.the_dealer.player_score(self.num_decks)):
            return 1
        else:
            pass

    def play(self):
        if self.output == False:
            sys.stdout = open('/dev/null', 'w')
            sys.stdout = open('nul', 'w')

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
        self.the_dealer.the_deck.shuffle_deck()
        while self.the_player.bank > 0 and num_hands < self.repition:
            self.the_dealer.new_hand()
            print('')
            print("This is currently how much money you have in your bank account: " + str(self.the_player.bank))
            print('')
            self.the_player.player_bet(self.auto, self.the_dealer.cards_used,self.card_count)
            print('')
            while self.the_turn < 6:
                self.the_dealer.player_card(self.num_decks, self.the_player, self.auto)
                self.the_turn += 1
                self.the_dealer.dealer_card(self.num_decks)
                self.the_turn += 1
            if self.winner() == 1:
                print("Congrats Player! You have won: " + str(self.the_player.bet))
                self.num_win += 1
                self.the_player.bank += self.the_player.bet
                self.player_winnings += self.the_player.bet
            elif self.winner() == 2:
                print("Congrats you have gotten blackjack! and won: " + str(self.the_player.bet * 1.5))
                self.num_win += 1
                self.the_player.bank += self.the_player.bet * (1.5)
                self.player_winnings += self.the_player.bet * (1.5)
            elif self.winner() == -1:
                print("Sorry Player. You have lost: " + str(self.the_player.bet))
                self.num_lose += 1
                self.the_player.bank -= self.the_player.bet
                self.player_losings += self.the_player.bet
            else:
                print("The game has ended in a tie")
                #self.the_player.bank += self.the_player.bet
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
        print("This is how many times the deck has been reshuffled: " + str(x))
        print("This is how many games you have won: " + str(self.num_win))
        print("This is how many games you lost: " + str(self.num_lose))
        print("This is how many games you tied: " + str(self.num_tie))
        print("This is how much money you have in your bank: " + str(self.the_player.bank))
        sys.exit()

    def display_player_money(self):
        print("This is how much money you have in your bank: " + str(self.the_player.bank))
        print('')
        print("This is how much money you have won: " + str(self.player_winnings))
        print('')
        print("This is how much money you have lost: " + str(self.player_losings))

if len(sys.argv) != 5:
    print("Welcome to blackjack help.\n In order to play you will need to enter the following in order: how many decks you would like to play with, how many hands will be played,whether you would like to card count, whether you would like an auto player or not, if you would like to see the ouput, and the max and min bets.\n For the number of decks you want to play with type -d and the number of decks you wish to play with.\n If you want this program to play with an automatic player type -a and True or False if you would like an interactive player.\n If you want this program to card count type -c and True or False if you don't want card counting. \n For the number of hands you like to be played type -r and the number of hands.\n If you would like to see the output of the game being played type -o and True or False if you don't want to see the game being played.\n To set the min bet type -mi and the min bet.\n To set the max bet type -ma and the max bet.")
else:
    b = BlackJack(int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    b.play()
