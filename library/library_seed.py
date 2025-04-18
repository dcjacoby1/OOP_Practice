#seed file for library.py
from library import Book, Member, Library
import ipdb

# Create a library instance
library = Library()

# Create some sample books
book1 = Book("The Great Gatsby", "Fiction")
book2 = Book("To Kill a Mockingbird", "Fiction")
book3 = Book("Python Programming", "Technical")
book4 = Book("Data Science Basics", "Technical")
book5 = Book("Machine Learning", "Technical")

# Create some sample members
member1 = Member("Alice")
member2 = Member("Bob")
member3 = Member("Charlie")

# Add books to library
library.books.extend([book1, book2, book3, book4, book5])

# Add members to library
library.members.extend([member1, member2, member3])

# Print initial state
print("\n=== Initial Library State ===")
print(f"Total books: {len(library.books)}")
print(f"Total members: {len(library.members)}")

# Set debug point - code will pause here when you run 'python library_seed.py'
print("\n=== Debugger Starting ===")
print("You can now interact with the library system.")
print("Available objects: library, book1-5, member1-3")
print("Example commands:")
print("  p library.books  # Print all books")
print("  p member1.borrowed_books  # Check member's borrowed books")
print("  member1.borrow_book(book1)  # Borrow a book")
print("  p book1.available  # Check if book is available")
print("  c  # Continue execution")
print("  q  # Quit debugger")
ipdb.set_trace()

# After the debugger, you can continue with more operations
print("\n=== Debugger Session Ended ===")
print("Continuing with example operations...")

# Example operations
member1.borrow_book(book1)
member2.borrow_book(book2)
member1.borrow_book(book3)
member3.borrow_book(book4)
member2.borrow_book(book5)

# Demonstrate book returns
member1.return_book(book1)
member3.borrow_book(book1)

# Demonstrate member restriction
member2.restricted_member()
print(f"\nIs {member2.name} restricted? {member2.is_restricted}")

# Try to borrow a book while restricted (should not work)
member2.borrow_book(book3)
print(f"Books borrowed by {member2.name}: {[book.title for book in member2.borrowed_books]}")

# Unrestrict member
member2.unrestrict_member()
print(f"Is {member2.name} restricted? {member2.is_restricted}")

# Now member can borrow the book
member2.borrow_book(book3)

# Print final state
print("\n=== Final Library State ===")
print(f"Total books: {len(library.books)}")
print(f"Total members: {len(library.members)}")

# Show books by category
print("\n=== Books by Category ===")
fiction_books = library.category_list("Fiction")
print(f"Fiction books: {[book.title for book in fiction_books]}")
technical_books = library.category_list("Technical")
print(f"Technical books: {[book.title for book in technical_books]}")

# Show top borrowed books
top_books = library.top_3_borrowed_books()
print("\n=== Top Borrowed Books ===")
for book in top_books:
    print(f"{book.title}: {book.borrowed_count} times")

# Show member information
print("\n=== Member Information ===")
for member in library.members:
    print(f"\nMember: {member.name}")
    print(f"Borrowed Books: {[book.title for book in member.borrowed_books]}")
    print(f"Restricted: {member.is_restricted}")

print("\n=== Library Seed Complete ===") 