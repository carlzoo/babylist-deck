class Card:
    def __init__(self, suit, rank):
	'''
	Creates a new card object

	:param suit: str
	:param rank: str
	'''
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
	'''
	Returns true if two cards have the same suit and rank
	False otherwise

	:return: bool
	'''
        return self.suit == other.suit and self.rank == other.rank

    def __repr__(self):
	'''
	Returns the string output of the card object

	:return: str
	'''
        return self.rank + " " + self.suit
