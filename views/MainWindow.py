from tkinter import *
import tkinter as tk

from views.BaseView import BaseView
from views.GameOptionsWindow import GameOptionsWindow
from views.ReportsWindow import ReportsWindow
from Utils.WindowUtil import WindowUtil
from constants import Constants
from objects.GameManager import GameManager
from custom_widgets.PrimaryButton import PrimaryButton
from custom_widgets.TopicLabel import TopicLabel


class MainWindow(BaseView):
    """
    A class used to handle the main window.

    Attributes:
    master (Tk): the root window object.
    """

    def __init__(self, master):
        self.master = master

        self.init_widgets()

    def start_options_window(self):
        """
        Function starts the options window.
        Checks if game window is already open.
        Checks if game options window is already open.
        Opens the game options window.
        """
        if GameManager.get_instance() is not None:
            self.activate_label_error('Can only have one game at once!')
            return

        if GameOptionsWindow.get_instance() is not None:
            GameOptionsWindow.get_instance().activate_label_error('Can only have one game options window at once!')
            return

        # start root for game options window
        root = tk.Toplevel()
        WindowUtil.config_window(root, Constants.WINDOW_SIZE, False, 'Game Options',
                                 Constants.ICON_PATH, True, 'lavender')
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root, 0))
        game_options_window = GameOptionsWindow(root)
        root.mainloop()

    def start_reports_window(self):
        """
        Function starts the reports window.
        Checks if reports window is already open.
        Opens the game reports window.
        """
        if ReportsWindow.get_instance() is not None:
            ReportsWindow.get_instance().activate_label_error('Can only display one reports window at once!')
            return

        # start root for records window
        root = tk.Toplevel()
        WindowUtil.config_window(root, Constants.WINDOW_SIZE, False, 'Reports Table',
                                 Constants.ICON_PATH, True, 'lavender')
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root, 1))
        records_window = ReportsWindow(root)
        root.mainloop()

    def on_closing(self, root, option):
        root.destroy()
        if option == 0:
            GameOptionsWindow.reset_game_options_window()
        else:
            ReportsWindow.reset_records_screen()

    def init_widgets(self):
        # frame that will consist the topic in the window
        topic_frame = Frame(self.master)
        topic_frame.configure(bg='lavender')
        topic_frame.pack(pady=20)

        # frame that will consist the buttons in the window
        buttons_frame = Frame(self.master)
        buttons_frame.configure(bg='lavender')
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # create label widget for topic of the window
        topic_label = TopicLabel(topic_frame, text="Memory Game").get_label()
        topic_label.pack()

        # create buttons custom_widgets and attach them to screen
        button_easy = PrimaryButton(buttons_frame, "New Game", 'white', 10, self.start_options_window).get_button()
        button_easy.grid(row=1, padx=5, pady=15)
        button_records = PrimaryButton(buttons_frame, "Reports", 'white', 10, self.start_reports_window).get_button()
        button_records.grid(row=2, padx=5, pady=15)

        # create label widget to show error
        self.label_error = Label(buttons_frame, text="", fg="red", bg='lavender', font=('Ariel', 18))
        self.label_error.grid(row=3, pady=10)
