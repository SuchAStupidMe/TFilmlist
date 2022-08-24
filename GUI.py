# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from title_search import look_file
from database import insert_into_table, get_list, get_link, delete_row
from webbrowser import open_new_tab


class Window(QMainWindow):
    title_dict = {}
    chosen_title = ''

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()

        # Initial Title list filling
        self.lst = get_list()
        for item in self.lst:
            self.your_list.addItem(item[0])

        # Activities
        self.searchButton.clicked.connect(self.search)

        self.listWidget.itemDoubleClicked.connect(self.insert_into_db)

        self.your_list.itemDoubleClicked.connect(self.open_link)

        self.your_list.itemClicked.connect(self._get_title)

        self.delete_button.clicked.connect(self._del_title)

    # Search from input
    def search(self):
        self.listWidget.clear()
        self.title_dict = look_file(self.title_search.text())
        for line in self.title_dict:
            self.listWidget.addItem(line + " : " + self.title_dict[line])

    # Insertion into sql table
    def insert_into_db(self, lstitem):
        to_insert = lstitem.text().split(' : ')
        insert_into_table(to_insert[0], to_insert[1])
        # Adding to the list
        self.your_list.addItem(to_insert[0])

    # Open title link
    def open_link(self, title):
        title = title.text()
        link = str(get_link(title)).strip("',)(")
        open_new_tab(link)

    # Getting title
    def _get_title(self, title):
        self.chosen_title = title.text()

    # Deleting title
    def _del_title(self):
        delete_row(self.chosen_title)

        # Updating the list
        self.your_list.clear()
        self.lst = get_list()
        for item in self.lst:
            self.your_list.addItem(item[0])


def app_launch():
    app = QApplication([])
    window = Window()
    app.exec_()
