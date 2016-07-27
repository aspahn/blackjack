import sys
from deck import BasicDeck


class Player():
    def __init__(self, bet_spread_low, bet_spread_high):
        self.p_move = (" ")
        self.bet = 0
        self.bank = 100000
        self.betting_unit = bet_spread_low
        self.bet_max = bet_spread_high

    def player_move(self, auto, myHand=[], dealerHand=[]):
        if auto == False:
            self.p_move = raw_input("Do you want to hit or stand? (Enter H or S): ")
            print('')
            return self.p_move.upper()
        else:
            return self.player_move_auto(myHand, dealerHand)

    def player_move_auto(self, myHand=[], dealerHand=[]):
        total = 0
        num_aces = 0
        dealer_card = dealerHand[1]
        for i in myHand:
            if i > 10:
                total += 10
            elif i == 1:
                num_aces += 1
                total += 11
            else:
                total += i

        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1

        'use table for 9 - 16'
        user_table_array = [["HDDDDHHHHH"],
                            ["DDDDDDDDHH"],
                            ["DDDDDDDDDH"],
                            ["HHSSSHHHHH"],
                            ["SSSSSHHHHH"],
                            ["SSSSSHHHHH"],
                            ["SSSSSHHHHH"],
                            ["SSSSSHHHHH"]]

        'use table for 13 - 18 when there is an ace remaining'
        user_table_ace_array = [["HHHDDHHHHH"],
                                ["HHHDDHHHHH"],
                                ["HHDDDHHHHH"],
                                ["HHDDDHHHHH"],
                                ["HDDDDHHHHH"],
                                ["SDDDDSSHHH"]]

        'use table from http://www.hitorstand.net/strategy.php'
        if (1):
            if dealer_card > 9:
                offset = 8
            elif dealer_card == 1:
                offset = 9
            else:
                offset = dealer_card - 2

            if (num_aces == 0):
                index = total - 9
                if (total < 9):
                    return 'H'
                elif (total > 16):
                    return 'S'
                else:
                    line = user_table_array[index]
                    val = line[0][offset]
                    return val
            else:
                index = total - 13
                if (total < 13):
                    return 'H'
                elif (total > 18):
                    return 'S'
                else:
                    line = user_table_ace_array[index]
                    val = line[0][offset]
                    return val
        else:
            'Hit on soft 17'
            if (total == 17):
                if (num_aces > 0):
                    return 'H'
                else:
                    return 'S'
            elif total < 17:
                return 'H'
            else:
                return 'S'

    def player_bet(self, auto, card_count, cards_used=[]):
        if auto == False:
            while True:
                self.bet = int(raw_input("How much would you like to bet?: "))
                if self.bet > self.bank:
                    print("Sorry you don't have that much money. Please bet again.")
                else:
                    break
            # self.bank -= self.bet
            return self.bet
        else:
            if card_count == True:
                return self.player_bet_auto_card_count(cards_used)
            else:
                 return self.player_bet_auto()

    'http://www.blackjackgeeks.com/cardcounting/betting.php'
    'Table minimum is $5'
    def player_bet_auto_card_count(self, cards_used=[]):
        x = self.card_count_hi_lo(cards_used)
        if x < 2:
            self.bet = 5
        else:
            self.bet = self.betting_unit * x
        if self.bet > self.bet_max:
            self.bet = self.bet_max

        if (self.bet > self.bank):
            self.bet = self.bank

        # self.bank -= self.bet
        return self.bet

    def player_bet_auto(self):
        if self.bank < 50:
            self.bet = self.bank
        else:
            self.bet = 50
        # self.bank -= self.bet
        return self.bet

    def card_count_hi_lo(self, cards_used=[]):
        running_count = 0
        remaining_decks = ((self.num_decks * 52) - len(cards_used)) / 52
        true_count = 0
        for i in cards_used:
            if i in range(2, 7):
                running_count += 1
            elif i in range(7, 10):
                running_count += 0
            else:
                running_count += -1

        if remaining_decks > 1:
            'round up'
            true_count = ((running_count / remaining_decks) + .5)
        else:
            true_count = running_count

        return true_count


