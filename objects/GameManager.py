import copy
from datetime import datetime
from Utils.FileUtil import FileUtil
from constants import Constants
from objects.Deck import Deck
from objects.GameState import GameState
from objects.Memento import *


class GameManager(object):
    """
    A singleton class used to manage the game.

    Attributes:
    instance (GameManager): used to store instance of the singleton object.
    levels (dict): stores the difficulty as key and the number of cards and undos as value.
    header (list of strings): stores the header values to store in the excel file.
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
    originator (Originator): creates and stores states in Memento objects.
    caretaker (CareTaker): responsible to restore object state from Memento.
    """

    instance = None
    levels = {'Beginner': [12, 2], 'Intermediate': [18, 4], 'Expert': [24, 6]}
    header = ["Nickname", "Score", "Moves", "Difficulty", "Max Streak", "Date"]

    def __init__(self, player, difficulty):
        if GameManager.instance is not None:
            raise Exception('Can only have one game at once!')
        else:
            GameManager.instance = self
            self.player = player
            self.moves = 0
            self.streak = 0
            self.max_streak = 0
            self.picked_card1 = None
            self.picked_card2 = None
            self.is_card1_picked = False
            self.is_card2_picked = False

            keys = GameManager.levels.keys()
            for level in keys:
                if level is difficulty:
                    self.difficulty = difficulty
                    self.undos = GameManager.levels[level][1]
                    self.deck = Deck(GameManager.levels[level][0])
                    self.matches_left = GameManager.levels[level][0] / 2
                    self.is_game_ended = False
                    break

            self.originator = Originator()
            self.caretaker = Caretaker()

    def play_round(self):
        """
        Function updates the game parameters based on the cards being played.

        Returns:
        success (bool): False if cards don't match, True if the cards do match.
        """
        success = False

        if not self.is_game_ended and self.are_two_cards_picked():
            if self.picked_card1.is_same_card_type(self.picked_card2):
                self.matches_left -= 1
                self.streak += 1
                self.player.increase_score(self.streak)
                if self.streak > self.max_streak:
                    self.max_streak = self.streak
                success = True
                if self.matches_left == 0:
                    self.end_game()
            else:
                self.streak = 0

            # reset cards
            self.is_card1_picked = False
            self.is_card2_picked = False

        return success

    def end_game(self):
        """
        Function in-charge of ending the game.
        Changing the is_game_ended parameter to True.
        Activates write_record_csv_file() function to write game results to file
        """
        self.is_game_ended = True
        self.write_record_csv_file()

    def are_two_cards_picked(self):
        return self.is_card1_picked and self.is_card2_picked

    def undo(self):
        if self.undos > 0:
            self.restore_game_state()
            self.undos -= 1
            return True
        else:
            return False

    def is_first_choice_in_game(self):
        return self.moves == 0 and self.picked_card1 is None

    def get_is_game_ended(self):
        return self.is_game_ended

    def get_is_card1_picked(self):
        return self.is_card1_picked

    def get_is_card2_picked(self):
        return self.is_card2_picked

    def get_number_of_cards(self):
        return GameManager.levels[self.difficulty][0]

    def get_moves(self):
        return self.moves

    def get_score(self):
        return self.player.get_score()

    def get_streak(self):
        return self.streak

    def get_max_streak(self):
        return self.max_streak

    def get_undos(self):
        return self.undos

    def get_picked_card1(self):
        return self.picked_card1

    def get_picked_card2(self):
        return self.picked_card2

    def set_picked_card1(self, card_index):
        self.picked_card1 = self.deck.flip_card(card_index)

    def set_picked_card2(self, card_index):
        self.picked_card2 = self.deck.flip_card(card_index)

    def pick_card(self, card_index):
        self.backup_game_state()
        self.moves += 1
        if not self.is_card1_picked:
            self.set_picked_card1(card_index)
            self.is_card1_picked = True
            return
        if not self.is_card2_picked:
            self.set_picked_card2(card_index)
            self.is_card2_picked = True

    def write_record_csv_file(self):
        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        record = [self.player.get_nickname(), self.player.get_score(), self.moves, self.difficulty,
                  self.get_max_streak(), date]
        FileUtil.write_record_csv_file(Constants.RECORDS_FILE_PATH, self.header, record)

    @staticmethod
    def reset_game():
        GameManager.instance = None

    @staticmethod
    def get_instance():
        return GameManager.instance

    # we backup two type of states: 1. when picking first card, two when picking second card and playing round
    def backup_game_state(self):
        game_state = GameState(self.moves, self.undos, self.streak, self.max_streak, self.deck,
                               self.picked_card1, self.picked_card2, self.is_game_ended,
                               copy.copy(self.player), self.difficulty, self.matches_left,
                               self.is_card1_picked, self.is_card2_picked)
        self.originator.set_state(game_state)
        self.caretaker.add_memento(self.originator.save_state_to_memento())

    def restore_game_state(self):
        self.originator.get_state_from_memento(self.caretaker.get_memento())
        game_state = self.originator.get_state()

        self.moves = game_state.get_moves()
        self.streak = game_state.get_streak()
        self.max_streak = game_state.get_max_streak()
        self.deck = game_state.get_deck()  
        self.picked_card1 = game_state.get_picked_card1()
        self.picked_card2 = game_state.get_picked_card2()
        self.is_game_ended = game_state.get_is_game_ended()
        self.player = game_state.get_player()
        self.difficulty = game_state.get_difficulty()
        self.matches_left = game_state.get_matches_left()
        self.is_card1_picked = game_state.get_is_card1_picked()
        self.is_card2_picked = game_state.get_is_card2_picked()
