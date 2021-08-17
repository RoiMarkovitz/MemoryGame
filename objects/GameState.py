
class GameState(object):
    """
    A class used to represent a state of the game.

    Attributes:
    player (Player): the player object playing the game.
    moves (int): the number of current moves in the game.
    streak (int): the number of sequenced card matches.
    streak_max (int): the maximum sequenced card matches.
    picked_card1 (Card): the current first picked card object in the round.
    picked_card2 (Card): the current second picked card object in the round.
    is_card1_picked (bool): tracks if card1 is picked or not in the current round.
    is_card2_picked (bool): tracks if card2 is picked or not in the current round.
    difficulty (string): the difficulty of the game.
    undos (int): the number of undos left to use.
    deck (Deck): the deck of cards.
    matches_left (int): tracks how many card matches are left in the game.
    is_game_ended (bool): tracks if game ended.
    """

    def __init__(self, moves, undos, streak, max_streak, deck, picked_card1, picked_card2,
                 is_game_ended, player, difficulty, matches_left, is_card1_picked, is_card2_picked):
        self.moves = moves
        self.undos = undos
        self.streak = streak
        self.max_streak = max_streak
        self.deck = deck
        self.picked_card1 = picked_card1
        self.picked_card2 = picked_card2
        self.is_game_ended = is_game_ended
        self.player = player
        self.difficulty = difficulty
        self.matches_left = matches_left
        self.is_card1_picked = is_card1_picked
        self.is_card2_picked = is_card2_picked

    def get_moves(self):
        return self.moves

    def get_streak(self):
        return self.streak

    def get_max_streak(self):
        return self.max_streak

    def get_deck(self):
        return self.deck

    def get_picked_card1(self):
        return self.picked_card1

    def get_picked_card2(self):
        return self.picked_card2

    def get_is_game_ended(self):
        return self.is_game_ended

    def get_player(self):
        return self.player

    def get_difficulty(self):
        return self.difficulty

    def get_matches_left(self):
        return self.matches_left

    def get_is_card1_picked(self):
        return self.is_card1_picked

    def get_is_card2_picked(self):
        return self.is_card2_picked
