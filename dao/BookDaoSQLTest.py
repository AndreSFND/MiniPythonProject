import unittest
from .BookDaoSQL import BookDaoSQL

class BookDaoSQLTest(unittest.TestCase):
    def setUp(self):
        self.book_dao = BookDaoSQL()

    # Tests index method
    def test_1_index(self):
        books = self.book_dao.index(order='ASC')
        first_book = books[0]
        (bid, title, author) = (first_book.get_id(), first_book.get_title(), first_book.get_author())

        self.assertEqual((bid, title, author), (1, 'Harry Potter 1', 'J K Rowling'))

    # Tests search method
    def test_2_search(self):
        books = self.book_dao.search("Dialog", order='ASC')
        first_book = books[0]
        (bid, title, author) = (first_book.get_id(), first_book.get_title(), first_book.get_author())

        self.assertEqual((bid, title, author), (5, 'Harry Potter 4', 'Dialog'))

    # Tests create method
    def test_3_create(self):
        book_title = "New book"
        book_author = "Andre"
        self.book_dao.create(book_title, book_author)

        books = self.book_dao.index()
        first_book = books[0]
        (title, author) = (first_book.get_title(), first_book.get_author())

        self.assertEqual((title, author), (book_title, book_author))

    # Tests update method
    def test_4_update(self):
        books = self.book_dao.index(order='ASC')
        first_book = books[0]
        (bid, title, author) = (first_book.get_id(), first_book.get_title(), first_book.get_author())

        book_title = "New book 2"
        book_author = "Andre S"
        self.book_dao.update(bid, book_title, book_author)

        books = self.book_dao.search("Andre S")
        first_book = books[0]
        (new_title, new_author) = (first_book.get_title(), first_book.get_author())

        self.assertEqual((new_title, new_author), (book_title, book_author))

        self.book_dao.update(bid, title, author)

    # Tests delete method
    def test_5_delete(self):
        books = self.book_dao.index()
        first_book = books[0]
        (bid, title, author) = (first_book.get_id(), first_book.get_title(), first_book.get_author())

        response = self.book_dao.delete(bid)
        self.assertEqual(response, True)

if __name__ == '__main__':
    # unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()