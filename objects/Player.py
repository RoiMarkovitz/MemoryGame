class Player(object):
    """
    A class used to represent a player.

    Attributes:
    MAX_NICKNAME_LENGTH (int): the maximum characters allowed in a nickname.
    MIN_NICKNAME_LENGTH (int): the minimum characters allowed in a nickname.
    NICKNAME_ERROR_MESSAGE (string): the error message when user entered invalid nickname.
    nickname (string): the nickname of the player
    score (int): the current score of the player
    """

    MAX_NICKNAME_LENGTH = 20
    MIN_NICKNAME_LENGTH = 1
    NICKNAME_ERROR_MESSAGE = "Nickname must be between 1 to 20 characters"

    def __init__(self, nickname):
        if not self.is_nickname_correct(nickname):
            raise Exception(self.NICKNAME_ERROR_MESSAGE)
        self.nickname = nickname
        self.score = 0

    def get_nickname(self):
        return self.nickname

    def get_score(self):
        return self.score

    def increase_score(self, points):
        """
        Function used to increase the score of the player.

        Parameters:
        points (int): the number of points to add to score parameter.
        """
        self.score += points

    @staticmethod
    def is_nickname_correct(nickname):
        """
        Function used to validate if nickname is correct.

        Parameters:
        nickname (string): the nickname to validate.

        Returns:
        (bool): True if nickname is valid, False if nickname is not valid.
        """
        return Player.MAX_NICKNAME_LENGTH >= len(nickname) >= Player.MIN_NICKNAME_LENGTH
