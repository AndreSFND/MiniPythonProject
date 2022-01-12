from .models.BookIssue import BookIssue

# Defines book issue DAO interface
class BookIssueDao:

    def index(self):
        pass
    
    def create(self, book_id, issue_date, return_date):
        pass

    def close(self, issue_id):
        pass