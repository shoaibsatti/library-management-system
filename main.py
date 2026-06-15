from library import Library

def main():
    library = Library()

    while True:
        print("\n===== LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            print(library.add_book(book_id, title, author))

        elif choice == "2":
            books = library.view_books()
            for b in books:
                print(b)

        elif choice == "3":
            book_id = input("Book ID to borrow: ")
            print(library.borrow_book(book_id))

        elif choice == "4":
            book_id = input("Book ID to return: ")
            print(library.return_book(book_id))

        elif choice == "5":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
