# main.py
from db import setup_database
from book_manager import add_book, list_books, delete_book

def main():
    setup_database()

    while True:
        print("\n1. Add a book")
        print("2. List books")
        print("3. Delete a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
        elif choice == "2":
            books = list_books()
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
        elif choice == "3":
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
