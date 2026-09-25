from data import books, members, issued_books


def show_report():
    print("\n--- LIBRARY REPORT ---")

    total_books = len(books)
    total_members = len(members)
    total_issued = len(issued_books)

    available_books = 0

    for book in books:
        if book["available"]:
            available_books += 1

    print("Total books:", total_books)
    print("Available books:", available_books)
    print("Issued books:", total_issued)
    print("Total members:", total_members)