
class BaseView(object):
    """
    A base class for the derived view (window) classes with shared functions

    Attributes:
    master (Tk): the root window object.
    label_error (Label): label for presenting errors.
    master (Tk):
    """
    master = None
    label_error = None

    def activate_label_error(self, text):
        """
        Function used to show error text in a label.
        The text of the label is changed.
        Then, the after method waits 3000 milliseconds to start the clear_error_label function

        Parameters:
        text (string): the root window object.
        self.label_error (Label): the label object
        """
        self.label_error['text'] = text
        self.master.after(3000, self.clear_error_label)

    def clear_error_label(self):
        """
        Function used to clear error text from a label.
        """
        self.label_error['text'] = ''
