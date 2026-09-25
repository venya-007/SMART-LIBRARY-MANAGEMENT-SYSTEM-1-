from data import books
from utils import get_number


def add_book():
    print("\n--- ADD BOOK ---")

    name = input("Enter book name: ")
    author = input("Enter author name: ")

    book_id = len(books) + 1

    book = {
        "id": book_id,
        "name": name,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book added successfully.")


def show_books():
    print("\n--- ALL BOOKS ---")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print("\nBook ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")


def delete_book():
    print("\n--- DELETE BOOK ---")

    book_id = get_number("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["available"] is False:
                print("This book is currently issued.")
                return

            books.remove(book)

            print("Book deleted successfully.")
            return

    print("Book not found.")