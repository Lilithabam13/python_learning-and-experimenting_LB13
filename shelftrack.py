# Shelf track is a program that serves as a bookstore database

# ===== Importing external modules ===========
'''This is the section where modules are imported'''
import sqlite3

# ------------- CLASSES -------------

class Author():
    """Represents an author of books
    
    Attributes:
        id (int): Indiviual identifier of an author
        name (str): Name of an author
        country (str): Birthplace of an author
        books (list): List of books written by authors

    Methods:
        _str_ : String representation of an author
        author_input : Prompt for author's id,
        name, country
    """
    def __init__(self,id = None, name = None,country = None):
        self.id = id
        self.name = name
        self.country = country
        self.books = []

    def __str__(self):
        return ("-----Author Details-----\n"  
        f"Author_ID: {self.id}\n" 
        f"Author: {self.name}\n"
        f"Country: {self.country}")
    
    def author_input(self,authors_list):
       # Author_ID 
        while True:
            author_id = input("\nEnter Author_ID (press Enter to auto-generate): ").strip()
            
            if author_id and any(author.id == author_id for author in authors_list):
                print(f"Author_ID: {author_id} already exists. Please enter unique Author_ID")
                continue
            
            if not author_id:
                self.id = str(len(authors_list)+1).zfill(4)
                break 
            elif (author_id.isdigit() and len(author_id) == 4):
                self.id = int(author_id)
                break
            else:
                print("Invalid entry. Please enter 4-digit Author_ID (eg.1234)")
        
        # Name
        while True:
            author_name = input("\nEnter Name of author: ").strip()
            if author_name:
                self.name = author_name
                break
            else:
                print("Name cannot be blank. Enter 'unknown' if unclear.")

        # Country
        while True:
            author_country = input("\nEnter Country which author is from: ").strip()
            if author_country:
                self.country = author_country
                break
            else:
                print("Country cannot be empty. Enter 'unknown' if unclear.")


class Book():
    """Represents book in bookstore
    
    Attributes:
        id (int): Individual identifier of a book
        title (str): Title of a book
        author (Author): Author object linked to a book
        genre (str): Genre of a book
        quantity (int): Number of copies of a book
        availability (str): 'Yes'/'No' indicating if book is available
    
    Methods:
        _str_ : String representation of a book
        available() : Toggle availability of a book
        book_input() : Prompt for a book's id, title
        author, genre, availability, quantity
    """
    def __init__(self,id = None, title = None, author = None, genre = None, quantity = None, availability = "Yes"):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = int(quantity) if quantity is not None else 0
        self.availability = availability

        if isinstance (self.author,Author):
            self.author.books.append(self)

    def __str__(self):
        author_name = self.author.name if self.author else "Unknown"
        return ("-----Book Details-----\n"  
        f"Book_ID: {self.id}\n" 
        f"Title: {self.title}\n"
        f"Author: {author_name}\n"
        f"Genre: {self.genre}\n"
        f"Availability: {self.availability}\n"
        f"Quantity: {self.quantity}")
    

        # Update availability status
    def available(self):
        """Update availability of book"""

        self.availability = "No" if self.availability == "Yes" else "Yes"
        print(f"Book availability status changed to {self.availability}")
    
    
    def book_input(self, authors_list, books_list):
        # Book_ID
        self.id = (3000 + len(books_list) + 1)
        print(f"Auto-generated Book_ID: {str(self.id).zfill(4)}")

        # Title
        while True:
            self.title = input("\nEnter title of book: ").strip()
            if self.title:
                break
            else:
                print("Title cannot be empty. Enter 'unknown' if book title is not clear.")

        # Author
        while True:
            author_of_book = input("\nEnter Author of book: ").strip()
            if not author_of_book:
                print("Author cannot be blank. Enter 'unknown' if  book author is not clear.")
                continue
            
            known_author = next((author for author in authors_list if author.name.lower() == author_of_book.lower()), None) 
            if known_author:
                self.author = known_author
                break
            else:
                new_author = Author()
                new_author.author_input(authors_list)
                self.author = new_author
                authors_list.append(new_author)
                print(f"Author: {new_author.name}, Author_ID: {new_author.id} has been created.")
                break

        # Genre
        while True:
            self.genre = input("\nEnter Genre of book: ").strip()
            if self.genre:
                print(f"Genre: {self.genre}")
                break
            else:
                print("Genre cannot be empty.\nEnter 'unknown' if book genre is not clear.")
        
        # Availability
        while True:
            self.availability = input("\nIs the book available? (Yes/No): ").strip().capitalize()
            if self.availability in ("Yes", "No"):
                break
            else:
                print("Invalid entry. Please enter 'Yes' or 'No' only.")

        # Quantity
        while True:
            book_copies = input("\nEnter the quantity of copies (Eg. 0, 1, 2 ...): ")
            if book_copies.isdigit():
                self.quantity = int(book_copies)
                print(f"Quantity: {self.quantity}")
                break
            else:
                print(f"Invalid entry. Please enter a number.")

