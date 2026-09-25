from login import login

from books import (
    add_book,
    show_books,
    delete_book
)

from members import (
    add_member,
    show_members
)

from issue_return import (
    issue_book,
    return_book,
    show_issued_books
)

from search import search_book

from reports import show_report

from utils import show_title, pause


def main():

    show_title("LIBRARY MANAGEMENT SYSTEM")

    if login() is False:
        print("Program closed.")
        return

    while True:

        show_title("MAIN MENU")

        print("1. Add Book")
        print("2. Show Books")
        print("3. Delete Book")
        print("4. Add Member")
        print("5. Show Members")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Show Issued Books")
        print("9. Search Book")
        print("10. Library Report")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_books()

        elif choice == "3":
            delete_book()

        elif choice == "4":
            add_member()

        elif choice == "5":
            show_members()

        elif choice == "6":
            issue_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            show_issued_books()

        elif choice == "9":
            search_book()

        elif choice == "10":
            show_report()

        elif choice == "11":
            print("Thank you for using the library system.")
            break

        else:
            print("Invalid choice.")

        pause()


if __name__ == "__main__":
    main()