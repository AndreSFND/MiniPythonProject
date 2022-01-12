# Holds book model
class Book:

    # Defines book schema and initializes an object
    def __init__(self, id=None, title=None, author=None, available=None):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__available = available

    # Defines str method
    def __str__(self):
        return f"ID: {self.__id}, title: {self.__title}, Author: {self.__author}, Available: {self.__available}"

    # Gets and sets
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_available(self):
        return self.__available