# ------------- GLOBAL DATA -------------
books_list = []
authors_list = []

# ------------- BOOK FUNCTIONS -------------


# Save book
def save_books(books_list):
    """Saves all books in the in-memory list to 
    books text file.

    Returns:
    books_list (list): List of book objects
    """
    with open("books.txt","w") as file:
        for book in books_list:
            file.write(f"{book.id},{book.title},{book.author.name},{book.genre},{book.availability},{book.quantity}\n")


# View all books
def view_books(books_list):
    """Displays all the books in the system.

    Uses _str_ method of Book class to display book details in
    user-friendly format.

    Args:
        books_list (list): List of Book objects.
    """
    if not books_list:
        print("No books in database")
        return
    else:
        print("\n-----Books in Database-----")
        for index,book in enumerate(books_list,start=1):
            print(f"Book: {index}\n{book}")
            print("-"*40)


# Add book
def add_book(authors_list, books_list):
    """Add new book into existing books list using
    book_input function and update in-memory lists.
    
    Args:
        authors_list (list): List of Author objects
        books_list (list): List of Book objects
    
    Returns:
        books_list (list): Updated list of Book objects
    """
    new_book = Book()
    new_book.book_input(authors_list,books_list)
    
    books_list.append(new_book)

    with open("books.txt","a") as file:
        file.write(f"{new_book.id},{new_book.title},{new_book.author.name},{new_book.genre},{new_book.availability},{new_book.quantity}\n")
    print(f"{new_book.title} by {new_book.author.name} has been added successfully! ")
    return books_list


# Delete book
def delete_book(books_list):
    """Delete existing book from list of Book objects
    and update in-memory lists.

    Args: 
        books_list (list): List of Book objects

    Returns:
        books_list (list): Updated of Book objects
    """
    view_books(books_list)

    while True:
        try:
            book_no = input("\nEnter the number of the book you wish to delete: ").strip()
            if book_no.isdigit():
                book_no = int(book_no)
            if 1 <= book_no <= len(books_list):
                deleted_book = books_list.pop(book_no - 1) # Pythonically index starts at 0
                print(f"{deleted_book.title} has been deleted")
                save_books(books_list)
                return deleted_book
            else:
                print(f"Book No.{book_no} is not on the system.")
        except ValueError:
            print("Invalid entry. Please enter a digit")


def update_book(books_list):
    """Edit an existing book from list of Book objects
    and update in-memory lists.
    
    Args:
        books_list (list): List of Book objects
    
    Returns:
        books_list (list): Updated of Book objects
    """
    view_books(books_list)
    while True:
        try:
            book_no = int(input("\nEnter the number of the book you wish to update: "))
            if 1 <= book_no <= len(books_list):
                selected_book = books_list[book_no - 1]
                print(f"Updating... {selected_book.title}")

                new_book_title = input("\nEnter the new title (press Enter to keep current): ").strip()
                if new_book_title:
                    selected_book.title = new_book_title
                
                new_book_quantity = input("\nEnter the new quantity (press Enter to keep current): ").strip()
                if new_book_quantity.isdigit():
                    selected_book.quantity = int(new_book_quantity)

                while True:
                    selected_book_availability = input("\nIs the book available? (yes/no): ").strip().lower()
                    if selected_book_availability == "yes":
                        selected_book.availability = "Yes"
                        break
                    elif selected_book_availability == "no":
                        selected_book.availability = "No"
                        break
                    else:
                        print("Invalid entry. Please enter 'Yes' or 'No'")
                
                print(f"{selected_book.title} has been successfully updated")
                save_books(books_list)
                return selected_book
            else:
                print("Book number you have entered is out of range.")        
        except ValueError:
            print("Invalid entry please enter a number.")   
        
 
