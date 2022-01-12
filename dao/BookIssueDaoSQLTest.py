import unittest
from .BookIssueDaoSQL import BookIssueDaoSQL

class BookIssueDaoSQLTest(unittest.TestCase):
    def setUp(self):
        self.book_issue_dao = BookIssueDaoSQL()

    # Tests index method
    def test_1_index(self):
        issues = self.book_issue_dao.index(order='ASC')
        first_issue = issues[0]
        (issue_id, bid) = (first_issue.get_id(), first_issue.get_book_id())

        self.assertEqual((issue_id, bid), (1, 1))

    # Tests issue method
    def test_2_issue(self):
        book_id = 1
        self.book_issue_dao.create_issue(book_id)

        issues = self.book_issue_dao.index()
        first_issue = issues[0]
        bid = first_issue.get_book_id()

        self.assertEqual(bid, book_id)

    # Tests return method
    def test_3_return(self):
        try:
            book_id = 2
            self.book_issue_dao.create_issue(book_id)

            issues = self.book_issue_dao.index()
            first_issue = issues[0]
            issue_id = first_issue.get_id()

            result = self.book_issue_dao.close_issue(issue_id)

            self.assertEqual(result, True)

        except Exception as e:
            result = False

        self.assertEqual(result, True)    

if __name__ == '__main__':
    # unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()