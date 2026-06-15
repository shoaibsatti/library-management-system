from book import Book
from book_manager import BookManager


def main():
    """Main entry point for the library management system."""
    
    # Initialize the book manager
    manager = BookManager()
    
    # Create sample books
    book1 = Book(1, "Python 101", "John Doe")
    book2 = Book(2, "Web Development Basics", "Jane Smith")
    book3 = Book(3, "Data Science Guide", "Alice Johnson")
    book4 = Book(4, "Machine Learning", "Bob Wilson")
    
    # Add books to the library
    manager.add_book(book1)
    manager.add_book(book2)
    manager.add_book(book3)
    manager.add_book(book4)
    
    print("📚 Welcome to Library Management System\n")
    
    # Display all books
    manager.list_all_books()
    
    # Borrow some books
    print("Borrowing 'Python 101'...")
    if manager.borrow_book(1):
        print("✓ Book borrowed successfully!\n")
    
    print("Borrowing 'Data Science Guide'...")
    if manager.borrow_book(3):
        print("✓ Book borrowed successfully!\n")
    
    # Display all books after borrowing
    manager.list_all_books()
    
    # Check available books
    available = manager.get_available_books()
    print(f"Available books: {len(available)}")
    for book in available:
        print(f"  - {book.title}")
    print()
    
    # Check borrowed books
    borrowed = manager.get_borrowed_books()
    print(f"Borrowed books: {len(borrowed)}")
    for book in borrowed:
        print(f"  - {book.title}")
    print()
    
    # Search by author
    print("Searching for books by 'John Doe'...")
    results = manager.search_by_author("John Doe")
    for book in results:
        print(f"  - {book}")
    print()
    
    # Return a book
    print("Returning 'Python 101'...")
    if manager.return_book(1):
        print("✓ Book returned successfully!\n")
    
    # Final display
    manager.list_all_books()


if __name__ == "__main__":
    main()
