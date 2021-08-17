from tkinter import *
from constants import Constants
from views.MainWindow import MainWindow
from Utils.WindowUtil import WindowUtil

# Created by Roi Markovitz

"""
Program Entry Point
Opens Main Window of the game
"""

root = Tk()  # creating a blank window
WindowUtil.config_window(root, Constants.WINDOW_SIZE, False, 'Main Menu', Constants.ICON_PATH, True, 'lavender')
main_window = MainWindow(root)
root.mainloop()  # infinite loop to display custom_widgets
