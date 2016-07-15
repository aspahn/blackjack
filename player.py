import sys
from deck import BasicDeck

class Player():

    def __init__(self):
        self.p_move = (" ")
        self.bet = 0
        self.bank = 1000
        self.the_dealer = Dealer()

    def player_move(self):
        self.p_move  = raw_input("Do you want to hit or stand? (Enter H or S): ")
        print('')
        return self.p_move

    def player_move_auto(self,myHand = []):
        total = 0
        for i in myHand:
            if i > 10:
                total += 10
            elif i == 1:
                if total > 10:
                    total += 1
                else:
                    total += 11
            else:
                total += i
        if total < 17:
            return 'H'
        else:
            return 'S'

    def player_bet(self):
         while True:
            self.bet = int(raw_input("How much would you like to bet?: "))
            if self.bet > self.bank:
                print("Sorry you don't have that much money. Please bet again.")
            else:
                break
         self.bank -= self.bet
         return self.bet

    def player_auto_bet(self):
        if self.bank < 25:
            self.bet = self.bank
        else:
            self.bet = 25
        self.bank -= self.bet
        return self.bet

    def card_count(self, cards = [],num_decks):
        remaining_decks = num_decks - self.the_dealer.reshuffle_deck()
        running_count = 0
        true_count = 0
        for i in cards:
            if i in range (2,7):
                running_count += 1
            elif i in range (7,10):
                running_count += 0
            else:
                running_count -= -1
        true_count = running_count/remaining_decks



class Dealer():

    def __init__(self, num_decks):
        self.the_player = Player()
        self.the_deck = BasicDeck(num_decks)
        self.cards_used = []
        self.total_player = []
        self.suits_player = []
        self.suits_dealer = []
        self.total_dealer = []
        self.deck_shuffles = 0
        self.card_suit = ""
        self.card_value = 0
        self.turn = 0
        self.open_spots = []
        self.dealers_first_card = 0
        for d in range (num_decks):
            for i in range(52):
                self.open_spots.append(i+1)

    def player_card(self,num_decks):
        if self.turn ==  0 or self.turn == 2:
            self.pick_card(num_decks)
            self.total_player.append(self.card_value)
            self.cards_used.appennd(self.card_value)
            self.suits_player.append(self.card_suit)
            print("Player, this is your hand: ")
            self.the_deck.print_card(self.total_player,self.suits_player)
            print("This is your current score: " + str(self.player_score(num_decks)))
            print('')
            self.turn +=1
        elif self.turn == 4:
            if self.player_score(num_decks) == 21:
                print("Blackjack!")
            else:
                move = self.the_player.player_move_auto()
                if  move  == 'h' or move == 'H':
                    self.pick_card(num_decks)
                    self.total_player.append(self.card_value)
                    self.cards_used.appennd(self.card_value)
                    self.suits_player.append(self.card_suit)
                    print("Player, this is your hand: ")
                    self.the_deck.print_card(self.total_player,self.suits_player)
                    self.player_score(num_decks)
                    self.turn +=1
                else:
                    self.turn +=1
                print("this is your score: " + str(self.player_score(num_decks)))
                print('')
        else:
            pass

    def dealer_card(self,num_decks):
        if self.turn == 1:
            self.pick_card(num_decks)
            self.total_dealer.append(self.card_value)
            self.cards_used.appennd(self.card_value)
            self.suits_dealer.append(self.card_suit)
            print("This is the dealer's hand: ")
            self.the_deck.print_blank_card()
            print('')
            self.turn +=1
        elif self.turn == 3:
            print("This is the dealer's hand: ")
            self.pick_card(num_decks)
            self.total_dealer.append(self.card_value)
            self.cards_used.appennd(self.card_value)
            self.suits_dealer.append(self.card_suit)
            self.the_deck.print_dealer_2card(self.total_dealer,self.suits_dealer)
            print('')
            self.turn +=1
        elif self.turn ==5:
            if self.dealer_score(num_decks) == 21:
                print("Blackjack!")
            else:
                while self.dealer_score(num_decks) < 17:
                    print("This is the dealer's hand: ")
                    self.pick_card(num_decks)
                    self.total_dealer.append(self.card_value)
                    self.cards_used.appennd(self.card_value)
                    self.suits_dealer.append(self.card_suit)
                    self.the_deck.print_card(self .total_dealer,self.suits_dealer)
                    self.turn +=1
                print("This is the dealer's score: " + str(self.dealer_score(num_decks)))
                print('')
        else:
            pass

    def pick_card(self,num_decks):
        while True:
            if len(self.open_spots) > 0:
                x = self.open_spots[0]
                self.card_value =  self.the_deck.card_value(x)
                self.card_suit = self.the_deck.card_suit(x)
                del self.open_spots[0]
                break
            else:
                self.reshuffle_deck(self)

    def reshuffle_deck(self):
        for d in range (num_decks):
            for i in range(52):
                self.open_spots.append(i+1)
        self.the_deck.shuffle_deck()
        self.deck_shuffles += 1
        return self.deck_shuffles

    def player_score(self,num_decks):
        p_score = 0
        for i in range(len(self.total_player)):
            if self.total_player[i] > 10:
                p_score += 10
            elif self.total_player[i] == 1:
                if p_score > 10:
                    p_score += 1
                else:
                    p_score+= 11
            else:
                p_score += self.total_player[i]
        return p_score

    def dealer_score(self,num_decks):
        d_score = 0
        for i in range(len(self.total_dealer)):
            if self.total_dealer[i] > 10:
                d_score += 10
            elif self.total_dealer[i] == 1:
                if d_score > 10:
                    d_score  += 1
                else:
                    d_score += 11
            else:
                d_score += self.total_dealer[i]
        return d_score

    def new_hand(self):
        del self.suits_dealer[:]
        del self.suits_player[:]
        del self.total_dealer[:]
        del self.total_player[:]
        self.turn = 0
