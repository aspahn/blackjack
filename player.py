import sys
from deck import BasicDeck

class Player():

    def __init__(self):
        print("Hello welcome to Blackjack!")
        self.p_move = (" ")

    def player_move(self):
        self.p_move  = raw_input("Do you want to hit or stand? (Enter H or S): ")
        return self.p_move

class Dealer():

    def __init__(self, num_decks):
        self.the_player = Player()
        self.the_deck = BasicDeck(num_decks)
        self.total_player = []
        self.total_dealer = []
        self.card_value = 0
        self.open_spots = []
        for d in range (num_decks):
            for i in range(52):
                self.open_spots.append(i+1)

    def player_card(self,num_decks):
        if i ==  0 or i == 2:
            self.deal_card(num_decks)
            self.total_player.append(self.card_value)
        elif i == 4:
            if self.player_score(num_decks) == 21:
                print("Blackjack!")
            else:
                move = self.the_player.player_move()
                if  move  == 'h' or move == 'H':
                    self.deal_card(num_decks)
                    self.total_player.append(self.card_value)
                    self.player_score(num_decks)
                print("this is your score: " + str(self.player_score(num_decks)))
        else:
            pass

    def dealer_card(self,num_decks):
        if i == 1 or i == 3:
            self.deal_card(num_decks)
            self.total_dealer.append(self.card_value)
        elif i ==5:
            if self.dealer_score(num_decks) == 21:
                print("Blackjack!")
            else:
                while self.dealer_score(num_decks) < 17:
                    self.deal_card(num_decks)
                    self.total_dealer.append(self.card_value)
                print("This is the dealer's score: " + str(self.dealer_score(num_decks)))
        else:
            pass

    def deal_card(self,num_decks):
        if len(self.open_spots) > 0:
            x = self.open_spots[0]
            print self.the_deck.print_card(x)
            self.card_value =  self.the_deck.card_value(x)
            del self.open_spots[0]
        else:
            print("The deck is full")

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
                if d__score > 10:
                    d_score  += 1
                else:
                    d_score += 11
            else:
                d_score += self.total_dealer[i]
        return d_score


