from tkinter import *
from tkinter import messagebox
from constants import Constants
from custom_widgets.DataLabel import DataLabel
from objects.GameManager import GameManager
from custom_widgets.DataBox import DataBox
from views.BaseView import BaseView


class GameWindow(BaseView):
    """
    A singleton class used to handle the game window.

    Attributes:
    CARD_W_RATIO (int): the width ratio of the card images.
    CARD_H_RATIO (int): the height ratio of the card images.
    master (Tk): the root window object.
    picked_card1 (Card): the current first picked card object in the round.
    picked_card2 (Card): the current second picked card object in the round.
    card_buttons (list of Buttons): list of buttons attached to the card images
    """
    CARD_W_RATIO = 5
    CARD_H_RATIO = 5

    def __init__(self, master, difficulty, player):
        self.master = master
        self.game = GameManager(player, difficulty)
        self.picked_card1 = self.game.get_picked_card1()
        self.picked_card2 = self.game.get_picked_card2()
        self.card_buttons = []

        self.init_widgets()

        self.is_undo_button_disabled()

    def flip_card(self, index):
        """
        Function flips a card. when two cards are flipped activates update_round_status function.

        Attributes:
        index (int): the index location of the button image of the card.
        """
        # pick a card to flip
        self.game.pick_card(index)

        self.update_moves()
        self.is_undo_button_disabled()

        # store the card in picked_card1 or picked_card2
        path = Constants.PATH_CARD
        if self.game.is_card1_picked and not self.game.is_card2_picked:
            self.picked_card1 = self.game.get_picked_card1()
            path += self.picked_card1.get_type() + ".png"
            #print("card1: " + self.picked_card1.get_type() + str(self.picked_card1.get_id()))

        if self.game.is_card2_picked:
            self.picked_card2 = self.game.get_picked_card2()
            path += self.picked_card2.get_type() + ".png"
            #print("card2: " + self.picked_card2.get_type() + str(self.picked_card2.get_id()))
        # place card image to screen
        self.switch_image_button(self.card_buttons[index], path, self.CARD_W_RATIO,
                                 self.CARD_H_RATIO, 'normal', 'sunken', 'none')

        if self.game.are_two_cards_picked():
            self.update_round_status()

    def update_round_status(self):
        """
        Function presents the round results on-screen.
        """
        result = self.game.play_round()
        self.update_streak()
        if result:
            self.card_buttons[self.picked_card1.get_position()].configure(state=DISABLED)
            self.card_buttons[self.picked_card2.get_position()].configure(state=DISABLED)
            self.update_score()
            self.update_max_streak()
            if self.game.get_is_game_ended():
                self.is_undo_button_disabled()
        else:
            messagebox.showinfo("Incorrect", "Memorize the cards! press enter when ready.", parent=self.master)
            # hide both cards and make them clickable
            card1_index = self.picked_card1.get_position()
            self.switch_image_button(self.card_buttons[card1_index], Constants.PATH_BACK_CARD, self.CARD_W_RATIO,
                                     self.CARD_H_RATIO, 'normal', 'raised', lambda c=card1_index: self.flip_card(c))

            card2_index = self.picked_card2.get_position()
            self.switch_image_button(self.card_buttons[card2_index], Constants.PATH_BACK_CARD, self.CARD_W_RATIO,
                                     self.CARD_H_RATIO, 'normal', 'raised', lambda c=card2_index: self.flip_card(c))

    def switch_image_button(self, button, path, w_ratio, h_ratio, state, relief, command):
        # Photoimage is built-in method used to store images
        photo = PhotoImage(file=path).subsample(w_ratio, h_ratio)
        self.photo = photo
        # keep reference of the photo, so it wont be garbage collected
        button.image = self.photo
        # updates the configuration properties of the button
        button.configure(image=photo, state=state, relief=relief, command=command)

    def undo_move(self):
        """
        Function presents the last move state on-screen.
        """
        if self.game.undo():
            self.update_undos()
            self.update_score()
            self.update_moves()
            self.update_streak()
            self.update_max_streak()

            if not self.game.get_is_card1_picked() and not self.game.get_is_card2_picked():
                # case 1 - state restored to two hidden cards
                # need to hide card1 that is showing on screen (card2 is hidden already)
                # ('case 1 - state restored to two hidden cards ')
                # print('need to hide card1 that is showing on screen (card2 is hidden already)')
                card1_index = self.picked_card1.get_position()
                self.switch_image_button(self.card_buttons[card1_index], Constants.PATH_BACK_CARD,
                                         self.CARD_W_RATIO, self.CARD_H_RATIO, 'normal', 'raised',
                                         lambda c=card1_index: self.flip_card(c))

            elif self.game.get_is_card1_picked() and not self.game.get_is_card2_picked():
                if self.card_buttons[self.picked_card1.get_position()]['state'] == DISABLED \
                        and self.card_buttons[self.picked_card2.get_position()]['state'] == DISABLED:
                    # case 2.2 - restore from match of two cards
                    # state restored to first card shown and second card hidden
                    # need to show card1 and hide card2
                    # print('case 2.2 - restore from match of two cards')
                    # print('state restored to first card shown and second card hidden')
                    # print("need to show card1 and hide card2")
                    picked_card1_index = self.picked_card1.get_position()
                    path = Constants.PATH_CARD + self.picked_card1.get_type() + ".png"
                    # show card 1
                    self.switch_image_button(self.card_buttons[picked_card1_index], path,
                                             self.CARD_W_RATIO, self.CARD_H_RATIO, 'normal', 'sunken', 'none')
                    # hide card 2
                    picked_card2_index = self.picked_card2.get_position()
                    self.switch_image_button(self.card_buttons[picked_card2_index], Constants.PATH_BACK_CARD,
                                             self.CARD_W_RATIO, self.CARD_H_RATIO, 'normal', 'raised',
                                             lambda c=picked_card2_index: self.flip_card(c))
                else:
                    # case 2.1 - regular restore. not a match
                    # state restored to first card shown and second card hidden
                    # need to show card 1 (card2 is hidden already)
                    # print('case 2.1 - regular restore. not a match')
                    # print('state restored to first card shown and second card hidden')
                    # print('need to show card 1 (card2 is hidden already)')
                    picked_card1_index = self.picked_card1.get_position()
                    path = Constants.PATH_CARD + self.picked_card1.get_type() + ".png"
                    self.switch_image_button(self.card_buttons[picked_card1_index], path, self.CARD_W_RATIO,
                                             self.CARD_H_RATIO, 'normal', 'sunken', 'none')

            # update cards in view with the restored cards
            self.picked_card1 = self.game.get_picked_card1()
            self.picked_card2 = self.game.get_picked_card2()

    def update_undos(self):
        self.undos_stringVar.set(str(self.game.get_undos()))
        self.is_undo_button_disabled()

    def is_undo_button_disabled(self):
        """
        Function checks if the undo button should be disabled.
        """
        if self.game.is_first_choice_in_game() or self.game.get_undos() == 0\
                or self.game.get_is_game_ended() is True:
            self.undo_button.configure(state=DISABLED)
        else:
            self.undo_button.configure(state=NORMAL)

    def update_score(self):
        self.score_stringVar.set(str(self.game.get_score()))

    def update_moves(self):
        self.moves_stringVar.set(str(self.game.get_moves()))

    def update_streak(self):
        self.streak_stringVar.set(str(self.game.get_streak()))

    def update_max_streak(self):
        self.max_streak_stringVar.set(str(self.game.get_max_streak()))

    def end_game(self):
        GameManager.reset_game()
        self.master.destroy()

    def init_widgets(self):
        # frame that will consist of all the cards
        cards_frame = Frame(self.master, pady=5)
        cards_frame.configure(bg='lavender')
        cards_frame.pack()

        # frame that will consist of the status of the game parameters
        status_frame = Frame(self.master)
        status_frame.configure(bg='lavender')
        status_frame.pack()

        # get photo of back card (hidden)
        self.photo = PhotoImage(file=Constants.PATH_BACK_CARD).subsample(self.CARD_W_RATIO, self.CARD_H_RATIO)

        # init cards as hidden
        for i in range(0, self.game.get_number_of_cards()):
            self.card_buttons.append(Button(cards_frame, image=self.photo, command=lambda c=i: self.flip_card(c)))
            self.card_buttons[i].image = self.photo  # keep reference, so it wont be garbage collected
            self.card_buttons[i].grid(row=int(i / 6), column=i % 6, padx=4, pady=4)

        # create undo button widget and attach it to screen
        self.undo_button = Button(status_frame, text="Undo", fg="white", bg="navy",
                                  command=self.undo_move, font=('Ariel', 16))
        self.undo_button.grid(row=0, columnspan=5, pady=12)

        # define stringVar for the game parameters
        self.score_stringVar = StringVar(status_frame, value=str(self.game.get_score()))
        self.moves_stringVar = StringVar(status_frame, value=str(self.game.get_moves()))
        self.undos_stringVar = StringVar(status_frame, value=str(self.game.get_undos()))
        self.streak_stringVar = StringVar(status_frame, value=str(self.game.get_streak()))
        self.max_streak_stringVar = StringVar(status_frame, value=str(self.game.get_max_streak()))

        # create disabled entry custom_widgets for the game parameters and attach them to screen
        score_box = DataBox(status_frame, self.score_stringVar).get_data_box()
        score_box.grid(row=1, column=0, padx=5, pady=0)
        moves_box = DataBox(status_frame, self.moves_stringVar).get_data_box()
        moves_box.grid(row=1, column=1, padx=5, pady=0)
        undos_box = DataBox(status_frame, self.undos_stringVar).get_data_box()
        undos_box.grid(row=1, column=2, padx=5, pady=0)
        streak_box = DataBox(status_frame, self.streak_stringVar).get_data_box()
        streak_box.grid(row=1, column=3, padx=5, pady=0)
        max_streak_box = DataBox(status_frame, self.max_streak_stringVar).get_data_box()
        max_streak_box.grid(row=1, column=4, padx=5, pady=0)

        # create label custom_widgets for the game parameters and attach them to screen
        score_label = DataLabel(status_frame, text="Score").get_data_label()
        score_label.grid(row=2, column=0, padx=5)
        moves_label = DataLabel(status_frame, text="Moves").get_data_label()
        moves_label.grid(row=2, column=1, padx=5)
        undos_label = DataLabel(status_frame, text="Undos left").get_data_label()
        undos_label.grid(row=2, column=2, padx=5)
        streak_label = DataLabel(status_frame, text="Streak").get_data_label()
        streak_label.grid(row=2, column=3, padx=5)
        max_streak_label = DataLabel(status_frame, text="Max streak").get_data_label()
        max_streak_label.grid(row=2, column=4, padx=5)

        # create return to main menu button widget and attach it to screen
        button_return_main_menu = Button(status_frame, text="Return to menu", fg="white",
                                         bg="green", command=self.end_game, font=('Ariel', 16))
        button_return_main_menu.grid(row=0, pady=12)
