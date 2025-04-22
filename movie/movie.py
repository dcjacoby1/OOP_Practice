# Prompt:
# Design a movie theater booking backend that handles movies, showtimes, and seat reservations.

# Required methods:

# How do you add a new showtime to a movie?

# How can a customer reserve a seat?

# How do you cancel a reservation?

# How do you check available seats for a showtime?

# How do you list all showtimes for a movie?

# How do you find which customers booked a specific showtime?

# How do you check if a seat is reserved?


class Movie:
    def __init__(self, title):
        self.title = title
        self.showtimes = []
    
    def add_showtime(self, showtime):
        if isinstance(showtime, Showtime) and showtime not in self.showtimes:
            self.showtimes.append(showtime)

    def movie_showtimes(self):
        return self.showtimes

    def __repr__(self):
        return f"Movie(title='{self.title}')"


class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer(name='{self.name}')"


class Seat:
    def __init__(self, row, seat_number):
        self.row = row
        self.seat_number = seat_number
        self.reserved = False

    def __repr__(self):
        status = "Reserved" if self.reserved else "Available"
        return f"Seat(row={self.row}, number={self.seat_number}, status='{status}')"


class Showtime:
    def __init__(self, movie, time):
        if not isinstance(movie, Movie):
            raise ValueError("movie must be an instance of Movie class")

        self.movie = movie
        self.time = time
        self.row = 5
        self.seat_number = 10
        self.seats = [[Seat(row, seat_number) for seat_number in range(self.seat_number)] for row in range(self.row)]
        self.reservations = {}

    def reserve_seat(self, row, seat_number, customer):
        if not isinstance(customer, Customer):
            raise ValueError("movie must be an instance of Movie class")
        if 0 <= row < self.row and 0 <= seat_number < self.seat_number:
            seat = self.seats[row][seat_number]
        if not seat.reserved:
            seat.reserved = True
            self.reservations[(row, seat_number)] = customer
    
    def cancel_reservation(self, row, seat_number):
        if 0 <= row < self.row and 0 <= seat_number < self.seat_number:
            seat = self.seats[row][seat_number]
        if seat.reserved:
            seat.reserved = False
            del self.reservations[(row, seat_number)]

    def available_seats(self):
        return[(r.row, r.seat_number) for row in self.seats for r in row if not r.reserved]
    
    def reservation_by_customer(self):
        return list(self.reservations.values())

    def __repr__(self):
        return f"Showtime(movie='{self.movie.title}', time='{self.time}')"

    
