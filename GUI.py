# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from title_search import look_file, get_caption_title_and_description, format_list
from database import insert_into_table, get_list, get_link, delete_row
from webbrowser import open_new_tab


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()

        # Initial Title list filling
        self.title_dict = {}
        self.chosen_title = ''
        self.formatted_list = format_list()
        self.final_filmlist = get_list()
        for item in self.final_filmlist:
            self.your_list.addItem(item[0])

        # Activities

        # Search button
        self.searchButton.clicked.connect(self.search)

        # Insertion into database
        self.listWidget.itemDoubleClicked.connect(self.insert_into_db)

        # Opening a link from list
        self.your_list.itemDoubleClicked.connect(self._open_link)

        # Choosing a title in the database
        self.your_list.itemClicked.connect(self._choose_title)

        # Delete from database button
        self.delete_button.clicked.connect(self._del_title)

        # Importing a list from .txt file
        self.import_button.clicked.connect(self.imp_list)

        # Search from imported .txt file
        self.import_list.itemDoubleClicked.connect(self.import_search)

    # Search from input function (Search button)
    def search(self):
        self.listWidget.clear()
        if self.title_search.text() != '':
            self.title_dict = look_file(self.title_search.text())
            for line in self.title_dict:
                self.listWidget.addItem(line + " : " + self.title_dict[line])

    # Insertion into sql table (Double-click search list)
    def insert_into_db(self, your_list_item):
        to_insert = your_list_item.text().split(' : ')
        insert_into_table(to_insert[0], to_insert[1])
        self.your_list.addItem(to_insert[0])  # Adding to the list

    # Open title link (Double-click on film list)
    @staticmethod
    def _open_link(title):
        title = title.text()
        link = str(get_link(title)).strip("',)(")
        open_new_tab(link)

    # Single click on title in film list
    def _choose_title(self, title):
        self.chosen_title = title.text()
        # Getting caption title and description
        link = str(get_link(self.chosen_title)).strip("',)(")
        description = get_caption_title_and_description(link)

        self.description_label.setText(description)

        pixmap = QPixmap('caption_title.png')  # Image loads and overwrites from buffer file
        self.label_image.setPixmap(pixmap)

    # Deleting title function using chosen title
    def _del_title(self):
        delete_row(self.chosen_title)
        self.label_image.clear()  # Clearing of the caption image
        self.description_label.clear()  # Clearing description

        # Updating the list
        self.your_list.clear()
        self.final_filmlist = get_list()
        for item in self.final_filmlist:
            self.your_list.addItem(item[0])

    # Import from .txt file button
    def imp_list(self):
        for item in self.formatted_list:
            self.import_list.addItem(item)

    # Search of imported item by double-clicking imported list
    def import_search(self, item):
        self.title_search.setText(item.text())  # Setting title name into input widget
        self.search()


def app_launch():
    app = QApplication([])
    window = Window()
    app.exec_()
