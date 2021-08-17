
class Card(object):
    """
    A class used to represent a card.

    Attributes:
    idGenerator (int): generates id's for the cards.
    position (int): the index location of the card.
    card_type (string): the type of the card.
    id (int): the id of the card.
    """
    idGenerator = 0
    position = None

    def __init__(self, card_type):
        self.type = card_type
        self.id = Card.idGenerator
        Card.idGenerator += 1

    def is_same_card_type(self, card):
        """
        Function used to check if two cards are the same type.

        Parameters:
        card (Card): the card object being compared to self

        Returns:
        (bool): False if cards don't match, True if the cards do match.
        """
        return self.type == card.get_type()

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
