from tkinter import *


class DataLabel(object):
    """
    A helper class used to create custom label widgets with pre-made characteristics.
    """

    def __init__(self, root, text):
        self.data_label = Label(root, text=text, font=('Ariel', 16), bg='lavender')

    def get_data_label(self):
        return self.data_label

