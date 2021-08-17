from objects.Card import Card
import random


class Deck(object):
    """
    A class used to represent a deck.

    Attributes:
    card_types (tuple of strings): stores the card types.
    deck (list of cards): stores the cards.
    """

    card_types = ('acorn', 'moon', 'bee', 'tree', 'mushroom',
                  'world', 'leaf', 'tulip', 'cloud', 'sun',
                  'ladybug', 'water', 'snow', 'fish', 'fruittree')

    def __init__(self, size):
        self.card_types = tuple(random.sample(self.card_types, len(self.card_types)))
        self.deck = []
        i = 0
        while i < size / 2:
            self.deck.append(Card(self.card_types[i]))
            self.deck.append(Card(self.card_types[i]))
            i += 1

        random.shuffle(self.deck)

        for i in range(0, len(self.deck)):
            self.deck[i].set_position(i)

    def get_deck(self):
        return self.deck

    def flip_card(self, index):
        """
        Function used to retrieve a card from the deck.

        Parameters:
        index (int): the position of the card object

        Returns:
        (Card): the card object in the indexed position
        """
        return self.deck[index]
