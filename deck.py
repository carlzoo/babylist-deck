from card import Card

class Deck:
    def __init__(self):
        """
        Encapsulates a list of Card objects
        
        :return: None
        """
        self.cards = []
        # initialize deck
        suits = ['Clubs', 'Diamonds', 'Hearts','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        """
        Shuffles the deck

        :return: None
        """
        pile_1 = self.cards[:len(self.cards)//2]
        pile_2 = self.cards[len(self.cards)//2:]
        new_pile = []
        pile_num = 1
        while len(pile_1)> 0 and len(pile_2) > 0:
            if pile_num == 1:
                new_pile.append(pile_1.pop())
            else:
                new_pile.append(pile_2.pop())
            pile_num *= -1

        while len(pile_1) > 0:
            new_pile.append(pile_1.pop())

        while len(pile_2) > 0:
            new_pile.append(pile_2.pop())

        self.cards = new_pile

    def deal(self):
        """
        Removes last card from self.cards

        :return: Card
        """
        return self.cards.pop()
