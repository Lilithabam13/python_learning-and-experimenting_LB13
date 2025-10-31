# Shelf track is a program that serves as a bookstore database

# ===== Importing external modules ===========
'''This is the section where modules are imported'''
import sqlite3


# ------------- CLASSES -------------

class Author():
    def __init__(self,id = None, name = None,country = None):
        self.id = id
        self.name = name
        self.country = country
        self.books = []

    def __str__(self):
        return ("-----Author Details-----\n"  
        f"Author ID: {self.id}\n" 
        f"Author: {self.name}\n"
        f"Country: {self.country}")

class Book():
    def __init__(self,id = None, title = None, author = None, genre = None, quantity = None, availability = "Yes"):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.availability = availability

        if self.author is not None:
            self.author.books.append(self)

    def __str__(self):
        return ("-----Book Details-----\n"  
        f"Book_ID: {self.id}\n" 
        f"Title: {self.title}\n"
        f"Author: {self.author.name}\n"
        f"Genre: {self.genre}\n"
        f"Availability: {self.availability}\n"
        f"Quantity: {self.quantity}")
    

        # Updaate availability status
    def available(self):
        """Update availability of book
        """
        self.availability = "Yes" if self.availability == "No" else "Yes"
        print(f"Book availability status changed to {self.availability}")
    
    
    def book_input(self):
        # Book_ID
        while True:
            self.id = input("Enter Book_ID: ").strip()
            if not (self.id.isdigit() and len(self.id) == 4):
                print("Invalid entry. Please enter 4-digit Book_ID (eg.1234)")
            else:
                print(f"Valid Book_ID: {self.id}")
                break

        # Title
        while True:
            self.title = input("Enter title of book: ").strip()
            if self.title:
                break
            else:
                print("Title field of book can not be empty.\nEnter 'unknown' if book title is not clear.")

        # Author
        while True:
            self.author = input("Enter author of book: ").strip()
            if self.author:
                print(f"Author: {self.author}")
                break
            else:
                print("Author field of book can not be empty.\nEnter 'unknown' if book author is not clear.")

        # Genre
        while True:
            self.genre = input("Enter genre of book: ").strip()
            if self.genre:
                print(f"Genre: {self.genre}")
                break
            else:
                print("Genre field can not be empty.\nEnter 'unknown' if book genre is not clear.")

        # Availability
        self.availability = "Yes"

        # Quantity
        while True:
            try:
                self.quantity = int(input("Enter number of copies of book: "))
                if self.quantity > 0:
                    print(f"Quantity: {self.quantity}")
                    break
                else:
                    print(f"The number of copies of {self.title} can not be negative or zero.")
            except ValueError:
                print(f"Invalid entry.(eg. {5} Copies of {self.title})")

# ------------- GLOBAL DATA -------------
books_list = []

# ------------- BOOK FUNCTIONS -------------

# View all books
def view_books(books_list):
    print("\n-----Books in Database-----")
    for index,book in enumerate(books_list,start=1):
        print(f"Book: {index}\n{book}")
        print("-"*40)


# Add book
def add_book(books_list):
    new_book = Book()
    new_book.book_input()
    
    books_list.append(new_book)

    with open("books.txt","a") as book_file:
        book_file.write(f"{new_book.id},{new_book.title},{new_book.author},{new_book.genre},{new_book.availability},{new_book.quantity}\n")
        print("Book added successfully! ")
        return books_list


# Delete book
def delete_book(books_list):
    view_books(books_list)

    while True:
        try:
            book_no = int(input("Enter the number of the book you wish to delete: "))
            if 1 <= book_no <= len(books_list):
                deleted_book = books_list.pop(book_no - 1) # Pythonically index starts at 0
                print(f"{deleted_book.title} has been deleted")

                with open("books.txt","w") as file:
                    for book in books_list:
                        file.write(f"{book.id},{book.title},{book.author},{book.genre},{book.availability},{book.quantity}\n")
                break
            else:
                print(f"Book No.{book_no} is not on the system.")
        except ValueError:
            print("Invalid entry. Please enter a digit")
    return books_list


def update_book(books_list):
    view_books(books_list)

    while True:
        try:
            book_no = int(input("Enter the number of the book you wish to delete: "))
            if 1 <= book_no <= len(books_list):
                selected_book = books_list[book_no - 1]
                print(f"Updating... {selected_book.title}")

                new_book_title = input("Enter the new title (leave blank to keep current): ").strip()
                if new_book_title:
                    selected_book.title = new_book_title
                
                new_book_quantity = input("Enter the new quantity (leave blank to keep current): ").strip()
                if new_book_quantity.isdigit():
                    selected_book.quantity = new_book_quantity

                while True:
                    selected_book_availability = input("Is the book available? (yes/no): ").strip().lower()
                    if selected_book_availability == "yes":
                        selected_book_availability.availability = "Yes"
                        break
                    elif selected_book_availability.availability == "no":
                        selected_book_availability.availability = "No"
                        break
                    else:
                        print("Invalid entry. Please enter 'Yes' or 'No'")
                
                print(f"{selected_book.title} has been successfully updated")
            else:
                print("Book number you have entered is out of range.")
        except ValueError:
            print("Invalid entry please enter a number.")

                


# Find book
def find_book(books_list):
    while True:
        choice = input( '''\nSearch options:
    1 - Search by code
    2 - Search by author
    3 - Search by title                                                                                            
    q - Exit program : ''').strip().lower()
    
        if choice == "q":
            print("Exiting...")
            break
                
        # By Code
        elif choice == "1":
            while True:
                search_book_id = input("Enter a book ID or (q to exit): ").strip().lower()
                if not search_book_id:
                    print("Book_ID can not be blank")
                    continue
                if search_book_id == "q":
                    print("Returning to main menu...")
                    break

                if not (search_book_id.isdigit() and len(search_book_id) == 4):
                    print("Invalid entry. Please enter 4-digit Book_ID (eg. 1234)")
                    continue

                found_book = [book for book in books_list if book.id == search_book_id]
                if found_book:
                    view_books(found_book)
                    break
                else:
                    print(f"Book_ID: {search_book_id} does not correspond with any book in the system.")
        
        # By Author
        elif choice == "2":
            while True:
                search_book_author = input("Enter author of book or (q to exit): ").strip().lower()
                if not search_book_author:
                    print("Author can not be blank")
                    continue

                if search_book_author == "q":
                    print("Returning to main menu...")
                    break
                found_author_book = [book for book in books_list if search_book_author in book.author.strip().lower()]  
                if found_author_book:
                    view_books(found_author_book)
                    break
                else:
                    print(f"Author: {search_book_author} does not correspond with any book in the system.")
        
        # By Title
        elif choice == "3":
            while True:
                search_book_title = input("Enter title of book or (q to exit): ").strip().lower()
                if not search_book_title:
                    print("Title can not be blank")
                    continue

                if search_book_title == "q":
                    print("Returning to main menu...")
                    break
                found_title_book = [book for book in books_list if search_book_title in book.title.strip().lower()]
                if found_title_book:
                    view_books(found_title_book)
                    break
                else:
                    print(f"Title: {search_book_title} does not correspond with any book in the system.")  
        else:
            print("Invalid entry. Please enter a number (eg. 1, 2, 3)")