# Find book
def find_book(books_list):
    """Find an existing book from the list of Book objects.
    User can search for book via book's id, author
    and title respectively.
        
    Args:
        books_list (list): List of Book objects
    
    Returns:
        A book (Book): A single Book object
        """
    if not books_list:
        print("No books in database")
        return
    else:
        while True:
            choice = input( '''\nSearch options:
        1 - Search by code
        2 - Search by author
        3 - Search by title                                                                                            
        q - Exit program : ''').strip().lower()
    
            if choice == "q":
                print("Exiting...")
                return None
                
            # By Code
            elif choice == "1":
                while True:
                    search_book_id = input("\nEnter a book ID or (q to exit): ").strip().lower()
                    if not search_book_id:
                        print("Book_ID cannot be blank")
                        continue
                    if search_book_id == "q":
                        print("Returning to main menu...")
                        break

                    if not search_book_id.isdigit():
                        print("Invalid entry. Please enter 4-digit Book_ID (eg. 1234)")
                        continue

                    search_book_id = int(search_book_id)
                    found_book = [book for book in books_list if book.id == search_book_id]
                    if found_book:
                        view_books(found_book)
                        return found_book[0]
                    else:
                        print(f"Book_ID: {search_book_id} does not correspond with any book in the system.")
        
            # By Author
            elif choice == "2":
                while True:
                    search_book_author = input("\nEnter author of book or (q to exit): ").strip().lower()
                    if not search_book_author:
                        print("Author cannot be blank")
                        continue

                    if search_book_author == "q":
                        print("Returning to main menu...")
                        break
                    found_author_book = [book for book in books_list if search_book_author in book.author.name.strip().lower()]  
                    if found_author_book:
                        view_books(found_author_book)
                        return found_author_book[0]
                    else:
                        print(f"Author: {search_book_author} does not correspond with any book in the system.")
        
            # By Title
            elif choice == "3":
                while True:
                    search_book_title = input("\nEnter title of book or (q to exit): ").strip().lower()
                    if not search_book_title:
                        print("Title cannot be blank")
                        continue

                    if search_book_title == "q":
                        print("Returning to main menu...")
                        break
                    found_title_book = [book for book in books_list if search_book_title in book.title.strip().lower()]
                    if found_title_book:
                        view_books(found_title_book)
                        return found_title_book[0]
                    else:
                        print(f"Title: '{search_book_title}' does not correspond with any book in the system.")  
            else:
                print("Invalid entry. Please enter a number (eg. 1, 2, 3)")


# ------------- DATABASE -------------
def setup_dbms(authors_list,books_list):
    """Create author/book tables if they do
    not exist and populate them.
    
    Args:
        authors_list (list): In-memory of list of Author objects.
        books_list (list): In-memory of Book objects.
    """
    db_book = sqlite3.connect("ebookstore.db")
    cursor = db_book.cursor()

    # Table Creation
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS author (
        id INTEGER PRIMARY KEY UNIQUE,
        name TEXT,
        country TEXT)
        """
    )
                    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY UNIQUE,
        title TEXT, 
        authorID INTEGER,
        qty INTEGER,
        FOREIGN KEY (authorID) REFERENCES author (id))    
        """
    )

    # Insertion of author/book data
    author_data = [(author.id, author.name, author.country) for author in authors_list]
    cursor.executemany("""
    INSERT OR IGNORE INTO author (id, name, country)
    VALUES (?, ?, ?)""",author_data
    )

    book_data = [(book.id, book.title, book.author.id, book.quantity) for book in books_list]
    cursor.executemany("""
    INSERT OR IGNORE INTO book (id, title, authorID, qty)
    VALUES (?, ?, ?, ?)""", book_data
    )
    db_book.commit()
    db_book.close()

# ------------- DATABASE OPERATIONS -------------

# Add book
def add_db():
    """Database operation to add new book and author
    to local SQLite database(ebookstore).
    
    Prompt user for author/book details, create missing author
    and inserts both into database.
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor() 
        
        add_book(authors_list, books_list)
        new_book = books_list[-1]
        if new_book:
            cursor.execute("""
                INSERT OR IGNORE INTO book(id, title, authorID, qty)
                VALUES (?, ?, ?, ?)""", 
                (new_book.id, new_book.title, new_book.author.id, new_book.quantity))
            db_book.commit()
            print(f"Book_ID: {new_book.id} Title: '{new_book.title}' addition successfull")
        else:
            print("Addition of book failed.")
    except Exception as e:
        db_book.rollback()
        raise e
    finally:
        db_book.close()


# Delete book
def delete_book_db():
    """Database operation to delete existing book
    to local SQLite database(ebookstore).
    
    Displays available books, allowing user to select which book 
    they wish to delete, uses delete_book() as part
    of its work to update text file
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor()    
    
        deleted_book = delete_book(books_list)
        if deleted_book:
            cursor.execute("""
                DELETE FROM book WHERE id = ?""",(deleted_book.id,))
            db_book.commit()
            print(f"Book_ID: {deleted_book.id} Title: '{deleted_book.title}' has been deleted successfully")
        else:
            print("Book not found in database.")
    except Exception as e:
        db_book.rollback()
        raise e
    finally:
        db_book.close()

    
