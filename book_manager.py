from book import Book


class BookManager:
    """Manages the library's book collection."""
    
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a new book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False

    def get_book_by_id(self, book_id):
        """Retrieve a book by its ID."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def borrow_book(self, book_id):
        """Borrow a book from the library."""
        book = self.get_book_by_id(book_id)
        if book and not book.is_borrowed:
            book.borrow()
            return True
        return False

    def return_book(self, book_id):
        """Return a borrowed book to the library."""
        book = self.get_book_by_id(book_id)
        if book and book.is_borrowed:
            book.return_book()
            return True
        return False

    def get_available_books(self):
        """Get all available books."""
        return [book for book in self.books if not book.is_borrowed]

    def get_borrowed_books(self):
        """Get all borrowed books."""
        return [book for book in self.books if book.is_borrowed]

    def list_all_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books in the library.")
            return
        
        print("\n" + "="*60)
        print("LIBRARY BOOKS")
        print("="*60)
        for book in self.books:
            print(book)
        print("="*60 + "\n")

    def search_by_title(self, title):
        """Search books by title."""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        """Search books by author."""
        return [book for book in self.books if author.lower() in book.author.lower()]
