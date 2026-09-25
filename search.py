from data import books


def search_book():
    print("\n--- SEARCH BOOK ---")

    keyword = input("Enter book name or author: ").lower()

    found = False

    for book in books:

        if (
            keyword in book["name"].lower()
            or keyword in book["author"].lower()
        ):
            print("\nBook ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            found = True

    if found is False:
        print("No book found.")