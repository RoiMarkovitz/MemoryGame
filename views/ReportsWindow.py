from tkinter import ttk
from Utils.FileUtil import FileUtil
from tkinter import *

from constants import Constants
from custom_widgets.TopicLabel import TopicLabel
from views.BaseView import BaseView


class ReportsWindow(BaseView):
    """
    A singleton class used to handle the reports window.

    Attributes:
    instance (ReportsWindow): used to store instance of the singleton object.
    master (Tk): the root window object.
    records (list of strings): contains the rows from the excel file.
    player_records (list of strings): contains the rows related to player
    """
    instance = None

    def __init__(self, master):
        if ReportsWindow.instance is not None:
            raise Exception('Can only have one records screen at once!')
        else:
            ReportsWindow.instance = self

        self.master = master
        self.records = FileUtil.read_record_csv_file(Constants.RECORDS_FILE_PATH)
        self.player_records = []

        self.init_widgets()

        self.show_all_reports()

    def show_all_reports(self):
        """
        Function shows all the reports from the csv file.
        """
        self.remove_all_records()
        for i, record in enumerate(self.records):
            if i == 0:  # ignore header
                continue
            # populate table
            self.records_tree.insert(parent='', index='end', iid=i, text="",
                                     values=(record[0], record[1], record[2],
                                             record[3], record[4], record[5]))
        self.records_tree.pack()

    def show_player_reports(self):
        """
        Function shows all the reports of a specific player the csv file.
        """
        for i, record in enumerate(self.records):
            if record[0] == self.nickname_stringVar.get() and i != 0:  # ignore header and unmatched nicknames
                self.player_records.append(record)
        if self.player_records:  # list is not empty. matching nickname found
            self.remove_all_records()
            # populate table
            for i, record in enumerate(self.player_records):
                self.records_tree.insert(parent='', index='end', iid=i, text="",
                                         values=(record[0], record[1], record[2],
                                                 record[3], record[4], record[5]))
        else:  # list is empty. no matching nickname found
            self.remove_all_records()

        self.player_records = []

    def set_tree_headers(self):
        """
        Function defines the headers of the reports table
        """
        header = self.records[0]
        header_style = ttk.Style()
        header_style.configure("Treeview.Heading", font=(None, 14, 'bold'))

        # define columns
        self.records_tree["columns"] = (header[0], header[1], header[2], header[3], header[4], header[5])
        # format columns
        self.records_tree.column("#0", width=0, stretch=NO)
        self.records_tree.column(header[0], anchor=CENTER, width=120)
        self.records_tree.column(header[1], anchor=CENTER, width=80)
        self.records_tree.column(header[2], anchor=CENTER, width=120)
        self.records_tree.column(header[3], anchor=CENTER, width=120)
        self.records_tree.column(header[4], anchor=CENTER, width=120)
        self.records_tree.column(header[5], anchor=CENTER, width=120)
        # create headings
        self.records_tree.heading("#0", text="", anchor=CENTER)
        self.records_tree.heading(header[0], text=header[0], anchor=CENTER)
        self.records_tree.heading(header[1], text=header[1], anchor=CENTER)
        self.records_tree.heading(header[2], text=header[2], anchor=CENTER)
        self.records_tree.heading(header[3], text=header[3], anchor=CENTER)
        self.records_tree.heading(header[4], text=header[4], anchor=CENTER)
        self.records_tree.heading(header[5], text=header[5], anchor=CENTER)

    def remove_all_records(self):
        """
        Function removes the records from the reports table
        """
        for record in self.records_tree.get_children():
            self.records_tree.delete(record)

    @staticmethod
    def get_instance():
        return ReportsWindow.instance

    @staticmethod
    def reset_records_screen():
        ReportsWindow.instance = None

    def clear_text(self, event):
        event.widget.delete(0, "end")

    def close_window(self):
        self.reset_records_screen()
        self.master.destroy()

    def init_widgets(self):
        # frame that will consist the topic in the window
        topic_frame = Frame(self.master)
        topic_frame.configure(bg='lavender')
        topic_frame.pack()

        # frame that will consist the search in the window
        search_frame = Frame(self.master)
        search_frame.configure(bg='lavender')
        search_frame.pack()

        # frame that will consist the table of the records
        tree_frame = Frame(self.master)
        tree_frame.configure(bg='lavender')
        tree_frame.pack(pady=20)

        # frame that will consist the show all reports button in the window
        bottom_frame = Frame(self.master)
        bottom_frame.configure(bg='lavender')
        bottom_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        # frame that will consist the show all reports button in the window
        return_frame = Frame(self.master)
        return_frame.configure(bg='lavender')
        return_frame.place(relx=0.05, rely=0.97, anchor=SW)

        # create label widget for topic of the window
        topic_label = TopicLabel(topic_frame, text="Reports Table").get_label()
        topic_label.pack(side=TOP, padx=2, pady=20)

        # create scroll bar widget and attach it to the tree table frame
        scroll_tree = Scrollbar(tree_frame)
        scroll_tree.pack(side=RIGHT, fill=Y)
        # tree view widget and bind the scroll bar to it
        self.records_tree = ttk.Treeview(tree_frame, yscrollcommand=scroll_tree.set, selectmode="none")
        scroll_tree.config(command=self.records_tree.yview)

        self.set_tree_headers()

        # define stringVar for nickname input
        self.nickname_stringVar = StringVar(search_frame, value="Type a nickname")
        # create entry widget for nickname, attach it to screen and bind mouse left click to it
        nickname_entry = Entry(search_frame, textvariable=self.nickname_stringVar, font=('Ariel', 18))
        nickname_entry.bind("<Button-1>", self.clear_text)
        nickname_entry.grid(row=0, column=0, padx=10, pady=10)

        # create search button widget and attach it to screen
        button_search = Button(search_frame, text="Search", fg="white", bg="navy",
                               command=self.show_player_reports, font=('Ariel', 18))
        button_search.grid(row=0, column=1, pady=10)

        # create label widget to show error
        self.label_error = Label(bottom_frame, text="", fg="red", bg='lavender', font=('Ariel', 18))
        self.label_error.grid(row=0, column=0)

        # create show all records button widget and attach it to screen
        button_show_all = Button(bottom_frame, text="Show All", fg="white",
                                 bg="navy", command=self.show_all_reports, font=('Ariel', 18))
        button_show_all.grid(row=1, column=0, pady=25)

        # create return to main menu button widget and attach it to screen
        button_return_main_menu = Button(return_frame, text="Return to menu", fg="white",
                                         bg="green", command=self.close_window, font=('Ariel', 14))
        button_return_main_menu.pack()
