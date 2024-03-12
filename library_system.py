class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}
        self.transactions = []

    def add_book(self, title, author, copies):
        book_id = len(self.books) + 1
        self.books[book_id] = {'title': title, 'author': author, 'copies': copies}

    def add_patron(self, name):
        patron_id = len(self.patrons) + 1
        self.patrons[patron_id] = {'name': name, 'books_borrowed': []}
 
    def borrow_book(self, patron_id, book_id): 
        if patron_id in self.patrons and book_id in self.books:
            if self.books[book_id]['copies'] > 0:
                self.patrons[patron_id]['books_borrowed'].append(book_id)
                self.books[book_id]['copies'] -= 1 
                self.transactions.append({'type': 'Borrow', 'patron_id': patron_id, 'book_id': book_id})
                print("Book borrowed successfully.")
            else:
                print("Sorry, the book is currently not available.")
        else: 
            print("Invalid patron ID or book ID.")


     def return_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            if book_id in self.patrons[patron_id]['books_borrowed']:
                self.patrons[patron_id]['books_borrowed'].remove(book_id)
                self.books[book_id]['copies'] += 1
                self.transactions.append({'type': 'Return', 'patron_id': patron_id, 'book_id': book_id}) 
                print("Book returned successfully.")
            else:
                print("This book is not borrowed by the specified patron.")
        else:
            print("Invalid patron ID or book ID.")

    def display_books(self):
        print("Books in the library:")
        for book_id, book_info in self.books.items():
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Copies: {book_info['copies']}")

    def display_patrons(self):
        print("Patrons in the library:")
        for patron_id, patron_info in self.patrons.items():
            print(f"ID: {patron_id}, Name: {patron_info['name']}, Books Borrowed: {patron_info['books_borrowed']}")

    def display_transactions(self):
        print("Library transactions:")
        for transaction in self.transactions:
            print(transaction)


# Example usage:
library_system = Library() 

library_system.add_book("Introduction to Python", "John Doe", 5)
library_system.add_book("Data Science Basics", "Jane Smith", 3)

library_system.add_patron("Alice Johnson")
library_system.add_patron("Bob Williams")

library_system.borrow_book(1, 1)
library_system.borrow_book(1, 2)
library_system.borrow_book(2, 1)

library_system.return_book(1, 1)
library_system.return_book(1, 2)

library_system.display_books()
library_system.display_patrons()
library_system.display_transactions()
# Agoo & MSFT Inc. 2024 tM
