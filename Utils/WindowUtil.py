from tkinter import *


class WindowUtil(object):
    """
    A helper class used to config windows with pre-made characteristics.
    """

    @staticmethod
    def config_window(root, window_size, is_resizable, title, icon_path, is_always_on_top, background_color):
        """
        Function used to config the window.

        Parameters:
        root (Tk): the root window object.
        window_size (string): the size of the window.
        is_resizable (bool): should window be resizeable.
        title (string): the title of the window.
        icon_path (string): the location of the icon in the file system.
        is_always_on_top (bool): should window always stay on top.
        background_color (string): the background color of the window.
        """
        root.geometry(window_size)
        if not is_resizable:
            root.resizable(0, 0)
        root.title(title)
        icon = PhotoImage(file=icon_path)
        root.iconphoto(False, icon)
        if is_always_on_top:
            root.wm_attributes('-topmost', True)
        root.configure(bg=background_color)
