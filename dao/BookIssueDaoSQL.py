from .Exceptions import BookNotAvailableException, BookAlreadyReturned
from .BookIssueDao import BookIssueDao
from .models.BookIssue import BookIssue
from .database.DBConnector import DBConnector

# Implements Book Issue Dao SQL
class BookIssueDaoSQL(BookIssueDao):

    # Initializes the Dao
    def __init__(self):
        self.db_connector = DBConnector() # Creates a database connector

    # Lists all book issues
    def index(self, order='DESC'):
        book_issue_list = []

        query = f"SELECT * FROM book_issues ORDER BY issue_id {order}"
        book_issues = self.db_connector.get_data(query)
        
        for book_issue in book_issues:
            book_issue_list.append( BookIssue(book_issue[0], book_issue[1], book_issue[2], book_issue[3], book_issue[4] ) )

        return book_issue_list
    
    # Creates a new issue
    def create_issue(self, book_id, issue_days=7):
        query = f"SELECT * FROM book_issues WHERE returned_date IS NULL AND bid = {book_id}"
        book = self.db_connector.get_data(query)
        if len(book) == 0:
            query = f"INSERT INTO book_issues (bid, return_date) VALUES ('{book_id}', NOW() + INTERVAL {issue_days} DAY)"
            self.db_connector.execute(query)
        else:
            raise BookNotAvailableException("This book is not available")

        return True

    # Closes an issue
    def close_issue(self, issue_id):
        query = f"SELECT * FROM book_issues WHERE issue_id = {issue_id} AND returned_date IS NOT NULL"
        book = self.db_connector.get_data(query)
        if len(book) == 0:
            query = f"UPDATE book_issues SET returned_date = NOW() WHERE issue_id = {issue_id}"
            self.db_connector.execute(query)
        else:
            raise BookAlreadyReturned("This book has already been returned")

        return True
        