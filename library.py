from book import Book

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            return "❌ Book ID already exists."

        self.books[book_id] = Book(book_id, title, author)
        return "✅ Book added successfully."

    def view_books(self):
        if not self.books:
            return ["📭 No books in library."]
        return [str(book) for book in self.books.values()]

    def borrow_book(self, book_id):
        book = self.books.get(book_id)

        if not book:
            return "❌ Book not found."

        if book.is_borrowed:
            return "❌ Book already borrowed."

        book.is_borrowed = True
        return f"📕 Borrowed: {book.title}"

    def return_book(self, book_id):
        book = self.books.get(book_id)

        if not book:
            return "❌ Book not found."

        if not book.is_borrowed:
            return "❌ Book was not borrowed."

        book.is_borrowed = False
        return f"📗 Returned: {book.title}"
