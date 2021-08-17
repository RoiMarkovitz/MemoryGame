from tkinter import *


class PrimaryButton(object):
    """
    A helper class used to create custom button widgets with pre-made characteristics.
    """

    def __init__(self, root, text, color, width, command):
        self.button = Button(root, text=text, fg=color, bg='navy',
                             font=('Ariel', 24), width=width, command=command)

    def get_button(self):
        return self.button
