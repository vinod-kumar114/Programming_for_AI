"""Create a Python program for a library system.

Create a class Book with attributes title and author. Create a class Library that stores multiple Book objects. Add a method add_book() to add a book to the library. Add a method display_books() to display all books available in the library. Create at least three Book objects and add them to a Library object."""


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Library:
    def __init__(self):
        self.book_dict = {}

    def addBook(self, book):
        self.book_dict[book.title] = {
            "author": book.author,
            "price": book.price
        }

    def display_books(self):
        if not self.book_dict:
            print("No books available")
        else:
            for k, v in self.book_dict.items():
                print("Book title:", k)
                print("Author:", v["author"])
                print("Price:", v["price"])

b1 = Book("OOP in C++", "Robert", 1000)
b2 = Book("OOP in Python", "Danson", 1000)
b3 = Book("OOP in Java", "Albert", 1000)

lib = Library()

lib.addBook(b1)
lib.addBook(b2)
lib.addBook(b3)
lib.display_books()
