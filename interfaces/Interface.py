from library import Library # Imports library

# Defines interface class
class Interface:

    # Initializes the class
    def __init__(self):
        self.library = Library() # Instantiates library
 
    # Defines abstract methods
    def add_new_book(self):
        pass

    def list_all_books(self):
        pass

    def search_book(self):
        pass
        
    def edit_book(self):
        pass
        
    def delete_book(self):
        pass
        
    def issue_book(self):
        pass
        
    def return_book(self):
        pass
        
    def exit_program(self):
        pass

