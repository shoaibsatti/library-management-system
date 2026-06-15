class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        """Mark the book as borrowed."""
        self.is_borrowed = True

    def return_book(self):
        """Mark the book as returned/available."""
        self.is_borrowed = False

    def get_status(self):
        """Get the current status of the book."""
        return "Borrowed" if self.is_borrowed else "Available"

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} - {self.get_status()}"
