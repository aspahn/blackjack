#! /usr/bin/env python

import sys, os
import argparse
from work_player import Dealer
from work_player import Player


class BlackJack():
    def __init__(self, num_decks, betting_unit, bet_max,output, hands, autoPlay, countCards, bank):
        self.the_dealer = Dealer(num_decks, output)
        self.the_player = Player(betting_unit, bet_max, num_decks, bank)
        self.num_decks = num_decks
        self.betting_unit = betting_unit
        self.bank = bank
        self.bet_max = bet_max
        self.output = output
        self.hands = hands
        self.autoPlay = autoPlay
        self.countCards = countCards
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
        # sys.stdout = open('/dev/null', 'w')
        if (self.output == False):
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
        "You will start with $" + str(self.bank) + " in your bank and your winnings and bets will be subtracted or added to it. \nGood luck!")
        print('')
        num_hands = 0
        self.the_dealer.the_deck.shuffle_deck()
        while self.the_player.bank > 0 and num_hands < self.hands:
            self.the_dealer.new_hand()
            print('')
            print("This is currently how much money you have in your bank account: " + str(self.the_player.bank))
            print('')
            self.the_player.player_bet(self.autoPlay, self.countCards, self.the_dealer.cards_used)
            print('')
            while self.the_turn < 6:
                self.the_dealer.player_card(self.num_decks, self.the_player, self.autoPlay)
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
            elif self.autoPlay == False:
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

parser = argparse.ArgumentParser(description='Blackjack')
parser.add_argument('-a', action='store_true', dest='auto', default=False, help='set the player moves to automatic')
parser.add_argument('-b', action='store', dest='bank', default=100000, help='how much money the player starts with')
parser.add_argument('-c', action='store_true', dest='count', default=False, help='use card counting to determine the bets')
parser.add_argument('-d', action='store', dest='decks', default=1, help='set the number of decks to use')
parser.add_argument('-m', action='store', dest='max', default=250, help='the maximum bet for the player')
parser.add_argument('-o', action='store_false', dest='output', default=True, help='turn the output off')
parser.add_argument('-p', action='store', dest='hands', default=5, help='the number of hands to play')
parser.add_argument('-u', action='store', dest='unit', default=25, help='the betting unit used in card counting')
parser.add_argument('--version', action='version', version='1.0')
args = parser.parse_args()

b = BlackJack(int(args.decks), int(args.unit), int(args.max), bool(args.output), int(args.hands), bool(args.auto), bool(args.count), int(args.bank))
b.play()
