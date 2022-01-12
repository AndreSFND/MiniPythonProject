from .BookDao import BookDao
from .models.Book import Book
from .database.DBConnector import DBConnector

# Implements Book Dao SQL
class BookDaoSQL(BookDao):

    # Initializes the Dao
    def __init__(self):
        self.db_connector = DBConnector() # Creates a database connector
    
    # Lists all books
    def index(self, order='DESC'):
        book_list = []

        query = f"SELECT B.*, IF(BI.return_date IS NULL, TRUE, FALSE) AS available FROM books B LEFT JOIN book_issues BI ON B.BID = BI.bid AND BI.returned_date IS NULL ORDER BY B.BID {order}"
        books = self.db_connector.get_data(query)
        
        for book in books:
            book_list.append( Book(book[0], book[1], book[2], book[3]) )

        return book_list
    
    # Searches for a book
    def search(self, query, order='DESC'):
        book_list = []

        query = f"SELECT B.*, IF(BI.return_date IS NULL, TRUE, FALSE) AS available FROM books B LEFT JOIN book_issues BI ON B.BID = BI.bid AND BI.returned_date IS NULL WHERE B.BID = '{query}' OR B.title LIKE '%{query}%' OR B.author LIKE '%{query}%' ORDER BY B.BID {order}"
        books = self.db_connector.get_data(query)
        
        for book in books:
            book_list.append( Book(book[0], book[1], book[2], book[3]) )

        return book_list
    
    # Creates a new book
    def create(self, title, author):
        query = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
        self.db_connector.execute(query)

        return True
    
    # Updates a book
    def update(self, id, title, author):
        query = f"UPDATE books SET title = '{title}', author = '{author}' WHERE BID = '{id}'"
        self.db_connector.execute(query)

        return True
        
    # Deletes a book
    def delete(self, id):
        query = f"DELETE FROM books WHERE BID = '{id}'"
        self.db_connector.execute(query)

        return True