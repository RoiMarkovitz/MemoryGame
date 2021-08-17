from tkinter import *
from tkinter import messagebox
import tkinter as tk

from views.BaseView import BaseView
from views.GameWindow import GameWindow
from constants import Constants
from objects.GameManager import GameManager
from objects.Player import Player
from Utils.WindowUtil import WindowUtil
from custom_widgets.PrimaryButton import PrimaryButton
from custom_widgets.TopicLabel import TopicLabel


class GameOptionsWindow(BaseView):
    """
    A singleton class used to handle the game options window.

    Attributes:
    instance (GameOptionsWindow): used to store instance of the singleton object.
    master (Tk): the root window object.
    """

    instance = None

    def __init__(self, master):
        if GameOptionsWindow.instance is not None:
            raise Exception('Can only have one options window at once!')
        else:
            GameOptionsWindow.instance = self
            self.master = master

            self.init_widgets()

    def start_game_window(self, difficulty):
        """
        Function starts the game window.
        Validates the player nickname entered.
        Closes game options window.
        Opens the game window.

        Parameters:
        difficulty (string): the difficulty of the game chosen by the player.
        """
        try:
            player = Player(self.nickname_stringVar.get())
        except Exception as e:
            self.activate_label_error(e)
            return

        # close current window
        self.master.destroy()
        # start root for the game window
        root = tk.Toplevel()
        WindowUtil.config_window(root, Constants.WINDOW_SIZE, False, 'Game',
                                 Constants.ICON_PATH, True, 'lavender')
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root))
        game_window = GameWindow(root, difficulty, player)
        self.reset_game_options_window()
        root.mainloop()

    def on_closing(self, root):
        """
        Function activated on window close.
        Validates if the user wants to close the window.
        If so, the window is being closed.
        Destroys the game singleton.
        Destroys the game options singleton.

        Parameters:
        root (Tk): the root window object.
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?", parent=root):
            root.destroy()
            GameManager.reset_game()
            self.reset_game_options_window()

    @staticmethod
    def reset_game_options_window():
        GameOptionsWindow.instance = None

    @staticmethod
    def get_instance():
        return GameOptionsWindow.instance

    def clear_text(self, event):
        event.widget.delete(0, "end")

    def init_widgets(self):
        # frame that will consist the topic in the window
        topic_frame = Frame(self.master)
        topic_frame.configure(bg='lavender')
        topic_frame.pack(pady=20)

        # frame that will consist the game options in the window
        options_frame = Frame(self.master)
        options_frame.configure(bg='lavender')
        options_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # create label widget for topic of the window
        topic_label = TopicLabel(topic_frame, text="Game Options").get_label()
        topic_label.pack()

        # define stringVar for nickname input
        self.nickname_stringVar = StringVar(options_frame, value="Type a nickname")
        # create entry widget for nickname, attach it to screen and bind mouse left click to it
        nickname_entry = Entry(options_frame, textvariable=self.nickname_stringVar,
                               width=30, font=('Ariel', 18))
        nickname_entry.bind("<Button-1>", self.clear_text)
        nickname_entry.grid(row=0, pady=25)

        # create game-start buttons custom_widgets and attach them to screen
        button_beginner = PrimaryButton(options_frame, "Beginner", 'green', 20,
                                        lambda: self.start_game_window("Beginner")).get_button()
        button_beginner.grid(row=1, pady=10)
        button_intermediate = PrimaryButton(options_frame, "Intermediate", "blue", 20,
                                            lambda: self.start_game_window("Intermediate")).get_button()
        button_intermediate.grid(row=2, pady=10)
        button_expert = PrimaryButton(options_frame, "Expert", "red", 20,
                                      lambda: self.start_game_window("Expert")).get_button()
        button_expert.grid(row=3, pady=10)

        # create label widget to show error
        self.label_error = Label(options_frame, text="", fg="red", bg='lavender', font=('Ariel', 18))
        self.label_error.grid(row=4, pady=10)
