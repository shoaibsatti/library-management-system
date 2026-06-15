# Library Management System

A modular Python library management system with separated concerns for better code organization and maintainability.

## Project Structure

```
library-management-system/
├── book.py              # Book data model
├── book_manager.py      # Book management logic
├── main.py             # Application entry point
└── README.md           # This file
```

## Files Overview

### `book.py`
Contains the `Book` class - represents a single book with properties:
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Author name
- `is_borrowed`: Borrowing status

**Methods:**
- `borrow()` - Mark book as borrowed
- `return_book()` - Mark book as returned
- `get_status()` - Get current status
- `__str__()` - String representation

### `book_manager.py`
Contains the `BookManager` class - manages the entire book collection.

**Methods:**
- `add_book(book)` - Add a new book
- `get_book_by_id(book_id)` - Retrieve book by ID
- `borrow_book(book_id)` - Borrow a book
- `return_book(book_id)` - Return a borrowed book
- `get_available_books()` - Get all available books
- `get_borrowed_books()` - Get all borrowed books
- `list_all_books()` - Display all books
- `search_by_title(title)` - Search by title
- `search_by_author(author)` - Search by author

### `main.py`
Application entry point with example usage demonstrating all features.

## Running the Application

```bash
python main.py
```

## Example Output

```
📚 Welcome to Library Management System

============================================================
LIBRARY BOOKS
============================================================
[1] Python 101 by John Doe - Available
[2] Web Development Basics by Jane Smith - Available
[3] Data Science Guide by Alice Johnson - Available
[4] Machine Learning by Bob Wilson - Available
============================================================

Borrowing 'Python 101'...
✓ Book borrowed successfully!

[1] Python 101 by John Doe - Borrowed
[2] Web Development Basics by Jane Smith - Available
...
```

## Benefits of Separation

✅ **Single Responsibility**: Each class has one clear purpose
✅ **Reusability**: Easy to import and use in other projects
✅ **Testability**: Simple to write unit tests
✅ **Maintainability**: Changes to one module don't affect others
✅ **Scalability**: Easy to add new features

## Future Enhancements

- Add database integration (SQLite, PostgreSQL)
- Implement user authentication
- Add due dates for borrowed books
- Create a web interface (Flask/Django)
- Add book categories and genres
- Implement reservation system
