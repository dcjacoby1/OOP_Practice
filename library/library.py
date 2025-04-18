"""
Library Management System

This module implements a simple library management that handles the following requiremnts:

1. member can borrow a book
2. member can return a book
3. which books are borrowed by member
4. add new book to library
5. remove book not in circulation
6. check if book is available
7. list all books in category
8. list top 3 borrowed books
9. restrict a member from borrowing a book
"""

class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.available= True
        self.borrowed_count = 0
    
    def __repr__(self):
        return f"Book(title='{self.title}', category='{self.category}', available={self.available}, borrowed_count={self.borrowed_count})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.is_restricted = False
    
    def borrow_book(self, book):
        if book.available and not self.is_restricted:
            self.borrowed_books.append(book)
            book.available = False
            book.borrowed_count += 1
            
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True

    def restricted_member(self):
        self.is_restricted = True
    
    def unrestrict_member(self):
        self.is_restricted = False
    
    def __repr__(self):
        return f"Member(name='{self.name}', is_restricted={self.is_restricted})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def check_book_availability(self, book):
        if book.available:
            print("book is available")
        else:
            print("book is unavailable")

    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("book is not in the library")
    
    def book_list(self):
        return self.books
    
    def category_list(self, category):
        category_list = []
        for book in self.books:
            if book.category == category:
                category_list.append(book)
        return category_list
    
    def top_3_borrowed_books(self):
        return sorted(self.books, key=lambda x: x.borrowed_count, reverse=True)[:3]
    
    def __repr__(self):
        book_count = len(self.books)
        member_count = len(self.members)
        return f"Library(books={book_count}, members={member_count})"




        