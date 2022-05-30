
from collections import namedtuple


class FrenchDeck:
    Card = namedtuple('Card',['rank','Suit'])
    ranks = [str(n) for n in range(2,11)]+['J','Q','K','A']
    suits = ['SPADES','HEARTS','DIAMONDS','CLUBS']

    def __init__(self) -> None:
        self._cards = [self.Card(rank,suit)for rank in self.ranks for suit in self.suits ]
    
    def print(self):
        print(self._cards)

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]


if __name__ == "__main__":
    cards = FrenchDeck()
    print(len(cards))
    print(cards[2])