# Search book    
def search_book_db():
    """Database operation to search for existing book
    within local SQLite database(ebookstore).
    
    Uses find_book() function.
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor()
    
        found_book = find_book(books_list)
        if found_book:
            cursor.execute("""
                SELECT id, title, authorID, qty FROM book WHERE id = ?""", (found_book.id,))
            found_row = cursor.fetchone()
            db_book.commit()

            if found_row:
                print(f"----- Book Details -----\n" 
                    f"ID: {found_row[0]}\n"
                    f"Title: {found_row[1]}\n" 
                    f"Author_ID: {found_row[2]}\n" 
                    f"Quantity: {found_row[3]}")
            else:
                print("Book not found in database.")
        else:
            print("Book not found in database.")
    except Exception as e:
        db_book.rollback()
        raise e
    finally:
        db_book.close()
        

# Update book/author        
def update_book_author_db():
    """Update an existing book/author record in within ebookstore.
    
    Prompts user to update book/author details respectively.
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor()
        
        updated_id = input("Enter book ID to update: ").strip()
        if not updated_id:
            print("Book_ID cannot be blank")
            return
        if not updated_id.isdigit():
            print("Book_ID must be a number ")
            return
        updated_id = int(updated_id)
    
        # Fetch book/author info
        cursor.execute("""
            SELECT book.id, book.title, book.authorID, book.qty, author.id, author.name, author.country
            FROM book
            INNER JOIN author
                ON book.authorID = author.id
            WHERE book.id = ?""",(updated_id,))
    
        found_row = cursor.fetchone()

        if not found_row:
            print(f"Book_ID: {updated_id} does not correspond with any book in the system")
            return 
        
        book_id, book_title, book_authorID ,book_qty, author_id, author_name, author_country = found_row

        # All vaild author IDs
        cursor.execute("""
            SELECT id FROM author""")
        authors = [row[0] for row in cursor.fetchall()]

        # Author info update
        new_author_name = input(f"Enter new author name (press Enter to keep current, {author_name}): ").strip() or author_name
        new_author_country = input(f"Enter new author country (press Enter to keep current, {author_country}): ").strip() or author_country 

        # Book info update
        while True:
            new_book_qty_input = input(f"Enter new book quantity (press Enter to keep current, {book_qty}): ")
            if not new_book_qty_input:
                new_book_qty = book_qty
                break
            elif new_book_qty_input.isdigit():
                new_book_qty = int(new_book_qty_input)
                break
            else:
                print("Enter valid number only or press Enter to keep current")

        new_book_title = input(f"Enter new book title (press Enter to keep current, {book_title}): ").strip() or book_title 

        while True:
            new_authorID_input = input(f"Enter new book authorID (press Enter to keep current, {author_id}): ")
            if not new_authorID_input:
                new_book_authorID = book_authorID
                break
            elif new_authorID_input.isdigit():
                new_book_authorID = int(new_authorID_input)
                if new_book_authorID in authors:
                    break
                else:
                    print(f"AuthorID:{new_book_authorID} does not exist in the system.")
            else:
                print("Enter valid number author ID only or (press Enter to keep current) ")

        # Update book
        cursor.execute("""
                UPDATE book SET qty = ?, title = ?, authorID = ? WHERE id = ?""",(
                new_book_qty, new_book_title, new_book_authorID, book_id))
    
        # Update author
        if new_book_authorID == author_id:
            cursor.execute("""        
                UPDATE author SET name = ?, country = ? WHERE id = ?""",(
                new_author_name, new_author_country, author_id))

        db_book.commit()
        sync_with_dbms(authors_list,books_list)
        
        print(f"Book: '{new_book_title}' by Author: {new_author_name} updated successfully")
        if new_book_authorID == author_id:
            print(f"Author:{new_author_name}'s details have been updated successfully")
        else:
            print(f"Book: {new_book_title} is now linked to Author_ID: {new_book_authorID}")

    except Exception as e:
        db_book.rollback()
        print(f"\nAn error occured: {e}\n")
        sync_with_dbms(authors_list,books_list)
    finally:
        db_book.close()


