from data import books, issued_books
from members import find_member
from utils import get_number


def issue_book():
    print("\n--- ISSUE BOOK ---")

    book_id = get_number("Enter book ID: ")
    member_id = get_number("Enter member ID: ")

    selected_book = None

    for book in books:
        if book["id"] == book_id:
            selected_book = book

    if selected_book is None:
        print("Book not found.")
        return

    if selected_book["available"] is False:
        print("Book is already issued.")
        return

    member = find_member(member_id)

    if member is None:
        print("Member not found.")
        return

    selected_book["available"] = False

    issued_record = {
        "book_id": book_id,
        "member_id": member_id
    }

    issued_books.append(issued_record)

    print("Book issued successfully.")


def return_book():
    print("\n--- RETURN BOOK ---")

    book_id = get_number("Enter book ID: ")

    for record in issued_books:
        if record["book_id"] == book_id:

            for book in books:
                if book["id"] == book_id:
                    book["available"] = True

            issued_books.remove(record)

            print("Book returned successfully.")
            return

    print("This book is not issued.")


def show_issued_books():
    print("\n--- ISSUED BOOKS ---")

    if len(issued_books) == 0:
        print("No books are currently issued.")
        return

    for record in issued_books:
        print("\nBook ID:", record["book_id"])
        print("Member ID:", record["member_id"])