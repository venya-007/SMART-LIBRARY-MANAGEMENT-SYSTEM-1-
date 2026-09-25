def login():
    print("\n--- LIBRARIAN LOGIN ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful!")
        return True

    else:
        print("Wrong username or password.")
        return False