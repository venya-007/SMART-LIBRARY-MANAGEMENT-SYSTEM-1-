
# Library Management System

## Project Description

The Library Management System is a simple command-line application developed using Python.

This project helps a librarian manage books, members, book issuing, book returns, and library reports. It is designed using basic Python concepts such as functions, lists, dictionaries, loops, conditional statements, and modules.

The project is beginner-friendly and does not use a graphical user interface or database.

## Features

- Librarian login system
- Add new books
- Display all books
- Delete books
- Register library members
- Display all members
- Issue books to members
- Return books
- Display issued books
- Search books by name or author
- Display a library report

## Technologies Used

- Python 3
- Python Functions
- Python Lists
- Python Dictionaries
- Python Loops
- Python Conditional Statements
- Python Modules

## Project Structure

```text
LibraryManagementSystem/
│
├── main.py
├── books.py
├── members.py
├── issue_return.py
├── search.py
├── reports.py
├── login.py
├── data.py
└── utils.py
```

## Description of Modules

| Module | Description |
|---|---|
| main.py | Contains the main menu and controls the program |
| books.py | Adds, displays, and deletes books |
| members.py | Registers and displays members |
| issue_return.py | Issues and returns books |
| search.py | Searches books by name or author |
| reports.py | Displays library statistics |
| login.py | Handles librarian login |
| data.py | Stores books, members, and issued book records |
| utils.py | Contains reusable utility functions |

## Login Details

The default librarian login details are:

```text
Username: admin
Password: 1234
```

## Requirements

- Python 3.x
- Visual Studio Code or any Python-supported editor
- Python extension in VS Code (if using VS Code)

No external Python libraries are required.

## How to Run the Project

### Step 1: Download or Clone the Repository

Download the project files or clone the GitHub repository.

### Step 2: Open the Project Folder

Open the `LibraryManagementSystem` folder in Visual Studio Code.

### Step 3: Open the Terminal

Open the terminal in VS Code:

```text
Terminal → New Terminal
```

### Step 4: Run the Main Program

Execute the following command:

```bash
python main.py
```

If the above command does not work, try:

```bash
py main.py
```

### Step 5: Login

Enter the following login details:

```text
Username: admin
Password: 1234
```

After successful login, the main menu will be displayed.

## Main Menu Options

```text
1. Add Book
2. Show Books
3. Delete Book
4. Add Member
5. Show Members
6. Issue Book
7. Return Book
8. Show Issued Books
9. Search Book
10. Library Report
11. Exit
```

## Concepts Used

This project demonstrates the following programming concepts:

1. **Functions:** Used to divide the program into smaller tasks.
2. **Lists:** Used to store books, members, and issued book records.
3. **Dictionaries:** Used to store information about each book and member.
4. **Conditional Statements:** Used for decision-making.
5. **Loops:** Used to display and search records.
6. **Modules:** Used to divide the project into separate Python files.
7. **Exception Handling:** Used to validate numeric input.
8. **Menu-Driven Programming:** Used to interact with the user through the terminal.

## Limitations

- The project uses temporary in-memory data storage.
- Data is reset when the program is closed.
- There is no database connection.
- The project does not have a graphical user interface.
- Only one basic librarian login is provided.
- The system does not include advanced fine calculation or due-date tracking.

## Future Improvements

The following features can be added in the future:

- Database integration
- Graphical user interface
- Permanent data storage
- Multiple librarian accounts
- Due-date tracking
- Fine calculation
- Advanced book management
- Improved security

## Conclusion

The Library Management System is a beginner-friendly Python project that demonstrates how different programming concepts can be combined to create a practical application.

It provides basic library management functionality through a simple command-line interface and helps develop an understanding of modular programming in Python.

## Author
Venya Bisen


Developed as a Python project for academic learning and evaluation.
