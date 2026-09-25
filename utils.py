def pause():
    input("\nPress Enter to continue...")


def get_number(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Enter a positive number.")

        except ValueError:
            print("Enter a valid number.")


def show_title(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)