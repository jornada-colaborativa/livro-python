class Book:
    def __init__(self, title):
        self.title = title
        self.is_lent = False

class Library:
    def __init__(self):
        self.lent_books = []

    def lend_book(self, book):
        # modulo a ser testado
        if not book.is_lent:
            book.is_lent = True
            self.lent_books.append(book)
