from tkinter import *


class DataBox(object):
    """
    A helper class used to create custom data boxes widgets with pre-made characteristics.
    """

    def __init__(self, root, text_variable):
        self.data_box = Entry(root, textvariable=text_variable, state=DISABLED,
                              font=('Ariel', 16, 'bold'), width=10, justify=CENTER)

    def get_data_box(self):
        return self.data_box
