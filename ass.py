class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        # Initialize seats information
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                seat_key = f"{row}-{col}"
                self.seats[seat_key] = {"status": "available", "reservation": None}

        # Insert the object into Star_Cinema's hall_list
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.show_list.append(show_info)

        # Allocate seats with rows and cols using a 2D list
        seat_allocation = [["free" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation

    def book_seats(self, show_id, seat_list):
        if show_id in self.seats:
            for seat in seat_list:
                row, col = seat
                seat_key = f"{row}-{col}"
                if self.seats[show_id][row-1][col-1] == "free":
                    self.seats[show_id][row-1][col-1] = "booked"
                else:
                    print(f"Seat {seat_key} is already booked.")
        else:
            print(f"Show with ID {show_id} not found.")

    def view_show_list(self):
        print("Show List:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"Available Seats for Show {show_id}:")
            for row_num, row in enumerate(self.seats[show_id], start=1):
                for col_num, status in enumerate(row, start=1):
                    if status == "free":
                        print(f"Row {row_num}, Col {col_num}")
        else:
            print(f"Show with ID {show_id} not found.")

# Example usage:
# Creating an instance of the Hall class
hall1 = Hall(rows=8, cols=12, hall_no=1)

# Adding a show to the hall
hall1.entry_show(show_id="S1", movie_name="Avengers: Endgame", show_time="18:00")

# Viewing the show list
hall1.view_show_list()

# Booking seats for the show
hall1.book_seats(show_id="S1", seat_list=[(1, 2), (2, 3)])

# Viewing available seats for the show
hall1.view_available_seats(show_id="S1")
