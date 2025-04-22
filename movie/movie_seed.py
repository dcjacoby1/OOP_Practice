#!/usr/bin/env python3
"""
Movie Theater Booking System Seed File
Run this file with: python movie_seed.py
"""

from movie import Movie, Customer, Showtime
import ipdb

# Create some movies
movie1 = Movie("The Godfather")
movie2 = Movie("Star Wars")
movie3 = Movie("The Shawshank Redemption")

# Create some customers
customer1 = Customer("John Smith")
customer2 = Customer("Jane Doe")
customer3 = Customer("Bob Johnson")

# Create showtimes for movies
showtime1 = Showtime(movie1, "19:00")  # The Godfather at 7 PM
showtime2 = Showtime(movie1, "22:00")  # The Godfather at 10 PM
showtime3 = Showtime(movie2, "20:00")  # Star Wars at 8 PM
showtime4 = Showtime(movie3, "18:00")  # Shawshank at 6 PM

# Add showtimes to movies
movie1.add_showtime(showtime1)
movie1.add_showtime(showtime2)
movie2.add_showtime(showtime3)
movie3.add_showtime(showtime4)

# Make some reservations
showtime1.reserve_seat(0, 0, customer1)  # John Smith in first row, first seat
showtime1.reserve_seat(0, 1, customer2)  # Jane Doe in first row, second seat
showtime2.reserve_seat(1, 5, customer3)  # Bob Johnson in second row, sixth seat
showtime3.reserve_seat(2, 2, customer1)  # John Smith in third row, third seat

# Print initial state
print("\n=== Initial Theater State ===")
print(f"Movies: {[movie.title for movie in [movie1, movie2, movie3]]}")
print(f"Customers: {[customer.name for customer in [customer1, customer2, customer3]]}")
print(f"Showtimes for {movie1.title}: {[showtime.time for showtime in movie1.movie_showtimes()]}")

# Set debug point
print("\n=== Debugger Starting ===")
print("You can now interact with the movie theater system.")
print("Available objects: movie1-3, customer1-3, showtime1-4")
print("Example commands:")
print("  p showtime1.available_seats()  # Check available seats")
print("  p showtime1.reservation_by_customer()  # List customers with reservations")
print("  p movie1.movie_showtimes()  # List showtimes for a movie")
print("  c  # Continue execution")
print("  q  # Quit debugger")
ipdb.set_trace()

# After the debugger, demonstrate some operations
print("\n=== Demonstrating Operations ===")

# Check available seats
print(f"\nAvailable seats for {movie1.title} at {showtime1.time}:")
print(showtime1.available_seats())

# List customers with reservations
print(f"\nCustomers with reservations for {movie1.title} at {showtime1.time}:")
print([customer.name for customer in showtime1.reservation_by_customer()])

# Cancel a reservation
print(f"\nCanceling {customer1.name}'s reservation...")
showtime1.cancel_reservation(0, 0)

# Check available seats again
print(f"\nAvailable seats for {movie1.title} at {showtime1.time} after cancellation:")
print(showtime1.available_seats())

# List all showtimes for a movie
print(f"\nAll showtimes for {movie1.title}:")
for showtime in movie1.movie_showtimes():
    print(f"Time: {showtime.time}")
    print(f"Available seats: {len(showtime.available_seats())}")

print("\n=== Movie Seed Complete ===") 