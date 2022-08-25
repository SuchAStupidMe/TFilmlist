# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from title_search import look_file, get_caption_title, format_list
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
        self.formated_list = format_list()
        self.lst = get_list()
        for item in self.lst:
            self.your_list.addItem(item[0])

        # Activities
        self.searchButton.clicked.connect(self.search)

        self.listWidget.itemDoubleClicked.connect(self.insert_into_db)

        self.your_list.itemDoubleClicked.connect(self.open_link)

        self.your_list.itemClicked.connect(self._choose_title)

        self.delete_button.clicked.connect(self._del_title)

        self.import_button.clicked.connect(self.imp_list)

        self.import_list.itemDoubleClicked.connect(self.import_search)

    # Search from input
    def search(self):
        self.listWidget.clear()
        if self.title_search.text() != '':
            self.title_dict = look_file(self.title_search.text())
            for line in self.title_dict:
                self.listWidget.addItem(line + " : " + self.title_dict[line])

    # Insertion into sql table
    def insert_into_db(self, your_list_item):
        to_insert = your_list_item.text().split(' : ')
        insert_into_table(to_insert[0], to_insert[1])
        # Adding to the list
        self.your_list.addItem(to_insert[0])

    # Open title link
    @staticmethod
    def open_link(title):
        title = title.text()
        link = str(get_link(title)).strip("',)(")
        open_new_tab(link)

    # Getting title
    def _choose_title(self, title):
        self.chosen_title = title.text()
        # Getting caption title
        link = str(get_link(self.chosen_title)).strip("',)(")
        get_caption_title(link)
        pixmap = QPixmap('caption_title.png')
        self.label_image.setPixmap(pixmap)

    # Deleting title
    def _del_title(self):
        delete_row(self.chosen_title)

        # Updating the list
        self.your_list.clear()
        self.lst = get_list()
        for item in self.lst:
            self.your_list.addItem(item[0])

    # Import button
    def imp_list(self):
        for item in self.formated_list:
            self.import_list.addItem(item)

    # Search of imported item
    def import_search(self, item):
        self.title_search.setText(item.text())
        self.search()


def app_launch():
    app = QApplication([])
    window = Window()
    app.exec_()
