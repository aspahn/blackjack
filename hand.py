import sys
import random
from deck import BasicDeck

class Hand():

    def __init__(self,num_decks):
        self.the_deck = BasicDeck(num_decks)
        self.open_spots = []
        x = 52*num_decks
        for i in range(x):
            self.open_spots.append(i)

    def pick_card(self):
        i = 0
        while True:
            print self.the_deck.print_card(i)
            i += 1
            break

h=Hand(int(sys.argv[1]))
h.pick_card()

