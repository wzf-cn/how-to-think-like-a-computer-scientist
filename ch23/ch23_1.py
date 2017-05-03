# -*- coding: utf-8 -*-
"""
Created on Thu May  4 00:05:22 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0
    
    def __ge__(self, other):
        return self.cmp(other) >= 0
    
    def __gt__(self, other):
        return self.cmp(other) > 0
    
    def __lt__(self, other):
        return self.cmp(other) < 0
    
    def __ne__(self, other):
        return self.cmp(other) != 0
    
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
        
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if abs(13/self.rank-6.5) > abs(13/other.rank-6.5): return 1
        if abs(13/self.rank-6.5) < abs(13/other.rank-6.5): return -1
        # Ranks are the same... it's a tie
        return 0

card1 = Card(1, 11)
card2 = Card(1, 1)
card3 = Card(1, 11)
print(card1 < card2)
print(card1 == card3)