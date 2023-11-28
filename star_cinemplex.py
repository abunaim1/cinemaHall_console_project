class StarCinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def entry_hall(hall):
        StarCinema.hall_list.append(hall)
        
class Hall(StarCinema):
    def __init__(self, row, col, hall_no) -> None:
        self.row=row
        self.col=col
        self.hall_no=hall_no
        self.seats = {}
        self.show_list = []
        StarCinema.entry_hall(self)
        super().__init__()
    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        seats = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(0)
            seats.append(row)
        self.seats[id] = seats
             
        # self.seats[id] = [[0] * self.col for _ in range(self.row)]
    def view_show_list(self):
        print('--------------------------------------------------')
        for show in self.show_list:
            print(f'MOVIE NAME: {show[1]} ID: {show[0]} TIME: {show[2]}')
        print('--------------------------------------------------')
    def book_seats(self, id, row_num, col_num):
        seat = (row_num, col_num)
        if id in self.seats:
            for row in range(self.row):
                for col in range(self.col):
                    if row == row_num and col == col_num:
                        if self.seats[id][row][col] == 0:
                            self.seats[id][row][col] == 1
                    else:
                        print('INVALID ROW COLUMN')
                print()
            

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available Seats for Show {id}:")
            for seat in self.seats[id]:
                print(seat)    
        else:
            print(f"Show with ID {id} not found.")

    

h1 = Hall(5,5,1)
h1.entry_show(111, 'JAWAN', '12/December/2023')
h1.entry_show(232, 'Banglore Days', '12/December/2023')
h1.entry_show(111, 'Spider Man', '12/December/2023')

while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOKED TICKET')
    print('4. EXIT')
    print('Select an option: ')
    
    choice = int(input())
    if choice == 1:
        h1.view_show_list()
    if choice == 2:
        id = int(input('ENTER SHOW ID: '))
        h1.view_available_seats(id)
    if choice == 3:
        id = int(input('ENTER SHOW ID: '))
        row_num = int(input('ENTER ROW NUMBER: '))
        col_num = int(input('ENTER COLUMN NUMBER: '))
        h1.book_seats(id, row_num, col_num)
    if choice == 4:
        break

