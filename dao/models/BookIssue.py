# Holds BookIssue model
class BookIssue:

    # Defines book issue schema and initializes an object
    def __init__(self, id=None, book_id=None, issue_date=None, return_date=None, returned_date=None):
        self.__id = id
        self.__book_id = book_id
        self.__issue_date = issue_date
        self.__return_date = return_date
        self.__returned_date = returned_date

    # Defines str method
    def __str__(self):
        return f"ID: {self.__id}, BID: {self.__book_id}, Issue date: {self.__issue_date}, Return date: {self.__return_date}, Returned date: {self.__returned_date}"

    # Gets and sets
    def get_id(self):
        return self.__id

    def get_book_id(self):
        return self.__book_id

    def get_issue_date(self):
        return self.__issue_date

    def get_return_date(self):
        return self.__return_date

    def set_return_date(self, return_date):
        self.__return_date = return_date

    def get_returned_date(self):
        return self.__returned_date

    def set_returned_date(self, returned_date):
        self.__returned_date = returned_date