def view_all_books_db():
    """Database operation to view existing book
    within ebookstore database.
    
    Displays databse records in user-friendly fashion
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor()

        cursor.execute("""
            SELECT book.title, author.name, author.country
            FROM book
            INNER JOIN author
                ON book.authorID = author.id
            ORDER BY book.title""")
    
        found_rows = cursor.fetchall()
        if not found_rows:
            print("\nBooks not found in system\n")
            return
    
        print("\n---------- Details ----------\n")
        for title, name, country in found_rows:
            print(f"Title: {title} ")
            print(f"Author's Name: {name}")
            print(f"Author's Country: {country}")
            print("-" * 50)
    
    except Exception as e:
        print(f"An error occurred while displaying book details: {e}\n")
    finally:
        db_book.close()


def sync_with_dbms(authors_list, books_list):
    """Sync in-memory book and author lists respectively
    to match SQLite database.

    Called from setup_dbms() or after major database updates
    such as add_db() or update_book_author_db()

    Args:
        authors_list (list): List to populate with Author objects
        books_list (list): List to populate Book objects
    """
    try:
        db_book = sqlite3.connect("ebookstore.db")
        cursor = db_book.cursor()

        books_list.clear()
        authors_list.clear()

        cursor.execute("SELECT id, name, country FROM author")
        for row in cursor.fetchall():
            author_id, name, country = row
            authors_list.append(Author(author_id, name, country))

        cursor.execute("SELECT id, title, authorID, qty FROM book")
        for row in cursor.fetchall():
            book_id, title, author_id, qty = row
            author_obj = next((author for author in authors_list if author.id == author_id),None)
            
            if author_obj is None:
                author_obj = Author(author_id,f"Unknown Author {author_id}", "Unknown")
                authors_list.append(author_obj)

                cursor.execute("INSERT OR IGNORE INTO author (id, name, country) VALUES (?, ?, ?)",(author_id, author_obj.name, author_obj.country)
                )
                
            books_list.append(Book(book_id, title, author_obj, genre="Unknown", quantity=qty))
        
        db_book.commit()
        print("\nIn-memory data in sync with database\n")
    
    except Exception as e:
        print(f"Error occured while syncing data: {e}")
    finally:
        db_book.close()


# Menu
def menu():
    """Displays the main menu options

    Returns:
        menu_choice(int): A user's selected option
    """
    while True:
        try:
            menu_choice = int(input( '''\nSelect one of the following options
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View details of all books
0. Exit : ''').strip())
            if menu_choice in range(0, 6):
                return menu_choice
            else:
                print("Invalid option. Select from 0 to 5")
        except ValueError:
            print("Invalid entry. Number's only (eg. 0 - 5)")

# ------------- MENU (Program flow) -------------

def main():
    """Main control flow for the Shelf Track system"""
    setup_dbms(authors_list,books_list)
    sync_with_dbms(authors_list, books_list)

    while True:
        operation = menu()

        if operation is None:
            continue

        if operation == 1:
            add_db()

        elif operation == 2:
            update_book_author_db()
    
        elif operation == 3:
            delete_book_db()

        elif operation == 4:
            search_book_db()

        elif operation == 5:
            view_all_books_db()

        elif operation == 0:
            print('Goodbye!!!')
            break
        else:
            print("You have entered an invalid input. Please try again")
if __name__ == "__main__":
    main()
    


   








































# # Update book
# def update_book_db():
#     try:
#         db_book = sqlite3.connect("ebookstore.db")
#         cursor = db_book.cursor() 

#         updated_book = update_book(books_list)
#         if updated_book:
#             cursor.execute("""
#                 UPDATE book SET qty = ?, title = ?, authorID = ? WHERE id = ?""",(
#                 updated_book.quantity, updated_book.title, updated_book.author.id, updated_book.id))
#             db_book.commit()
#             print(f"Book_ID:{updated_book.id} Title: '{updated_book.title}' update successfull")
#         else:
#             print("Book not found in database.")
#     except Exception as e:
#         db_book.rollback()
#         raise e
#     finally:
#         db_book.close()
