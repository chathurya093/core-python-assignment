# Initialize total seats and booked seats
total_seats = 10
booked_seats = [2, 5, 7]

# Function to book a seat
def book_seat(seat_number):
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number > total_seats or seat_number < 1:
        print(f"Seat {seat_number} is invalid.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} booked successfully.")

# Function to cancel a booking
def cancel_seat(seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} booking canceled.")
    else:
        print(f"Seat {seat_number} is not booked.")

# Example actions
book_seat_number = 3
cancel_seat_number = 5

book_seat(book_seat_number)
cancel_seat(cancel_seat_number)

# Compute available seats
available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
print("Available seats:", available_seats)
