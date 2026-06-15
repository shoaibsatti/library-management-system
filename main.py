from book import Book
from book_manager import BookManager


SAMPLE_BOOKS = [
    (1, "Python 101", "John Doe"),
    (2, "Web Development Basics", "Jane Smith"),
    (3, "Data Science Guide", "Alice Johnson"),
    (4, "Machine Learning", "Bob Wilson"),
]

BOOKS_TO_BORROW = [1, 3]


def initialize_library(manager):
    """Initialize the library with sample books."""
    for book_id, title, author in SAMPLE_BOOKS:
        book = Book(book_id, title, author)
        manager.add_book(book)


def borrow_books(manager, book_ids):
    """Borrow multiple books from the library."""
    for book_id in book_ids:
        book = next((b for b in manager.get_available_books() if b.book_id == book_id), None)
        if book:
            print(f"Borrowing '{book.title}'...")
            if manager.borrow_book(book_id):
                print("✓ Book borrowed successfully!\n")


def display_book_status(manager):
    """Display the current status of available and borrowed books."""
    available = manager.get_available_books()
    print(f"Available books: {len(available)}")
    for book in available:
        print(f"  - {book.title}")
    print()
    
    borrowed = manager.get_borrowed_books()
    print(f"Borrowed books: {len(borrowed)}")
    for book in borrowed:
        print(f"  - {book.title}")
    print()


def search_and_display(manager, author):
    """Search for books by author and display results."""
    print(f"Searching for books by '{author}'...")
    results = manager.search_by_author(author)
    for book in results:
        print(f"  - {book}")
    print()


def return_books(manager, book_ids):
    """Return multiple books to the library."""
    for book_id in book_ids:
        book = next((b for b in manager.get_borrowed_books() if b.book_id == book_id), None)
        if book:
            print(f"Returning '{book.title}'...")
            if manager.return_book(book_id):
                print("✓ Book returned successfully!\n")


def main():
    """Main entry point for the library management system."""
    manager = BookManager()
    
    print("📚 Welcome to Library Management System\n")
    
    # Initialize library with sample books
    initialize_library(manager)
    
    # Display all books
    manager.list_all_books()
    
    # Borrow books
    borrow_books(manager, BOOKS_TO_BORROW)
    
    # Display all books after borrowing
    manager.list_all_books()
    
    # Display book status
    display_book_status(manager)
    
    # Search by author
    search_and_display(manager, "John Doe")
    
    # Return borrowed books
    return_books(manager, BOOKS_TO_BORROW)
    
    # Final display
    manager.list_all_books()


if __name__ == "__main__":
    main()
