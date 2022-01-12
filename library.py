from dao.BookDaoSQL import BookDaoSQL
from dao.BookIssueDaoSQL import BookIssueDaoSQL

# Organizes Books and BookIssues DAOs
class Library:

    # Initializes DAOs
    def __init__(self):
        self.book_dao = BookDaoSQL()
        self.book_issue_dao = BookIssueDaoSQL()

    # Creates a new book
    def add_new_book(self, title, author):
        self.book_dao.create(title, author)

    # Lists all books
    def list_all_books(self):
        books = self.book_dao.index()
        return books

    # Searches for a book
    def search_book(self, query):
        books = self.book_dao.search(query)
        return books

    # Edits a book
    def edit_book(self, id, title, author):
        self.book_dao.update(id, title, author)

    # Deletes a book
    def delete_book(self, id):
        self.book_dao.delete(id)

    # Lists all book issues
    def list_issues(self):
        book_issues = self.book_issue_dao.index()
        return book_issues
    
    # Issues a book
    def issue_book(self, book_id, issue_days=7):
        self.book_issue_dao.create_issue(book_id, issue_days)
    
    # Returns a book
    def return_book(self, issue_id):
        self.book_issue_dao.close_issue(issue_id)