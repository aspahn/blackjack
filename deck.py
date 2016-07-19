import sys
import random


class Deck(object):

    'comment out for no output'
    #CLUB = u'\u2660'
    #HEART = u'\u2665'
    #DIAMOND = u'\u2666'
    #SPADE = u'\u2663'

    'no ouput'
    CLUB = 'C'
    HEART = 'H'
    DIAMOND = "D"
    SPADE = "S"

    # Abstract

    # interface
    # print_card
    # shuffle
    # card_value
    # card_suit
    pass


class BasicDeck(Deck):
    def __init__(self, num_single_decks):
        self.deck = [" "] * (52 * num_single_decks)

        for d in range(num_single_decks):
            #populates shoe array
            for i in range(13):
                self.deck[i + 52 * d] = 'C' + str(i + 1)
                self.deck[i + 13 + 52 * d] = 'H' + str(i + 1)
                self.deck[i + 26 + 52 * d] = 'D' + str(i + 1)
                self.deck[i + 39 + 52 * d] = 'S' + str(i + 1)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_card(self, value, suit):

        self.print_horizontal(value)
        self.print_value_l(value)
        self.print_verticle(value)
        self.print_suit(suit)
        self.print_verticle(value)
        self.print_value_r(value)
        self.print_horizontal(value)

    def print_horizontal(self, value):
        for x in range(len(value)):
            print ("--------"),
            print ("   "),
        print ("")

    def print_value_l(self, value):
        for x in value:
            if x == 1:
                x = 'A'
            if x == 11:
                x = 'J'
            elif x == 12:
                x = 'Q'
            elif x == 13:
                x = 'K'
            else:
                pass
            print ("|"),
            print (str(x).ljust(2)),
            'print "%2d"%x,'
            print ("   |"),
            print ("  "),
        print ("")

    def print_value_r(self, value):
        for x in value:
            if x == 1:
                x = 'A'
            if x == 11:
                x = 'J'
            elif x == 12:
                x = 'Q'
            elif x == 13:
                x = 'K'
            else:
                pass
            print ("|   "),
            print ("%2s" % str(x)),
            print ("|"),
            print ("  "),
        print ("")

    def print_verticle(self, value):
        for x in range(len(value)):
            print ("|       |"),
            print ("  "),
        print ("")

    def print_suit(self, suit):
        for x in suit:
            print ("|  "),
            print (x),
            print ("  |"),
            print ("  "),
        print ("")

    def print_dealer_2card(self, value, suit):
        x = value[1]
        y = suit[1]
        if x == 1:
            x = 'A'
        if x == 11:
            x = 'J'
        elif x == 12:
            x = 'Q'
        elif x == 13:
            x = 'K'
        print("--------" + "     " + "--------")
        print("|" + "       " + "|" + "    " + "|"),
        print str(x).ljust(2),
        print "   " + "|"
        print("|" + "       " + "|" + "    " + "|" + "       " + "|")
        print("|" + "       " + "|" + "    " + "|" + "   " + y + "   " + "|")
        print("|" + "       " + "|" + "    " + "|" + "       " + "|")
        print("|" + "       " + "|" + "    " + "|" + "   "),
        print ("%2s" % str(x)),
        print ("|")
        print("---------" + "    " + "--------")

    def print_blank_card(self):
        print("--------")
        print("|" + "       " + "|")
        print("|" + "       " + "|")
        print("|" + "       " + "|")
        print("|" + "       " + "|")
        print("|" + "       " + "|")
        print("---------")

    def card_value(self, card_idx):
        """ returns number on card
        >>> b = BasicDeck(1)
        >>> b.card_value(2)
        3
        """
        return int(self.deck[card_idx][1:])

    def card_suit(self, card_idx):
        """ returns suit on card. C for club, H for heart, D for diamond, S for spade
        >>> b = BasicDeck(1)
        >>> b.card_suit(2)
        u'\u2660'
        """
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


