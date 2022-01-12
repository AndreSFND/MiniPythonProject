from .models.Book import Book

# Defines book DAO interface
class BookDao():

    def index(self):
        pass
    
    def search(self, query):
        pass
    
    def create(self, name, author):
        pass
    
    def update(self, book, name, author):
        pass
        
    def delete(self, id):
        pass