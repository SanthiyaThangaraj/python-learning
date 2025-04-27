'''Create a class Book with:

A method details() that prints "This is a book"

Create a class Textbook that inherits from Book.

Task:

Create an object of Textbook and call details() method.'''

class book:
    def details(self):
        print("This is a book")

class textbook(book):
    def deta(self):
        print("This is a tamil book")

obj=textbook()
obj.details()
obj.deta()
