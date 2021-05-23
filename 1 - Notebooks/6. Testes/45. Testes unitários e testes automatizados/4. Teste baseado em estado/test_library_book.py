import unittest
from library_book import Library, Book
class TestLibrary(unittest.TestCase):
    def test_lend_book_not_lent(self):
        # Arrange
        new_book = Book("Dom Casmurro")
        new_library = Library()
        # Action
        new_library.lend_book(new_book)
        # Assert
        self.assertTrue(new_book.is_lent)
        self.assertEqual(new_library.lent_books, [new_book])

if __name__ == '__main__':
    unittest.main()
