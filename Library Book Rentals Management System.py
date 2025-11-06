import os
import datetime

# ---------------------------
# File Setup
# ---------------------------
BOOKS_FILE = "books.txt"
RENTALS_FILE = "rentals.txt"

# Initialize files if not found
for file in [BOOKS_FILE, RENTALS_FILE]:
    if not os.path.exists(file):
        open(file, "w").close()

# ---------------------------
# Utility Functions
# ---------------------------
def read_file(filename):
    """Reads a file and returns a list of lines without newlines."""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def write_file(filename, lines):
    """Writes a list of lines to a file."""
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def append_file(filename, line):
    """Appends a single line to a file."""
    with open(filename, "a") as f:
        f.write(line + "\n")

# ---------------------------
# Core Functionalities
# ---------------------------
def show_books():
    """Display all available books."""
    books = read_file(BOOKS_FILE)
    if not books:
        print("\n📚 No books available in the library.\n")
    else:
        print("\n📚 Available Books:")
        print("-" * 40)
        for book in books:
            book_id, title, author, available = book.split("|")
            status = "✅ Available" if available == "yes" else "❌ Rented"
            print(f"ID: {book_id} | {title} by {author} | {status}")
        print("-" * 40)

def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if not title or not author:
        print("⚠️ Both fields are required.")
        return
    books = read_file(BOOKS_FILE)
    new_id = len(books) + 1
    append_file(BOOKS_FILE, f"{new_id}|{title}|{author}|yes")
    print(f"✅ '{title}' by {author} added successfully!")

def rent_book():
    """Rent out a book to a customer."""
    show_books()
    try:
        book_id = int(input("\nEnter Book ID to rent: "))
        customer = input("Enter customer name: ").strip()
        if not customer:
            print("⚠️ Customer name cannot be empty.")
            return
        books = read_file(BOOKS_FILE)
        updated_books = []
        found = False

        for book in books:
            b_id, title, author, available = book.split("|")
            if int(b_id) == book_id:
                found = True
                if available == "no":
                    print(f"❌ '{title}' is already rented.")
                    return
                else:
                    date_rented = datetime.date.today().strftime("%Y-%m-%d")
                    append_file(RENTALS_FILE, f"{book_id}|{title}|{customer}|{date_rented}|not_returned")
                    updated_books.append(f"{b_id}|{title}|{author}|no")
                    print(f"✅ '{title}' rented to {customer}.")
            else:
                updated_books.append(book)
        if not found:
            print("⚠️ Book ID not found.")
            return
        write_file(BOOKS_FILE, updated_books)
    except ValueError:
        print("⚠️ Invalid input. Enter a valid number.")

def return_book():
    """Return a rented book."""
    rentals = read_file(RENTALS_FILE)
    if not rentals:
        print("\n📄 No active rentals found.")
        return
    print("\n📦 Active Rentals:")
    for rent in rentals:
        b_id, title, customer, date_rented, status = rent.split("|")
        if status == "not_returned":
            print(f"ID: {b_id} | {title} | {customer} | Rented on: {date_rented}")
    try:
        book_id = int(input("\nEnter Book ID to return: "))
        found = False
        updated_rentals = []
        for rent in rentals:
            b_id, title, customer, date_rented, status = rent.split("|")
            if int(b_id) == book_id and status == "not_returned":
                found = True
                date_returned = datetime.date.today().strftime("%Y-%m-%d")
                updated_rentals.append(f"{b_id}|{title}|{customer}|{date_rented}|returned:{date_returned}")
                print(f"✅ '{title}' returned successfully by {customer}.")
            else:
                updated_rentals.append(rent)
        if not found:
            print("⚠️ Rental record not found or already returned.")
            return
        write_file(RENTALS_FILE, updated_rentals)

        # Update book availability
        books = read_file(BOOKS_FILE)
        updated_books = []
        for book in books:
            b_id, title, author, available = book.split("|")
            if int(b_id) == book_id:
                updated_books.append(f"{b_id}|{title}|{author}|yes")
            else:
                updated_books.append(book)
        write_file(BOOKS_FILE, updated_books)
    except ValueError:
        print("⚠️ Invalid input. Enter a valid number.")

def show_rental_summary():
    """Generate a rental summary report."""
    rentals = read_file(RENTALS_FILE)
    if not rentals:
        print("\n📄 No rental records found.\n")
        return
    print("\n📊 Rental Summary Report:")
    print("-" * 70)
    for rent in rentals:
        b_id, title, customer, date_rented, status = rent.split("|")
        print(f"Book ID: {b_id} | {title} | Rented by: {customer} | On: {date_rented} | Status: {status}")
    print("-" * 70)

# ---------------------------
# Main Menu
# ---------------------------
def main():
    while True:
        print("\n===== 📘 RentTrack Library Management =====")
        print("1️⃣ Show All Books")
        print("2️⃣ Add New Book")
        print("3️⃣ Rent a Book")
        print("4️⃣ Return a Book")
        print("5️⃣ View Rental Summary")
        print("6️⃣ Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            rent_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            show_rental_summary()
        elif choice == "6":
            print("\n👋 Exiting RentTrack... Goodbye!\n")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1–6.")

# ---------------------------
# Program Entry Point
# ---------------------------
if __name__ == "__main__":
    main()
