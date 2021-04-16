'''
Author: Ful Chou
Date: 2021-03-19 13:27:32
LastEditors: Ful Chou
LastEditTime: 2021-03-19 13:48:32
FilePath: /python advance/python_data_model.py
Description: What this document does
'''

import collections
Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self) -> None:
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._card)
    def __getitem__(self,position):
        return self._card[position]
    
t1 = Card('7','diamonds')
print(t1)
deck = FrenchDeck()
print(len(deck))
for card in deck:
    print(card)