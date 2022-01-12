from .Interface import Interface
from .gui.MainMenu import Ui_MainWindow
from .gui.CatchExceptions import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class GraphicUserInterface(Interface):
    
    # Initializes GUI
    def __init__(self):

        super().__init__()

        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Updates the widgets
        self.update_widgets()
        # Appends actions to widgets
        self.widget_actions()
        # Loads the books
        self.load_books()
        # Loads the issues
        self.load_issues()

        self.MainWindow.show()
        sys.exit(app.exec_())

    # Appends actions to some widgets
    def widget_actions(self):
        self.ui.book_search_button.clicked.connect(self.search_book) # Books search button
        self.ui.book_delete.clicked.connect(self.delete_book) # Books delete rows button
        self.ui.book_add.clicked.connect(self.add_row) # Books add row button
        self.ui.book_save.clicked.connect(self.book_save) # Books save rows button
        self.ui.book_issue.clicked.connect(self.issue_book) # Books issue button
        self.ui.book_refresh.clicked.connect(self.refresh_books) # Books refresh button
        self.ui.issue_refresh.clicked.connect(self.load_issues) # Issues refresh button
        self.ui.issue_return.clicked.connect(self.return_book) # Issues return button
        self.ui.actionQuit.triggered.connect(self.exit_program) # Exit program button

    # Updates the widgets
    def update_widgets(self):
        # Sets tab names to Books and Issues
        _translate = QtCore.QCoreApplication.translate
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.Books), _translate("MainWindow", "Books"))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.Issues), _translate("MainWindow", "Issues"))
        # Sets issues table to read only
        self.ui.issue_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # Refresh books table
    def refresh_books(self):
        while (self.ui.book_table.rowCount() > 0):
            self.ui.book_table.removeRow(0)

        self.load_books()

    # Loads books into the data table
    def load_books(self):
        self.ui.book_table.setColumnCount(0) # Clears table

        query = self.ui.book_search.text()
        if query == "": # If there is not a query, loads all books
            self.list_all_books()
        else: # If there is a query, searches for a book
            self.search_book()
    
    # Loads issues into the data table
    def load_issues(self):
        self.ui.issue_table.setColumnCount(0) # Clears table
        book_issues = self.library.list_issues()

        self.ui.issue_table.setRowCount( len(book_issues) )
        self.ui.issue_table.setColumnCount(5)
        self.ui.issue_table.setHorizontalHeaderLabels(['ID', 'BID', 'Issue Date', 'Return Date', 'Returned Date'])

        for i, issue in enumerate(book_issues):
            self.ui.issue_table.setItem(i, 0, QtWidgets.QTableWidgetItem( str( issue.get_id() ) ))
            self.ui.issue_table.setItem(i, 1, QtWidgets.QTableWidgetItem( str( issue.get_book_id() ) ))
            self.ui.issue_table.setItem(i, 2, QtWidgets.QTableWidgetItem( str( issue.get_issue_date() ) ))
            self.ui.issue_table.setItem(i, 3, QtWidgets.QTableWidgetItem( str( issue.get_return_date() ) ))
            self.ui.issue_table.setItem(i, 4, QtWidgets.QTableWidgetItem( str( issue.get_returned_date() ) ))

    # Adds a now row to the books table
    def add_row(self):
        rowPosition = self.ui.book_table.rowCount()
        self.ui.book_table.insertRow(rowPosition)

        id_item = QtWidgets.QTableWidgetItem("")
        id_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.ui.book_table.setItem(rowPosition, 0, id_item )

    # Saves the selected lines of books table
    def book_save(self):
        for index in self.ui.book_table.selectedIndexes():
            book_id = self.ui.book_table.item( index.row(), 0 ).text()
            book_title = self.ui.book_table.item( index.row(), 1 ).text()
            book_author = self.ui.book_table.item( index.row(), 2 ).text()

            if book_id == "":
                self.library.add_new_book(book_title, book_author)
            else:
                self.library.edit_book(book_id, book_title, book_author)

        self.load_books()

    # Populates books table
    def populate_books(self, books):
        self.ui.book_table.setRowCount( len(books) )
        self.ui.book_table.setColumnCount(4)
        self.ui.book_table.setHorizontalHeaderLabels(['BID', 'Title', 'Author', 'Available'])

        for i, book in enumerate(books):
            id_item = QtWidgets.QTableWidgetItem( str( book.get_id() ) )
            id_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            available_item = QtWidgets.QTableWidgetItem( str( book.get_available() ) )
            available_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            self.ui.book_table.setItem(i, 0, id_item )
            self.ui.book_table.setItem(i, 1, QtWidgets.QTableWidgetItem( book.get_title() ))
            self.ui.book_table.setItem(i, 2, QtWidgets.QTableWidgetItem( book.get_author() ))
            self.ui.book_table.setItem(i, 3, available_item )

    # Lists all books
    def list_all_books(self):
        books = self.library.list_all_books()
        self.populate_books(books)
        

    # Searches for a book
    def search_book(self):
        query = self.ui.book_search.text()
        books = self.library.search_book(query)

        self.populate_books(books)

    # Deletes selected rows from books table
    def delete_book(self):
        for index in self.ui.book_table.selectedIndexes():
            book_id = self.ui.book_table.item( index.row(), 0 ).text()
            self.library.delete_book(book_id)

        self.load_books()
        
    # Issues selected books
    def issue_book(self):
        for index in self.ui.book_table.selectedIndexes():
            book_id = self.ui.book_table.item( index.row(), 0 ).text()
            self.library.issue_book(book_id)

        self.load_books()
        
    # Returns selected books
    def return_book(self):
        for index in self.ui.issue_table.selectedIndexes():
            issue_id = self.ui.issue_table.item( index.row(), 0 ).text()
            self.library.return_book(issue_id)

        self.load_issues()
        
    # Exits program
    def exit_program(self):
        QtCore.QCoreApplication.quit()