class Dealer():
    def __init__(self, num_decks):
        self.cards_used = []
        self.the_deck = BasicDeck(num_decks)
        self.total_player = []
        self.suits_player = []
        self.suits_dealer = []
        self.total_dealer = []
        self.deck_shuffles = 0
        self.card_suit = ""
        self.card_value = 0
        self.turn = 0
        self.cards_in_shoe = 52 * num_decks
        self.dealers_first_card = 0

    def player_card(self, num_decks, player, auto):
        if self.turn == 0 or self.turn == 2:
            self.pick_card(num_decks)
            self.cards_used.append(self.card_value)
            self.total_player.append(self.card_value)
            self.suits_player.append(self.card_suit)
            print("Player, this is your hand: ")
            self.the_deck.print_card(self.total_player, self.suits_player)
            print("This is your current score: " + str(self.player_score(num_decks)))
            print('')
            self.turn += 1
        elif self.turn == 4:
            if self.player_score(num_decks) == 21:
                print("Blackjack!")
                print("Here is the dealer's hand: ")
                self.the_deck.print_card(self.total_dealer, self.suits_dealer)
            else:
                while self.player_score(num_decks) < 22:
                    move = player.player_move(auto, self.total_player, self.total_dealer)
                    if move == 'S':
                        break
                    self.pick_card(num_decks)
                    self.cards_used.append(self.card_value)
                    self.total_player.append(self.card_value)
                    self.suits_player.append(self.card_suit)
                    print("Player, this is your hand: ")
                    self.the_deck.print_card(self.total_player, self.suits_player)
                    self.player_score(num_decks)

                    if move == 'D':
                        if player.bank > player.bet *2:
                            player.bet *= 2
                        break
                print("this is your score: " + str(self.player_score(num_decks)))
                print('')
                if self.player_score(num_decks) < 22:
                    self.turn += 1
                else:
                    print("Here is the dealer's hand: ")
                    self.the_deck.print_card(self.total_dealer, self.suits_dealer)
        else:
            pass

    def dealer_card(self, num_decks):
        if self.turn == 1:
            self.pick_card(num_decks)
            self.cards_used.append(self.card_value)
            self.total_dealer.append(self.card_value)
            self.suits_dealer.append(self.card_suit)
            print("This is the dealer's hand: ")
            self.the_deck.print_blank_card()
            print('')
            self.turn += 1
        elif self.turn == 3:
            print("This is the dealer's hand: ")
            self.pick_card(num_decks)
            self.cards_used.append(self.card_value)
            self.total_dealer.append(self.card_value)
            self.suits_dealer.append(self.card_suit)
            self.the_deck.print_dealer_2card(self.total_dealer, self.suits_dealer)
            print('')
            self.turn += 1
        elif self.turn == 5:
            if self.dealer_score(num_decks) == 21:
                print("Blackjack!")
                self.the_deck.print_card(self.total_dealer, self.suits_dealer)
            else:
                if self.dealer_score(num_decks) < 17:
                    while self.dealer_score(num_decks) < 17:
                        print("This is the dealer's hand: ")
                        self.pick_card(num_decks)
                        self.cards_used.append(self.card_value)
                        self.total_dealer.append(self.card_value)
                        self.suits_dealer.append(self.card_suit)
                        self.the_deck.print_card(self.total_dealer, self.suits_dealer)
                        self.turn += 1
                else:
                    self.the_deck.print_card(self.total_dealer, self.suits_dealer)
                print("This is the dealer's score: " + str(self.dealer_score(num_decks)))
                print('')
        else:
            pass

    def pick_card(self, num_decks):
        if self.cards_in_shoe > 0:
            self.cards_in_shoe -= 1
            self.card_value = self.the_deck.card_value(self.cards_in_shoe)
            self.card_suit = self.the_deck.card_suit(self.cards_in_shoe)
        else:
            self.reshuffle_deck(num_decks)
            pass

    def reshuffle_deck(self, num_decks):
        self.cards_in_shoe = 52 * num_decks
        self.the_deck.shuffle_deck()
        self.deck_shuffles += 1
        return self.deck_shuffles

    def player_score(self, num_decks):
        p_score = 0
        num_aces = 0
        for i in range(len(self.total_player)):
            if self.total_player[i] > 10:
                p_score += 10
            elif self.total_player[i] == 1:
                num_aces += 1
                p_score += 11
            else:
                p_score += self.total_player[i]
        while p_score > 21 and num_aces > 0:
            p_score -= 10
            num_aces -= 1
        return p_score

    def dealer_score(self, num_decks):
        d_score = 0
        num_aces = 0
        for i in range(len(self.total_dealer)):
            if self.total_dealer[i] > 10:
                d_score += 10
            elif self.total_dealer[i] == 1:
                d_score += 11
                num_aces += 1
            else:
                d_score += self.total_dealer[i]
        while d_score > 21 and num_aces > 0:
            d_score -= 10
            num_aces -= 1
        return d_score

    def new_hand(self):
        del self.suits_dealer[:]
        del self.suits_player[:]
        del self.total_dealer[:]
        del self.total_player[:]
        self.turn = 0
