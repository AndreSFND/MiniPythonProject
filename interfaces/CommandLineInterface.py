from .Interface import Interface
from dao.Exceptions import *
import sys

# Class that holds the CLI
class CommandLineInterface(Interface):

    # Initializes the cli
    def __init__(self):

        super().__init__() # Runs Interface initializer
        
        # Initializes menu options
        self.menu_options = {

            '1': { 'label': "Add a new Book", 'function': self.add_new_book },
            '2': { 'label': "List all books", 'function': self.list_all_books },
            '3': { 'label': "Search for book", 'function': self.search_book },
            '4': { 'label': "Edit a book", 'function': self.edit_book },
            '5': { 'label': "Delete a book", 'function': self.delete_book },
            '6': { 'label': "Issue a book", 'function': self.issue_book },
            '7': { 'label': "Return a book", 'function': self.return_book },
            '0': { 'label': "Exit", 'function': self.exit_program }
            
        }

        # Runs main menu
        self.main_menu()

    # Runs main menu
    def main_menu(self):
        # While user doesnt exit application, run the mains menu
        while(True):
            # Prints the main menu
            self.print_main_menu() 
            # Reads the user option and calls it
            try:
                choice = input("Enter the choice: ") # Reads user option 
                self.menu_options.get(choice).get('function')() # Call its method
            except Exception:
                print("Try a valid option")
            # Waits for an interaction
            input("\nPress ENTER to continue")

    # Prints main menu
    def print_main_menu(self):
        print("\n****Welcome to Simple Library Management System****\n")
        print(" MAIN MENU")
        print("=====================")
        self.print_menu_options() # Prints menu options
        print("=====================\n")

    # Prints menu options
    def print_menu_options(self):
        for i, (key, value) in enumerate(self.menu_options.items()):
            label = value.get('label')
            print(f"[{key}] {label}")

    # Adds a new book
    def add_new_book(self):
        print("Inserting a new book\n")
        book_title = input("Insert the book title: ")
        book_author = input("Insert the book author: ")

        try:
           self.library.add_new_book(book_title, book_author)
        except Exception:
            print("An error ocurred, try again later")

    # Lists all books
    def list_all_books(self):
        print("Listing all books:\n")

        try:
            books = self.library.list_all_books()
            for book in books:
                print(book)
        except Exception:
            print("An error ocurred, try again later")

    # Searches for a book
    def search_book(self):
        print("Searching for a book\n")
        query = input("Insert the word to search for: ")

        try:
            books = self.library.search_book(query)
            for book in books:
                print(book)
        except Exception:
            print("An error ocurred, try again later")

    # Edits a book
    def edit_book(self):
        print("Editing a book\n")

        while True:
            try:
                book_id = int( input("Insert the book ID: ") )
                break
                
            except Exception:
                print("Type a valid book ID (number)")

        book_title = input("Insert the book title: ")
        book_author = input("Insert the book author: ")

        try:
            self.library.edit_book(book_id, book_title, book_author)
        except Exception:
            print("An error ocurred, try again later")

    # Deletes a book
    def delete_book(self):
        print("Deleting a book\n")
        while True:
            try:
                book_id = int( input("Insert the book ID: ") )
                break
                
            except Exception:
                print("Type a valid book ID (number)")

        try:
            self.library.delete_book(book_id)
        except Exception:
            print("An error ocurred, try again later")

    # Issues a book
    def issue_book(self):
        print("Issuing a book\n")
        while True:
            try:
                book_id = int( input("Insert the book ID: ") )
                break
                
            except Exception:
                print("Type a valid book ID (number)")

        try:
            self.library.issue_book(book_id)
        except BookNotAvailableException as e:
            print("This book is not available")
        except Exception:
            print("An error ocurred, try again later")

    # Returns a book
    def return_book(self):
        print("Returning a book\n")
        while True:
            try:
                issue_id = int( input("Insert the issue ID: ") )
                break
                
            except Exception:
                print("Type a valid issue ID (number)")

        try:
            self.library.return_book(issue_id)
        except BookAlreadyReturned as e:
            print("This book has already been returned")
        except Exception:
            print("An error ocurred, try again later")

    # Exists program
    def exit_program(self):
        sys.exit()