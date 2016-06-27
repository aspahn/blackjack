import sys
import random

class Deck(object):

    CLUB =u'\u2660'
    HEART =u'\u2665'
    DIAMOND =u'\u2666'
    SPADE =u'\u2663'
    V =u'\u00A6'

    # Abstract

    #interface
    #print_card
    #shuffle
    #card_value
    #card_suit
    pass

class BasicDeck(Deck):

    def __init__(self, num_single_decks):
        self.deck = [" "] * (52*num_single_decks)

        for d in range(num_single_decks):
            for i in range(13):
                self.deck[i + 52*d] = 'C' + " " + str(i+1)
                self.deck[i + 52*d] = 'C' + str(i+1)
                self.deck[i+13 + 52*d] = 'H' + str(i+1)
                self.deck[i+26 + 52*d] = 'D' + str(i+1)
                self.deck[i+39 + 52*d] = 'S' + str(i+1)
        random.shuffle(self.deck)

    def print_card(self, card_idx):
        x = self.card_suit(card_idx)

        if self.card_value(card_idx) < 10:
            print("--------")
            print(Deck.V+  "%d      " + Deck.V)%(self.card_value(card_idx))
            print(Deck.V+ "       " + Deck.V)
            print(Deck.V+ "   " +  x  + "   "  + Deck.V)
            print(Deck.V+ "       " + Deck.V)
            print(Deck.V+ "      %d"   + Deck.V)%(self.card_value(card_idx))
            print("---------")
        else:
             print("-------")
             print(Deck.V+ "%d    " + Deck.V) %(self.card_value(card_idx))
             print(Deck.V+ "      " + Deck.V)
             print(Deck.V+ "  " +  x  + "   "  + Deck.V)
             print(Deck.V+ "      " + Deck.V)
             print(Deck.V+ "    %d" + Deck.V) %(self.card_value(card_idx))
             print("--------")


    def card_value(self, card_idx):
        return int(self.deck[card_idx][1:])

    def card_suit(self, card_idx):
        if self.deck[card_idx][0] == 'C':
            return Deck.CLUB
        elif self.deck[card_idx][0] == 'H':
            return Deck.HEART
        elif self.deck[card_idx][0] == 'D':
            return Deck.DIAMOND
        elif self.deck[card_idx][0] == 'S':
            return Deck.SPADE
        else:
            assert False, "Bad suit %s" % self.deck[card_idx][0]


d = BasicDeck(int(sys.argv[1]))
d.print_card(2)
